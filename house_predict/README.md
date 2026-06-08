# 🏡 Ames Housing Price Prediction (Linear Regression Pipeline)

## 📌 Overview
This project builds a **machine learning pipeline** to predict house prices using the **Ames Housing dataset**.  
It uses **data preprocessing, feature engineering, and Linear Regression** inside a clean `scikit-learn` Pipeline.

The goal is to predict **log-transformed house prices** and evaluate model performance using regression metrics.

---

## 🚀 Features
- Handles missing values using `SimpleImputer`
- Log transformation of skewed numerical features
- One-hot encoding for categorical variables
- Clean preprocessing using `ColumnTransformer`
- End-to-end ML pipeline with `LinearRegression`
- Model evaluation using MAE, RMSE, and R²
- Sample prediction comparison (actual vs predicted)

---

## 📊 Dataset
- Dataset used: **Ames Housing Dataset**
- File path: `Datasets/AmesHousing.csv`

### Target Variable:
- `SalePrice` (log-transformed using `np.log1p`)

---

## ⚙️ Data Preprocessing Steps

### 1. Handling Missing Values
- `Lot Frontage` → filled with median
- Numerical features → median imputation
- Categorical features → most frequent imputation

### 2. Feature Dropping
Removed irrelevant or high-missing columns: Street, Alley, Utilities, Pool QC, Order, PID

### 3. Feature Transformation
Log transformation applied to reduce skewness:
- SalePrice
- Misc Val
- Lot Area
- Low Qual Fin SF
- 3Ssn Porch

---

## 🧠 Model Pipeline

The project uses a **Scikit-learn Pipeline**:

### Preprocessing:
- Numeric features → Median Imputation
- Categorical features → OneHotEncoding

### Model:
- Linear Regression

---

## 📈 Evaluation Metrics

### Mean Absolute Error (MAE)
Average absolute difference between actual and predicted values.

### Root Mean Squared Error (RMSE)
Penalizes large errors more heavily.

### R² Score
Measures how well the model explains variance.

---

## 🏗️ Workflow

Load Dataset
↓
Data Cleaning & Feature Engineering
↓
Train-Test Split
↓
Preprocessing Pipeline (Num + Cat)
↓
Linear Regression Model
↓
Training
↓
Prediction
↓
Evaluation

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install pandas numpy scikit-learn

2. Run the script
python your_script_name.py

Sample Output:
(1460, 79) (365, 79) (1460,) (365,)
MAE: 0.11
RMSE: 0.17
R2: 0.89


Sample Predictions (Inverse Log Scale):
Actual Price	Predicted Price
215000	        210450
181000	        175320
223500	        230120
140000	        135800
250000	        260300


🎯 Key Learnings
Building end-to-end ML pipelines in sklearn
Importance of preprocessing in real-world datasets
Handling categorical + numerical features together
Effect of log transformation on skewed data
Regression model evaluation techniques


🛠 Tech Stack
Python 🐍
Pandas 📊
NumPy 🔢
Scikit-learn 🤖