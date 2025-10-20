# 🤖 Simple AI Chatbot Web App

A lightweight and elegant **AI chatbot** web application built with **HTML, CSS, and JavaScript**, designed to let users ask any question and get instant AI-generated responses.  
This chatbot does **not retain memory** — every response is based only on the latest user query.

---

## ✨ Features

- **AI-powered responses** using the Google Gemini API (`gemini-2.0-flash` model)  
- **Interactive chat UI** with user and bot message bubbles  
- **Instant response display** with smooth scrolling  
- **Predefined suggestion buttons** to quickly start conversations  
- **Modern and minimal design** with soft gradients and responsive layout  
- **Stateless architecture** — no data or chat history is stored  

---

## 🛠 Tech Stack

| Component | Description |
|------------|-------------|
| **HTML5** | Structure of the chatbot interface |
| **CSS3** | Styling and responsive layout |
| **JavaScript (Vanilla)** | Handles chat logic, DOM manipulation, and API calls |
| **Google Gemini API** | Provides AI-generated responses |

---

## 📁 Project Structure

```
chatbot/
│
├── index.html       # Main HTML structure and layout
├── styles.css       # Styling for chatbot UI
├── script.js        # Chat logic, API connection, and user interaction
└── README.md        # Project documentation
```

---

## ⚙️ Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/simple-chatbot.git
cd simple-chatbot
```

### 2. Add Your API Key
Inside `script.js`, replace the placeholder with your own **Google Gemini API key**:
```js
const apiKey = "YOUR_API_KEY_HERE";
```

### 3. Run the Chatbot
You can open the app directly in a browser:
```
index.html
```

### 💻 Using VS Code
Right-click → **"Open with Live Server"**

---

## 💬 Example Interaction

**User:** What can I ask you to do?  
**Bot:** You can ask me to explain coding concepts, suggest project ideas, or help with academic tasks!

---

## 🧩 How It Works

➡️ The user types a message or clicks a suggestion button.  
➡️ The script sends the message and a predefined system prompt to the Gemini API.  
➡️ The API responds with a short, friendly message.  
➡️ The chatbot displays the response in the conversation window.

---

## 🖼️ UI Preview

*(Add a screenshot here if you want to showcase your chatbot UI)*  

Example:  
```
/assets/screenshot.png
```

---

## 🚧 Future Enhancements

- Add user authentication (Firebase / OAuth)  
- Implement chat memory or session context  
- Add dark mode  
- Enable voice input and output  
- Convert to a mobile PWA  

---

## ☁️ (Optional) Firebase Hosting Setup

If you’re hosting this project with **Firebase**:

1. Initialize Firebase in your project directory  
   ```bash
   firebase init hosting
   ```
2. Choose your Firebase project and set `public` as the folder containing `index.html`.
3. Deploy your chatbot:  
   ```bash
   firebase deploy
   ```
4. Firebase will provide a public URL to access your hosted chatbot.

---

## 👨‍💻 Author

**Kolla Upendra**  
Student developer passionate about building simple, user-friendly AI tools and educational apps.

📫 *Feel free to reach out or suggest improvements!*  
🔗 [GitHub Profile](https://github.com/K-upendra-7)

---

### ⭐ If you like this project, please consider giving it a star on GitHub!
