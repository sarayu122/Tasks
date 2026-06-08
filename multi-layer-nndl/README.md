# 🧠 2-Layer Neural Network using PyTorch

## 📌 Overview
This project implements a simple **2-layer neural network** using **PyTorch** for binary classification on a synthetic structured dataset.

The goal is to demonstrate the complete ML workflow: data generation, model building, training, and evaluation.

---

## 🚀 Features
- Synthetic dataset generation using PyTorch
- Fully connected neural network (2-layer architecture)
- ReLU activation + Sigmoid output layer
- Binary classification (0/1)
- Training using Adam optimizer
- Accuracy evaluation on training data

---

## 🏗️ Model Architecture
- Input layer: 4 features  
- Hidden layer: 8 neurons + ReLU  
- Output layer: 1 neuron + Sigmoid  

---

## ⚙️ Training Details
- Loss Function: Binary Cross Entropy (BCELoss)
- Optimizer: Adam
- Learning Rate: 0.01
- Epochs: 100

---

## 📊 Output
- Training loss printed every 10 epochs
- Final model accuracy displayed after training

---

## ▶️ How to Run
```bash
pip install torch
python your_script_name.py

Learning Outcomes:
    Understanding basic neural network structure
    Forward and backward propagation in PyTorch
    Binary classification workflow
    Model training and evaluation pipeline

Tech Stack:
Python 🐍, PyTorch 🔥