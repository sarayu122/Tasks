# Tasks Workspace — Consolidated README

This repository contains several small Python projects and experiments grouped into folders. This single README provides an overview of each project, key files, and basic run instructions.

---

# Prerequisites

* Python 3.8+ installed

## Create Virtual Environment (Recommended)

```bash id="9w4wz7"
python -m venv .venv
```

### Windows PowerShell

```powershell id="bxjlwm"
.\.venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd id="mgtm26"
.\.venv\Scripts\activate.bat
```

### Unix / macOS

```bash id="ngtw7s"
source .venv/bin/activate
```

---

# Install Dependencies

Install dependencies per project when available.

Example:

```bash id="6vsm1o"
pip install -r chatbot-model/requirements.txt
```

For machine learning projects:

```bash id="sjygul"
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

# Projects

---

## chatbot-memory-model/

Memory-focused chatbot experiments.

### Files

* `chatbot-memory.py` — memory-capable chatbot
* `uichatbot_memory.py` — UI wrapper
* `requirements.txt`
* `pyproject.toml`

---

## chatbot-model/

Primary chatbot model experiments.

### Files

* `chatbot.py` — chatbot implementation
* `uichatbot.py` — UI/example runner
* `requirements.txt`
* `pyproject.toml`

---

## embedding-generation-model/

Embedding generation utilities.

### Files

* `embedding_generation.py` — generates embeddings from text
* `requirements.txt`
* `pyproject.toml`

---

## Evaluation-metrics/

Evaluation metric implementations.

### Files

* `evaluationmetrics.py` — evaluation metric helpers

---

## house_predict/

Housing dataset experiments.

### Files

* `housenumber.py` — housing price prediction example
* `AmesHousing.csv` — dataset used

---

## movie_review/

Movie review sentiment analysis experiments.

### Files

* `movie_review.py` — sentiment classification example
* `IMDB_dataset.csv` — dataset

---

## multi-layer-nndl/

Multi-layer neural network experiments.

### Files

* `2-layer.py` — two-layer neural network implementation

---

## single-layer-nndl/

Single-layer neural network experiments.

### Files

* `single_nndl.py` — single-layer neural network implementation

---

## prompt-based-model/

Prompt-engineering experiments.

### Files

* `prompt.py` — prompt-based model
* `promptui.py` — UI helper
* `requirements.txt`
* `pyproject.toml`

---

Iris_Classification/

Machine Learning classification project using the Iris Dataset and Scikit-learn.

Files
iris_loaddata.py — loads Iris dataset from CSV file and trains ML models
iris_sklearn.py — loads Iris dataset using Scikit-learn and trains ML models
loaddataset.csv — Iris dataset CSV
iris_dataset.csv — generated dataset CSV

---

# How to Run Scripts

Run scripts from the repository root.

Examples:

```bash id="h04yyn"
python chatbot-model/chatbot.py
python embedding-generation-model/embedding_generation.py
python house_predict/housenumber.py
python single-layer-nndl/single_nndl.py
python Iris_Classification/iris_loaddata.py
python Iris_Classification/iris_sklearn.py
```

---

# Notes & Tips

* Many folders include their own `README.md` and dependency files.
* Ensure CSV datasets are present before running scripts.
* Activate virtual environment before running projects.
* GUI wrappers may require additional setup depending on the project.

---

# Learning Areas Covered

This workspace includes projects related to:

* Machine Learning
* Neural Networks
* Natural Language Processing
* Embeddings
* Prompt Engineering
* Evaluation Metrics
* Sentiment Analysis
* Data Visualization
* Classification Algorithms
* Python UI Experiments

---

# Conclusion

This workspace serves as a collection of machine learning, NLP, neural network, and chatbot experiments for learning and practical implementation using Python and Scikit-learn.
