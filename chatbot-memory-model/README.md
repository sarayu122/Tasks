# 💀 SAVAGE AI

A brutally honest, witty, and unfiltered AI chatbot built with **Streamlit**, **LangChain**, and **OpenRouter GPT models**.

---

## 🔥 Features

- 💬 Chat-based AI interface using Streamlit
- 🤖 Powered by `ChatOpenAI` (OpenRouter API)
- 💀 Custom "Savage AI" personality (roasting, witty, no sugarcoating)
- 🎨 Dark neon UI with custom CSS styling
- 🧠 Conversation memory using Streamlit session state
- ⏎ Press Enter to send messages (no extra buttons needed)

---

## 🛠️ Tech Stack

- Python 3.9+
- Streamlit
- LangChain
- OpenAI-compatible API (OpenRouter)
- dotenv

---

## 📁 Project Structure

```
.
├── app.py              # Main Streamlit app (your code file)
├── .env                # API keys (not committed)
├── requirements.txt    # Dependencies
└── README.md           # This file
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/savage-ai.git
cd savage-ai
```

### 2. Create virtual environment (recommended)
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

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Get your API key from:
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

- User inputs a message using `st.chat_input`
- Message is stored in `st.session_state`
- LangChain `ChatOpenAI` model processes conversation history
- System prompt defines “SAVAGE AI” personality:
  - Brutal honesty
  - Dark humor
  - Short, punchy replies
- UI refreshes using `st.rerun()`

---

## 💀 System Prompt Personality

> You are SAVAGE AI — brutally honest, witty, and unfiltered.  
> You roast weak ideas with surgical precision.  
> Short, punchy replies. No sugarcoating. Ever.

---

## 🧩 Dependencies (requirements.txt)

```txt
streamlit
langchain
langchain-openai
python-dotenv
```

---

## ⚠️ Notes

- Requires valid OpenRouter API key
- Internet connection required
- Not suitable for sensitive or professional decision-making (it roasts everything 😄)

---

## 📜 License

MIT License — feel free to modify and build on top of it.

---

## 💀 Author

Built with chaos, sarcasm, and Python.
