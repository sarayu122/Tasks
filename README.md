# ✦ Tasks Workspace — AI, ML & NLP Projects Collection

This repository contains multiple Python projects, experiments, and mini applications focused on:

* Artificial Intelligence
* Machine Learning
* Natural Language Processing
* Neural Networks
* Prompt Engineering
* Chatbots
* Data Analysis

The workspace is designed for learning, experimentation, and practical implementation using Python and modern AI frameworks.

---

# 🧠 Technologies Used

* Python 🐍
* Streamlit 🎈
* LangChain 🦜
* Scikit-learn
* OpenRouter API
* Pydantic
* NumPy
* Pandas
* Matplotlib

---

# 📂 Repository Structure

```bash id="2zhfce"
Tasks-Workspace/
│
├── chatbot-memory-model/
├── chatbot-model/
├── embedding-generation-model/
├── Evaluation-metrics/
├── house_predict/
├── movie_review/
├── multi-layer-nndl/
├── single-layer-nndl/
├── prompt-based-model/
├── Iris_Classification/
├── content-analyzer/
├── data-extraction-agent/
│
└── README.md
```

---

# ⚙️ Prerequisites

* Python 3.8 or higher
* pip package manager

---

# 🔧 Create Virtual Environment (Recommended)

## Windows PowerShell

```powershell id="iy2pxd"
python -m venv .venv

.\.venv\Scripts\Activate.ps1
```

---

## Windows CMD

```cmd id="j4g3i0"
python -m venv .venv

.\.venv\Scripts\activate.bat
```

---

## Linux / macOS

```bash id="uuxh9s"
python -m venv .venv

source .venv/bin/activate
```

---

# 📦 Install Dependencies

Install dependencies individually for each project when `requirements.txt` is available.

Example:

```bash id="v49m36"
pip install -r chatbot-model/requirements.txt
```

For ML-based projects:

```bash id="9v7dl3"
pip install pandas numpy matplotlib scikit-learn
```

---

# 🚀 Projects Overview

---

# 🤖 Chatbot Projects

## chatbot-model/

Basic chatbot implementation and UI experiments.

### Main Files

* `chatbot.py`
* `uichatbot.py`

---

## chatbot-memory-model/

Memory-enabled chatbot experiments using conversational memory.

### Main Files

* `chatbot-memory.py`
* `uichatbot_memory.py`

---

# 🧠 NLP & AI Projects

## prompt-based-model/

Prompt engineering experiments using LLMs.

### Main Files

* `prompt.py`
* `promptui.py`

---

## embedding-generation-model/

Text embedding generation utilities.

### Main Files

* `embedding_generation.py`

---

## content-analyzer/

AI-powered Streamlit application for analyzing stories, articles, and paragraphs.

### Features

* Summary generation
* Theme extraction
* Emotion & tone detection
* Genre classification
* Keyword extraction

### Technologies

* Streamlit
* LangChain
* OpenRouter API

---

## data-extraction-agent/

AI-powered structured data extraction app for customer support messages.

### Extracted Fields

* Customer Name
* Email Address
* Order ID
* Issue Type

### Technologies

* Streamlit
* LangChain
* Pydantic
* OpenRouter API

---

# 📊 Machine Learning Projects

## Iris_Classification/

Classification experiments using the Iris dataset.

### Main Files

* `iris_loaddata.py`
* `iris_sklearn.py`

---

## house_predict/

Housing price prediction experiments.

### Main Files

* `housenumber.py`

Dataset included:

* `AmesHousing.csv`

---

## movie_review/

Movie review sentiment analysis project.

### Main Files

* `movie_review.py`

Dataset included:

* `IMDB_dataset.csv`

---

# 🧮 Neural Network Projects

## single-layer-nndl/

Single-layer neural network implementation.

### Main Files

* `single_nndl.py`

---

## multi-layer-nndl/

Multi-layer neural network implementation.

### Main Files

* `2-layer.py`

---

# 📏 Evaluation Metrics

## Evaluation-metrics/

Utility functions and experiments for evaluation metrics.

### Main Files

* `evaluationmetrics.py`

---

# ▶️ Running Projects

Run scripts from the repository root.

Examples:

```bash id="hh36gl"
python chatbot-model/chatbot.py

python embedding-generation-model/embedding_generation.py

python house_predict/housenumber.py

python Iris_Classification/iris_sklearn.py
```

---

# ▶️ Running Streamlit Applications

## Content Analyzer

```bash id="88bjlwm"
streamlit run content-analyzer/app.py
```

---

## Data Extraction Agent

```bash id="2wdpsn"
streamlit run data-extraction-agent/app.py
```

---

# 📚 Learning Areas Covered

This workspace includes practical projects related to:

* Machine Learning
* Neural Networks
* NLP
* Chatbots
* Prompt Engineering
* Sentiment Analysis
* Embeddings
* Evaluation Metrics
* Data Visualization
* Classification Algorithms
* Streamlit UI Development

---

# 📌 Notes

* Some projects include their own dependency files.
* Ensure datasets are available before running scripts.
* Activate the virtual environment before execution.
* API-based projects require environment variables.

---

# 🔑 Environment Variables

Create a `.env` file where required:

```env id="4cwz4t"
OPENROUTER_API_KEY=your_api_key_here
```

---

# 👨‍💻 Purpose of This Repository

This repository serves as a personal learning and experimentation workspace for:

* AI & Machine Learning concepts
* NLP applications
* LLM integrations
* Neural network implementation
* Streamlit application development

---