# 🤖 AI CLI Chatbot

> **A lightning-fast, terminal-based AI assistant powered by Groq and Llama 3.1**
> Near‑instant inference • Persistent memory • Slash commands • Clean architecture

---

## 📖 Overview

**AI CLI Chatbot** is a modular Python application that brings the power of **Large Language Models (LLMs)** directly into your terminal. Unlike basic API wrappers, this project is designed as a *real application* — with persistent conversation state, a configurable AI persona, and integrated external tools.

It leverages **Groq’s LPU Inference Engine** to deliver ultra‑low latency responses, making the chat experience feel fluid, interactive, and surprisingly human.

This project was built using a **learning‑by‑building, AI‑assisted approach**, with a strong focus on architecture, clarity, and real‑world engineering practices.

---

## ✨ Key Features

⚡ **Blazing Fast Inference**
Powered by `llama-3.1-8b-instant` via the Groq API, delivering sub‑second response times.

🧠 **Context Awareness**
Maintains conversation history for coherent multi‑turn dialogue and follow‑up questions.

🛠️ **Integrated Slash Commands**

* `/weather <city>` — Fetch real‑time weather data using **wttr.in**
* `/clear` — Reset conversation memory and start fresh
* `/help` — Display available commands
* `/exit` — Gracefully close the application

🎨 **Typewriter Effect UI**
Simulates real‑time typing for a polished, immersive CLI experience.

🔐 **Secure Configuration**
Uses environment variables (`.env`) to protect API keys and sensitive data.

🧩 **Modular Architecture**
Clean separation of concerns (Config, Utils, Services) for maintainability and scalability.

---

## 📂 Project Structure

```text
📦 ai-cli-chatbot
 ┣ 📜 chatbot.py        # Main entry point (Controller & Event Loop)
 ┣ 📜 config.py         # Configuration, model IDs & system prompts
 ┣ 📜 weather.py        # Weather service integration
 ┣ 📜 utils.py          # UI/UX helpers (typewriter effect)
 ┣ 📜 requirements.txt  # Project dependencies
 ┗ 📜 .env.example      # Environment variable template
```

---

## 🚀 Getting Started

### Prerequisites

* Python **3.8+**
* A free-tier **[Groq API key](https://console.groq.com/keys)**

---

### Installation

#### 1️⃣ Clone the repository

```bash
git clone https://github.com/deepakrakshit/ai-cli-chatbot.git
cd ai-cli-chatbot
```

#### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

#### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 🔐 Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_gsk_key_here
```

> ⚠️ **Never commit your `.env` file to version control.**

---

## ▶️ Usage

Run the chatbot using:

```bash
python chatbot.py
```

Start chatting naturally, or use slash commands for additional functionality.

---

## 🎮 Command Guide

| Command    | Description                        | Example           |
| ---------- | ---------------------------------- | ----------------- |
| `/weather` | Fetches current weather for a city | `/weather London` |
| `/clear`   | Resets conversation context        | `/clear`          |
| `/help`    | Shows help menu                    | `/help`           |
| `/exit`    | Exits the application              | `/exit`           |

---

## ⚙️ Customization

### Change the AI Model

```python
# config.py
MODEL_NAME = "mixtral-8x7b-32768"  # Switch models easily
```

### Modify the AI Persona

Edit the `SYSTEM_PROMPT` in `config.py` to customize the bot’s behavior:

* Coding assistant
* Creative writer
* Study buddy
* Sarcastic chatbot 😄

---

## 🧠 Learning Outcomes

* Working with LLM APIs (Groq)
* Prompt engineering fundamentals
* Conversation memory management
* Modular Python project design
* External API integration
* CLI UX enhancement

---

## 🤝 Contributing

Contributions are welcome! 🚀

1. Fork the project
2. Create your feature branch

   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes

   ```bash
   git commit -m "Add AmazingFeature"
   ```
4. Push to the branch

   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request

---

## 👨‍💻 Author

**Deepak Rakshit**

* GitHub: [@deepakrakshit](https://github.com/deepakrakshit)

---

<p align="center">Made with ❤️, Python, and curiosity</p>
