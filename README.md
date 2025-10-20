# Agentic AI Training – Learning Journal

This repository is my personal record of learning from the **Agentic AI Training Program**.
The purpose of this repo is to track my journey, capture key concepts, and document practical experiments that I work on during and after each session.

By maintaining this log, I can reflect on my progress, revise concepts whenever needed, and build a solid foundation in **LLMs, GenAI, and Agentic AI**. 💡

---

## ℹ️ About the Training

- **📅 Kickoff Date:** 30th (August, 2025)
- **🎯 Core Focus Areas:**
  - Fundamentals of Large Language Models (LLMs)
  - Generative AI techniques and use-cases
  - Agentic AI – AI Agents, workflows, and tool integration
  - Applications in real-world industry settings
- **📚 Training Materials:** [Training Repository](https://github.com/TEJAPS/agentic-training)

---

## ✅ Prerequisites & Prep Checklist

This section will help me stay prepared before each session.
(Items will be updated as more details are shared during the program.)

- [ ] Install **Python 3.10+**
- [ ] Set up a **virtual environment** (e.g., `venv` or `conda`)
- [ ] Install **Jupyter Notebook / JupyterLab**
- [ ] Install **PyTorch / TensorFlow** (depending on training needs)
- [ ] Create a **GitHub account & repo** (this repository)
- [ ] Familiarize with **Git basics** (clone, commit, push)
- [ ] Review **fundamentals of AI/ML** (ML models, transformers, embeddings)
- [ ] Install any **libraries listed in the training materials**
- [ ] Optional: Explore basic **LLM APIs** (OpenAI, Hugging Face, etc.)

*(This checklist will be refined as new requirements are shared.)*

---

## 📔 Learning Journal

This section contains notes and reflections from each training session.
Every session entry will include the **date, topics covered, learnings, and my hands-on practice notes**.

## [Session 1: GitHub Integration, ML, and Full Stack]()
* **📅 Date:** 30th August 2025

### 📚Topics Covered:
* **Part 1: GitHub & Version Control** 
  * **Core Concepts:** A deep dive into essential Git commands and GitHub features including:
    * `push`, `pull`, and `pull request`
    * `branches` (local & remote)
    * Resolving `merge conflicts`
    * Managing `issues` for tracking tasks
  * **Practical Labs:** We completed three hands-on labs to solidify these concepts.
    * [Lab 1: Introduction to GitHub](https://github.com/skills/introduction-to-github)
    * [Lab 2: Reviewing Pull Requests](https://github.com/skills/review-pull-requests)
    * [Lab 3: Resolving Merge Conflicts](https://github.com/skills/resolve-merge-conflicts)
  * **Collaboration:** Discussed strategies for effective teamwork on a shared codebase using GitHub.

* **Part 2: Machine Learning & API Integration** 
  * **ML Fundamentals:** An overview of the machine learning lifecycle was provided.
    * Topics included data segregation (training/testing), prediction, algorithms, model creation, and model tuning.
    * A brief introduction to neural networks was also covered.
  * **Model Deployment:** Learned about storing trained ML models as `.pkl` files and using them in full-stack applications.
  * **APIs in Action:** A live demonstration using Chrome DevTools showed how to inspect API requests and responses, including methods, headers, and payloads.

## [Session 2: Cloud Platforms, APIs, and n8n Automation]()
* **📅 Date:** *10th September 2025*

### Topics Covered:
The session focused on the practical aspects of cloud platforms, API integrations, and workflow automation using n8n. The following key concepts were introduced:
* API Keys & OAuth
* Authentication vs. Authorization
* Cloud Platforms & Third-Party Integrations
* Docker for containerized workflows

### Practical Work:
* **Google Cloud Integration:** 
  * Successfully created a new project on Google Cloud.
  * Enabled the Email API.
  * Connected the Gmail API to an n8n workflow.

* **Telegram Bot Integration:** 
  * Created a new Telegram bot and generated the necessary API keys.
  * Integrated the Telegram APIs with an n8n workflow.

* **Troubleshooting & Testing:** 
  * Individually tested each node within the n8n workflows to ensure full functionality.
  * Collaboratively resolved Docker-related challenges and other integration issues that arose during setup.

## [Session 3: Agentic AI, Transformers, and Advanced n8n Workflows]()
* **📅 Date:** *10th September 2025*
 
### 📚 Topics Covered:
This session advanced both practical integration skills and the theoretical understanding of AI concepts.

* **T-Shaped Developer & Agentic AI:** 
  * Introduced the T-shaped developer model, which encourages broad general knowledge with a deep specialization in Agentic AI.
  * Studied core Agentic AI concepts including frameworks, hallucination management, and vectorization.
  * Mapped student skills against the growth path toward becoming an Agentic AI developer.

* **Transformer Architecture Concepts:** 
  * **Tokenization:** Converting text into machine-readable tokens.
  * **Embedding:** Mapping the tokens into a numerical vector space.
  * **Attention Mechanism:** Assigning weight to tokens that are most relevant in a given context.
  * **Transformer Layers:** Using multiple stacked blocks to process the embeddings.
  * **Unembedding:** Converting the final processed vectors back into output text.

### Practical Work:
The hands-on portion of the session involved building and deploying a real-time AI workflow.

  * An n8n workflow was created to integrate Gmail, the Gemini AI Chat Model, and Telegram.
  * Explored the essential components that AI agents rely on: input, chat models, memory, and tools.
  * Conducted node-by-node testing to validate the functionality of the entire workflow.
  * The workflow was deployed live and tested in real-time scenarios.


## [Session 4 & 5 – End-to-End Personalized LLM Pipeline]()
**📅 Date:** *11th October 2025*

### Topics Covered:
  *  Recap of n8n and introduction to Agentic AI workflow complexities.
  * Used Cursor IDE and UV package manager for environment setup.
  * Built workflows without frameworks using the OpenAI SDK.
  * Discussed five Agentic AI workflow design patterns:
    1. Prompt Chaining
    2. Routing
    3. Parallelization
    4. Orchestrator–Worker
    5. Evaluator–Optimizer
  * Created personalized LLMs using LinkedIn profiles and personal summaries.
  * Integrated multiple LLMs (OpenAI, Gemini, Anthropic, Groq, DeepSeek, Ollama).
  * Added tools for logging unknown queries and sending real-time notifications with Pushover.

### My Learnings: 
  * Understood how to personalize models using real user data.
  * Learned to integrate and switch between multiple LLM providers.
  * Learned to build and optimize workflows with Evaluator–Optimizer patterns.
  * Developed a complete personalized LLM pipeline with notifications and resource integration.

### Practice Work: 
  * Built workflows using OpenAI SDK.
  * Implemented Evaluator–Optimizer patterns.
  * Integrated personalized chatbot using Gradio.
  * Complete all four lab exercises.
  * Design a personalized LLM use case with one tool and one resource.
  * Demonstrate a real-world implementation using the personalized model.


## [Session 6 & 7 – Agentic Frameworks, LangChain, and OpenAI Agents]()
**📅 Date:** *18th October 2025* (Online Session)

### Topics Covered:
* Recap: Using OpenAI SDK core (without framework).
* **Morning Session:**
  * Implemented Agentic workflows using **OpenAI Agents SDK**.
  * Learned **asyncio** operations and tracing in OpenAI.
  * Practical work on **Agents, Handoffs, and Guardrails**.
  * Tools used: SendGrid (Email), Google WebSearchTool.
  * Built a Sales Manager setup with handoffs.

* **Afternoon Session:**
  * Used **LangChain** and **LangGraph** to implement agentic workflows.
  * Learned concepts of nodes, edges, state, reducers, and immutability.
  * Integrated with **LangSmith**, **Serper.dev**, **SendGrid**, and **Pushover**.
  * Implemented persistent and in-memory storage using SQLite.
  * Used decorators: `@function_tool`, `@input_guardrails`, etc.

### My Learnings: 
  * Implemented memory and tracing mechanisms in agentic systems.
  * Gained hands-on experience with OpenAI Agents SDK and LangChain ecosystem.
  * Built a complete, traceable agentic workflow with notifications and handoffs.
  * Understood when and why to use different frameworks (SDK, LangChain, LangGraph).

### Practice Work: 
  * Completed lab exercises.
  * Uploaded documentation, flow diagrams, and code to GitHub.
  * Demonstrate a real-world implementation using the personalized model.
  * Improve  personalized LLM use case with one tool and one resource from last session with all new concepts.