# Iris Classification using Scikit-Learn

## Overview

This project demonstrates multiclass classification using the Iris Dataset with Scikit-learn.

The project includes:

* Dataset loading
* Data preprocessing
* Duplicate removal
* Data visualization
* Correlation analysis
* Model training
* Model evaluation

Three machine learning models are implemented:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

---

# Project Structure

```text id="9f9sgy"
Iris_Classification/
│
├── iris_loaddata.py
├── iris_sklearn.py
├── loaddataset.csv
├── iris_dataset.csv
└── README.md
```

---

# Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

---

# Installation

Install required libraries:

```bash id="xktc5m"
pip install pandas matplotlib seaborn scikit-learn
```

---

# Dataset Information

The Iris dataset contains 150 flower samples.

Features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

Classes:

* Iris-setosa
* Iris-versicolor
* Iris-virginica

---

# File Descriptions

---

# 1. iris_sklearn.py

This file:

* Loads the Iris dataset using Scikit-learn
* Converts the dataset into a Pandas DataFrame
* Creates:

  * target column
  * species column
* Saves dataset as CSV
* Removes duplicate rows
* Splits dataset into train and test sets
* Trains:

  * Logistic Regression
  * Decision Tree
  * Random Forest
* Evaluates models using:

  * Accuracy
  * Precision
  * Recall
  * F1 Score
  * Confusion Matrix

---

## Features Used

```python id="4ib2x8"
X = loaded_df.drop(['target', 'species'], axis=1)
```

## Target Used

```python id="6i0h6z"
y = loaded_df['target']
```

---

# 2. iris_loaddata.py

This file:

* Loads dataset directly from CSV file
* Removes duplicate rows
* Performs preprocessing
* Splits dataset into training and testing data
* Trains:

  * Logistic Regression
  * Decision Tree
  * Random Forest
* Evaluates model performance

---

## Features Used

```python id="p8w73y"
X = df.drop(['Id', 'Species'], axis=1)
```

## Target Used

```python id="6a2hjz"
y = df['Species']
```

---

# Data Visualization

The project supports:

## Correlation Heatmap

Used to analyze relationships between features.

```python id="rkl2mh"
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap='coolwarm'
)
```

## Pairplot

Used to visualize:

* class separation
* feature relationships
* feature distributions

```python id="h1zbll"
sns.pairplot(df, hue='species')
```

---

# Machine Learning Models

## Logistic Regression

A linear classification algorithm suitable for multiclass problems.

## Decision Tree Classifier

A tree-based algorithm that learns decision rules from features.

## Random Forest Classifier

An ensemble model that combines multiple decision trees for improved performance.

---

# Evaluation Metrics

The project evaluates models using:

## Accuracy

Measures overall correct predictions.

## Precision

Measures how many predicted classes are correct.

## Recall

Measures how many actual classes are correctly identified.

## F1 Score

Harmonic mean of Precision and Recall.

## Confusion Matrix

Shows correct and incorrect predictions for each class.

---

# Weighted Average

The project uses:

```python id="gbmqcc"
average='weighted'
```

for:

* Precision
* Recall
* F1 Score

This means:

* classes with more samples influence the final metric more.

---

# Random State Observation

Initially, the models produced nearly 100% accuracy because:

* The Iris dataset is very clean
* Classes are highly separable
* Petal features strongly distinguish flower species

After changing:

```python id="pbm0h1"
random_state=1
```

the train-test split changed, resulting in slightly different performance.

This demonstrates that:

* model accuracy depends on train-test splitting
* different random states can produce different results

---

# Observed Results

## iris_loaddata.py Results

### Logistic Regression

```text id="91n8jm"
Accuracy : 0.9667
Precision: 0.9714
Recall   : 0.9667
F1 Score : 0.9673
```

### Confusion Matrix

```text id="6skhwp"
[[11  0  0]
 [ 0 12  1]
 [ 0  0  6]]
```

---

### Decision Tree

```text id="w08sqf"
Accuracy : 0.9667
Precision: 0.9714
Recall   : 0.9667
F1 Score : 0.9673
```

### Confusion Matrix

```text id="0e9xg8"
[[11  0  0]
 [ 0 12  1]
 [ 0  0  6]]
```

---

### Random Forest

```text id="9e3evn"
Accuracy : 0.9667
Precision: 0.9714
Recall   : 0.9667
F1 Score : 0.9673
```

### Confusion Matrix

```text id="fvw7oq"
[[11  0  0]
 [ 0 12  1]
 [ 0  0  6]]
```

---

## iris_sklearn.py Results

### Logistic Regression

```text id="jnnv2q"
Accuracy : 0.9333
Precision: 0.9333
Recall   : 0.9333
F1 Score : 0.9333
```

### Confusion Matrix

```text id="mbxvgg"
[[10  0  0]
 [ 0 12  1]
 [ 0  1  6]]
```

---

### Decision Tree

```text id="v8xofc"
Accuracy : 0.9333
Precision: 0.9333
Recall   : 0.9333
F1 Score : 0.9333
```

### Confusion Matrix

```text id="7vx4y0"
[[10  0  0]
 [ 0 12  1]
 [ 0  1  6]]
```

---

### Random Forest

```text id="lb8gve"
Accuracy : 0.9333
Precision: 0.9333
Recall   : 0.9333
F1 Score : 0.9333
```

### Confusion Matrix

```text id="10d30p"
[[10  0  0]
 [ 0 12  1]
 [ 0  1  6]]
```

---

# Learning Outcomes

By completing this project, you will understand:

* Dataset preprocessing
* Duplicate handling
* Correlation analysis
* Feature selection
* Data visualization
* Train-test splitting
* Classification algorithms
* Model evaluation metrics
* Effect of random_state on results

---

# Conclusion

The Iris dataset is simple and highly separable, allowing machine learning models to achieve very high accuracy.

Changing the train-test split using different random states slightly changes model performance, demonstrating the importance of dataset splitting in machine learning evaluation.
