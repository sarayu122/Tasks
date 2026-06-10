# ✦ AI Powered NLP Applications Suite

A collection of AI-powered Streamlit applications built using **LangChain**, **Pydantic**, and **OpenAI-compatible LLMs via OpenRouter**.

This repository currently contains:

1. **Content Analyzer** → Advanced AI content understanding & summarization
2. **Data Extraction Agent** → Structured information extraction from customer messages

---

# 🧠 Tech Stack

* Python 🐍
* Streamlit 🎈
* LangChain 🦜
* Pydantic
* OpenRouter API
* OpenAI-compatible LLMs
* HTML + CSS (Custom UI)

---

# 📂 Project Structure

```bash id="n92kqa"
project/
│── content_analyzer.py        # Content Analyzer app
│── data_extraction_agent.py   # Data Extraction app
│── .env                       # API keys
│── requirements.txt           # Dependencies
│── README.md                  # Documentation
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory:

```env id="f4qvwb"
OPENROUTER_API_KEY=your_api_key_here
```

---

# 📦 Installation

## 1️⃣ Clone the Repository

```bash id="7w0x7e"
git clone https://github.com/your-username/ai-nlp-suite.git

cd ai-nlp-suite
```

---

## 2️⃣ Install Dependencies

```bash id="8ow8a2"
pip install -r requirements.txt
```

---

# 🚀 Run Applications

## ▶️ Run Content Analyzer

```bash id="7fc3mo"
streamlit run content_analyzer.py
```

---

## ▶️ Run Data Extraction Agent

```bash id="z3z1cg"
streamlit run data_extraction_agent.py
```

---

# ✦ Project 1 — Content Analyzer

## 📌 Overview

The **Content Analyzer** is an AI-powered text analysis application that understands and extracts insights from stories, articles, paragraphs, or summaries.

It generates structured analysis including:

* Detailed Summary
* Quick Summary
* Themes & Emotions
* Genre Detection
* Tone Analysis
* Character Identification
* Conflict Detection
* Keywords & Concepts

---

## 🚀 Features

* 🧠 AI-powered content understanding
* 📊 Structured multi-section analysis
* 🎨 Modern UI with custom styling
* 🏷️ Theme & keyword visualization
* ⚡ Fast inference with OpenRouter
* 📦 Expandable raw response view

---

## 📊 Output Includes

* Title
* Content Type
* Genre & Subgenre
* Setting
* Main Characters
* Protagonist
* Conflict
* Themes
* Emotions
* Tone
* Keywords
* Detailed Summary
* Quick Summary

---

## 🎯 Use Cases

* Story understanding
* Article summarization
* NLP learning projects
* Book & movie analysis
* Content research

---

# ✦ Project 2 — Data Extraction Agent

## 📌 Overview

The **Data Extraction Agent** extracts structured customer support information from unstructured customer messages using LLMs.

The system automatically identifies:

* Customer Name
* Email Address
* Order ID
* Issue Type

---

## 🚀 Features

* 🧠 AI-powered information extraction
* 📩 Structured support ticket parsing
* 🧾 Pydantic schema validation
* 🎨 Dark-themed modern UI
* 📊 JSON-style structured output
* 🔍 Handles messy customer messages

---

## 📊 Example Extraction

### Input

```text id="jhyz1d"
Hi team,

My name is Rahul Sharma.
My payment failed while placing an order.

Order ID: ORD-45678
Email: rahul.sharma@gmail.com
```

### Output

```json id="9k2t0n"
{
  "name": "Rahul Sharma",
  "email": "rahul.sharma@gmail.com",
  "order_id": "ORD-45678",
  "issue_type": "Payment Failed"
}
```

---

## 🎯 Use Cases

* Helpdesk automation
* CRM preprocessing
* Customer support systems
* Structured NLP pipelines
* Information extraction projects

---

# 🔒 Validation

The project uses **Pydantic** to ensure:

* Structured outputs
* Proper email formatting
* Reliable AI-generated responses

---

# 🎨 UI Highlights

* Responsive Streamlit layouts
* Minimal modern design
* Card-based output rendering
* Custom CSS styling
* Smooth interaction flow

---

# 📌 Future Improvements

* 📎 PDF & document upload support
* 🌐 Multi-language support
* 📂 Export to CSV/JSON
* 🔄 Streaming AI responses
* 🧠 Improved classification models
* ☁️ Deployment support

---