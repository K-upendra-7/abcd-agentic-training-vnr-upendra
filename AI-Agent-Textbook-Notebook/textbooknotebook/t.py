# %% [markdown]
# 🧠 AI Agent — Textbook → Notebook Notes Generator
# Local LLaMA 3 (8B) + Gemini Evaluation + Auto PDF Export

# %%
!ollama pull llama3:8b
!ollama serve

# %%
import os
import json
import gradio as gr
import textwrap
import asyncio
import markdown_it
from dotenv import load_dotenv
from openai import AsyncOpenAI
from pypdf import PdfReader
from pydantic import BaseModel
from fpdf import FPDF

# %%
# Load environment variables
load_dotenv(override=True)

openai_api_key = os.getenv("OPENAI_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

if openai_api_key:
    print(f"✅ OpenAI API Key found ({openai_api_key[:8]}...)")
else:
    print("⚠️ OpenAI API Key not found. Set it in your .env file.")

if google_api_key:
    print(f"✅ Google API Key found ({google_api_key[:8]}...)")
else:
    print("⚠️ Google API Key not found. Set it in your .env file.")

# %%
# Async clients
ollama_client = AsyncOpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

gemini_client = AsyncOpenAI(
    api_key=google_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# %%
# Model for structured evaluator feedback
class Evaluation(BaseModel):
    is_acceptable: bool
    feedback: str

# %%
# -----------------------------
# NOTE GENERATION + EVALUATION
# -----------------------------

async def generate_notes(text_chunk: str, retries=2, feedback=""):
    """
    Generate structured notes for a given text chunk using LLaMA3:8b.
    Auto-retries with feedback from Gemini evaluation if needed.
    """
    system_prompt = (
        "You are an expert academic assistant. "
        "Produce clear, well-structured Markdown notes summarizing key ideas, "
        "definitions, and concepts from the provided text."
    )

    if feedback:
        user_prompt = (
            f"Improve the previous notes using this feedback:\n{feedback}\n\n"
            f"Original text:\n{text_chunk}"
        )
    else:
        user_prompt = f"Generate concise academic notes for the following text:\n{text_chunk}"

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    try:
        response = await ollama_client.chat.completions.create(
            model="llama3:8b",
            messages=messages,
        )
        notes = response.choices[0].message.content
    except Exception as e:
        print(f"❌ Ollama generation error: {e}")
        return f"Error generating notes: {e}"

    if retries > 0:
        evaluation = await evaluate_notes(text_chunk, notes)
        if not evaluation.is_acceptable:
            print(f"🔁 Retrying with feedback: {evaluation.feedback}")
            return await generate_notes(text_chunk, retries - 1, evaluation.feedback)
        else:
            print("✅ Evaluation passed.")
    return notes


async def evaluate_notes(text_chunk: str, notes: str) -> Evaluation:
    """
    Evaluates generated notes using Gemini for accuracy and clarity.
    """
    prompt = (
        "You are a quality evaluator. Check if the notes correctly and clearly summarize the text. "
        "Respond in JSON with keys: is_acceptable (bool) and feedback (string).\n\n"
        f"--- Original Text ---\n{text_chunk}\n\n"
        f"--- Notes ---\n{notes}"
    )

    try:
        response = await gemini_client.chat.completions.create(
            model="gemini-flash2.5",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
        )
        data = json.loads(response.choices[0].message.content)
        return Evaluation(**data)
    except Exception as e:
        print(f"⚠️ Gemini evaluation error: {e}")
        return Evaluation(is_acceptable=True, feedback=f"Evaluation failed: {e}")

# %%
# -----------------------------
# UTILITIES
# -----------------------------

def chunk_text(text: str, max_chars: int = 2500):
    """Split long text into smaller chunks."""
    return textwrap.wrap(text, width=max_chars, break_long_words=False, replace_whitespace=False)


def create_pdf_file(notes_markdown: str, source_filename: str) -> str:
    """
    Convert Markdown notes into a simple academic PDF.
    Automatically names it after the source textbook.
    """
    title = os.path.splitext(os.path.basename(source_filename))[0].replace('_', ' ').title()
    output_filename = f"{os.path.splitext(source_filename)[0]}_notes.pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Title
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, f"Notes for {title}", 0, 1, "C")
    pdf.ln(10)

    # Body text
    pdf.set_font("Arial", "", 11)

    try:
        pdf.write_markdown(notes_markdown)
        pdf.output(output_filename)
        print(f"✅ PDF created: {output_filename}")
        return output_filename
    except Exception as e:
        print(f"⚠️ PDF creation error: {e}")
        fallback = f"{os.path.splitext(source_filename)[0]}_notes.md"
        with open(fallback, "w", encoding="utf-8") as f:
            f.write(f"# Notes for {title}\n\n{notes_markdown}")
        print(f"Saved fallback Markdown: {fallback}")
        return fallback

# %%
# -----------------------------
# MAIN PIPELINE
# -----------------------------

async def process_textbook(file, progress=gr.Progress()):
    """
    Extracts text, summarizes it, evaluates quality, and outputs PDF + download link.
    """
    if file is None:
        return "Please upload a textbook to begin.", None

    pdf_file_path = file.name
    reader = PdfReader(pdf_file_path)
    num_pages = len(reader.pages)

    # Step 1 — Extract
    progress(0, desc="Step 1/4: Extracting text...")
    full_text = ""
    for i, page in enumerate(reader.pages):
        progress((i + 1) / num_pages, desc=f"Extracting Page {i + 1}/{num_pages}")
        page_text = page.extract_text()
        if page_text:
            full_text += page_text + "\n"

    if not full_text.strip():
        return "⚠️ No text extracted from the PDF.", None

    print(f"✅ Extracted {len(full_text)} characters from {num_pages} pages.")

    # Step 2 — Chunk
    chunks = chunk_text(full_text)
    num_chunks = len(chunks)
    all_notes = []

    progress(0, desc="Step 2/4: Generating notes...")
    for i, chunk in enumerate(chunks):
        progress((i + 1) / num_chunks, desc=f"Generating Chunk {i + 1}/{num_chunks}")
        notes_chunk = await generate_notes(chunk)
        all_notes.append(notes_chunk)

    combined_notes = "\n\n---\n\n".join(all_notes)

    # Step 3 — PDF
    progress(1, desc="Step 3/4: Creating PDF...")
    pdf_output_path = create_pdf_file(combined_notes, pdf_file_path)

    # Step 4 — Return both preview + file
    if os.path.exists(pdf_output_path):
        message = f"✅ Notes generated successfully!\n\n**Saved as:** {os.path.basename(pdf_output_path)}"
        return message, pdf_output_path
    else:
        return "❌ PDF generation failed.", None

# %%
async def create_notes_interface(file, progress=gr.Progress(track_tqdm=True)):
    """Handles Gradio flow."""
    if file is not None:
        return await process_textbook(file, progress)
    return "Please upload a textbook.", None

# %%
# -----------------------------
# GRADIO INTERFACE
# -----------------------------
iface = gr.Interface(
    fn=create_notes_interface,
    inputs=gr.File(label="📘 Upload Textbook (PDF)"),
    outputs=[
        gr.Markdown(label="🧾 Status / Summary"),
        gr.File(label="📥 Download Generated Notes (.pdf)")
    ],
    title="AI Textbook → Notebook Notes Generator",
    description=(
        "Upload any textbook (PDF). The local LLaMA 3 (8B) model summarizes it into concise academic notes. "
        "Gemini evaluates quality, and the output is auto-saved as a clean PDF titled after the textbook."
    ),
    allow_flagging="never"
)

if __name__ == "__main__":
    iface.launch(server_name="127.0.0.1", share=False)
