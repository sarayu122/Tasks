# 🧠 Single-Layer Feedforward Neural Network (NumPy)

## 📌 Overview
This project implements a **Single-Layer Feedforward Neural Network** using **NumPy**.  
It is the simplest neural network architecture with no hidden layers and performs a linear transformation followed by a sigmoid activation.

It is mathematically equivalent to **logistic regression** when used for binary classification.

---

## 🏗️ Model Architecture

Input (n features) → Linear Layer (W, b) → Sigmoid → Output


---

## 🚀 Features
- Pure NumPy implementation (no deep learning frameworks)
- Xavier weight initialization
- Sigmoid activation function with numerical stability
- Forward propagation only (no training loop)
- Model summary with parameter statistics

---

## ⚙️ Components
- **Weight Matrix (W):** Learns feature importance  
- **Bias (b):** Shifts activation  
- **Sigmoid Function:** Converts output to probability range (0–1)

---

## ▶️ How to Run
```bash
python your_script_name.py
