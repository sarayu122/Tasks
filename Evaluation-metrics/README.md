# Binary Classification Metrics from Scratch (NumPy Implementation)

## 📌 Overview
This project implements common **binary classification evaluation metrics** from scratch using **NumPy**, and compares them with implementations from `scikit-learn`.

It helps in understanding how metrics like **Confusion Matrix, Accuracy, Precision, Recall, and F1-score** are computed internally without relying on ML libraries.

---

## 🚀 Features
- Custom Confusion Matrix implementation using NumPy
- Accuracy calculation without sklearn
- Precision, Recall, and F1-score from scratch
- Comparison with `sklearn.metrics`
- Handles edge cases like division by zero
- Simple and beginner-friendly implementation

---

## 📊 Metrics Implemented

### 1. Confusion Matrix
Returns:
    [[TN, FP],
    [FN, TP]]

### 2. Accuracy
Proportion of correctly predicted labels:

Accuracy = (TP + TN) / Total Samples

### 3. Precision
How many predicted positives are actually correct:

Precision = TP / (TP + FP)

### 4. Recall
How many actual positives are correctly identified:

Recall = TP / (TP + FN)

### 5. F1 Score
Harmonic mean of Precision and Recall:

F1 = 2 * (Precision * Recall) / (Precision + Recall)



## 🧠 How It Works
- Inputs are converted into NumPy arrays
- Confusion matrix is computed manually using logical conditions
- Metrics are derived from TP, TN, FP, FN
- Results are compared with `sklearn.metrics` for validation



## ▶️ How to Run

### 1. Install dependencies
```bash
pip install numpy scikit-learn
2. Run the script
python metrics.py

📌 Example Output
NumPy implementation
Confusion Matrix:
 [[4 1]
 [1 4]]
Accuracy: 0.8
Precision: 0.8
Recall: 0.8
F1 Score: 0.8

sklearn.metrics comparison
Confusion Matrix:
 [[4 1]
 [1 4]]
Accuracy: 0.8
Precision: 0.8
Recall: 0.8
F1 Score: 0.8


After completing this project, you will understand:

How classification metrics are calculated internally
Why confusion matrix is the foundation of evaluation metrics
How sklearn abstracts these computations
Core evaluation logic used in ML models


🛠 Tech Stack:

Python 🐍
NumPy 🔢
scikit-learn 🤖