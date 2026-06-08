# 🎬 IMDB Sentiment Analysis using Machine Learning

## 📌 Overview
This project performs **sentiment analysis on movie reviews** using a Machine Learning pipeline.  
It classifies reviews as **positive or negative** using **TF-IDF features + Logistic Regression**.

The model is built using **Scikit-learn Pipeline**, making the workflow clean and production-ready.

---

## 🚀 Features
- Loads and processes IMDB review dataset
- Automatically detects text and label columns
- Cleans and standardizes sentiment labels
- Uses **TF-IDF Vectorization** for text feature extraction
- Trains **Logistic Regression classifier**
- Evaluates model using accuracy, confusion matrix, and classification report
- Predicts sentiment for custom sample reviews

---

## 📊 Dataset
- Dataset: IMDB Movie Reviews Dataset
- File path: `Datasets/IMDB_dataset.csv`

### Expected Columns:
- Text column → `review` (or first column if unnamed)
- Target column → `sentiment` (or second column)

---

## ⚙️ Data Preprocessing
- Removed missing values
- Standardized sentiment labels (lowercase + strip)
- Filtered dataset to keep only valid binary labels
- Used stratified train-test split for balanced classes

---

## 🧠 Model Pipeline

The model is built using a Scikit-learn Pipeline:


### 1. Text Feature Extraction

TfidfVectorizer(stop_words="english", max_features=20000)

### 2. Classifier

LogisticRegression(max_iter=1000)

## 📈 Evaluation Metrics

### Accuracy
Measures overall correctness of predictions.

### Classification Report
Includes:
- Precision
- Recall
- F1-score

### Confusion Matrix
Shows:
- True Positives
- True Negatives
- False Positives
- False Negatives

---

## 🏗️ Workflow

Load Dataset
↓
Data Cleaning & Label Processing
↓
Train-Test Split (Stratified)
↓
TF-IDF Vectorization
↓
Logistic Regression Training
↓
Prediction
↓
Evaluation

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install pandas scikit-learn

2. Run the script
python your_script_name.py

📊 Sample Output
Accuracy: 0.89

Classification Report:
               precision    recall  f1-score   support
    negative       0.88      0.90      0.89      2500
    positive       0.90      0.88      0.89      2500

Confusion Matrix:
[[2250  250]
 [ 300 2200]]


Sample Predictions:
Review: This movie was amazing, the acting and story were great!
Predicted sentiment: positive

Review: Worst movie ever. Completely boring and a waste of time.
Predicted sentiment: negative


Key Learnings:
    Text preprocessing for NLP tasks
    TF-IDF feature representation
    Logistic Regression for classification
    Building ML pipelines in Scikit-learn
    Evaluating classification models

Tech Stack:
Python 🐍
Pandas 📊
Scikit-learn 🤖