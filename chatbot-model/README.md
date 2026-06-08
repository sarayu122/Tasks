# 😤 RudeBot

A sarcastic, minimal, and "rude-style" AI chatbot built with **Streamlit**, **LangChain**, and **OpenRouter GPT models**.

---

## ⚡ Features

- 💬 Clean chat UI using Streamlit
- 🤖 Powered by `ChatOpenAI` (OpenRouter API)
- 😤 "Rude assistant" personality system prompt
- 🎨 Custom dark brutal UI with CSS styling
- 🧠 Conversation memory using Streamlit session state
- ⚡ Cached model initialization for better performance
- ⏎ Chat input with instant response

---

## 🛠 Tech Stack

- Python 3.9+
- Streamlit
- LangChain
- OpenAI-compatible API (OpenRouter)
- python-dotenv

---

## 📁 Project Structure

```
.
├── app.py              # Main Streamlit chatbot file
├── .env                # API key storage
├── requirements.txt    # Dependencies
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/rudebot.git
cd rudebot
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate    # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Get API key from:
👉 https://openrouter.ai/

---

## 🚀 Run the App

```bash
streamlit run app.py
```

Then open:
```
http://localhost:8501
```

---

## 🧠 How It Works

- User sends a message via `st.chat_input`
- Message stored in `st.session_state`
- LangChain `ChatOpenAI` model processes full chat history
- System prompt defines assistant behavior:
  - "You are a rude assistant"
- Response is rendered using custom styled HTML bubbles

---

## ⚠️ Notes

- Requires internet + valid OpenRouter API key
- Designed for fun / experimentation (not professional use)
- Cached model improves performance (`@st.cache_resource`)

---

## 📦 Requirements

```txt
streamlit
langchain
langchain-openai
python-dotenv
```

---

## 👨‍💻 Author

Built with attitude 😤 and Python.
