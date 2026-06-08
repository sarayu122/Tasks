# ✦ Content Analyzer (AI Powered Streamlit App)

## 📌 Overview
This project is an **AI-powered Content Analysis Web App** built using **Streamlit, LangChain, and OpenAI-compatible LLMs (via OpenRouter)**.

It analyzes any given text (story, article, synopsis, or paragraph) and extracts structured insights such as:
- Summary (detailed + quick)
- Themes, emotions, and tone
- Characters and conflict
- Genre classification
- Key concepts and keywords

---

## 🚀 Features
- 🧠 AI-powered content understanding using LLMs
- 🎨 Beautiful modern UI with custom CSS styling
- 📊 Structured output with 20+ analysis fields
- 🏷️ Keyword & theme tag visualization
- ⚡ Fast inference using OpenRouter API
- 📦 Expandable raw response view
- 🧾 Clean card-based result layout

---

## 🧠 Tech Stack
- Python 🐍
- Streamlit 🎈
- LangChain 🦜
- OpenAI-compatible LLM (OpenRouter)
- HTML + CSS (custom UI design)

---

## ⚙️ How It Works

1. User pastes a paragraph into the input box  
2. Text is sent to a prompt template  
3. LLM analyzes and returns structured output  
4. Response is parsed into sections  
5. UI renders results as styled cards  

---

## 📂 Project Structure

project/
│── app.py # Main Streamlit application
│── .env # API keys (OPENROUTER_API_KEY)
│── requirements.txt # Dependencies

---


## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
OPENROUTER_API_KEY=your_api_key_here

📦 Installation
    1. Clone the repository
        git clone https://github.com/your-username/content-analyzer.git
        cd content-analyzer
    2. Install dependencies
        pip install -r requirements.txt
    3. Run the app
        streamlit run app.py


📊 Output Sections:

The app extracts structured insights including:

Title
Content Type
Genre & Sub-Genre
Setting & Time Period
Characters & Protagonist
Conflict & Objective
Themes & Emotions
Tone
Keywords
Detailed Summary
Quick Summary


🎯 Example Use Cases:

Book / Movie analysis
Story understanding
Article summarization
Content breakdown for study
NLP learning project
