from tkinter import ON

from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df['target'] = iris.target

df['species'] = df['target'].map({
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'
})

csv_file_name = "iris_dataset.csv"

df.to_csv(csv_file_name, index=False)

loaded_df = pd.read_csv(csv_file_name)


loaded_df = loaded_df.drop_duplicates()

# print("Duplicate Rows:", loaded_df.duplicated().sum())

# print("\nFirst 5 Rows:\n")
# print(loaded_df.head())

# print("\nDataset Info:\n")
# print(loaded_df.info())

# print("\nStatistical Summary:\n")
# print(loaded_df.describe())

# plt.figure(figsize=(8,6))

# sns.heatmap(
#     loaded_df.corr(numeric_only=True),
#     annot=True,
#     cmap='coolwarm'
# )
# plt.title("Correlation Heatmap")
# plt.show()

# sns.pairplot(loaded_df, hue='species')
# plt.show()

X = loaded_df.drop(['target', 'species'], axis=1)
y = loaded_df['target']

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=1)

model1 = LogisticRegression(max_iter=100)
model1.fit(X_train, y_train)
y_pred = model1.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print("\n===== LOGISTIC REGRESSION =====")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")

cm1 = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n")
print(cm1)


model2 = DecisionTreeClassifier( random_state=1 ) 
model2.fit(X_train, y_train)
y_pred = model2.predict(X_test) 

accuracy = accuracy_score(y_test, y_pred) 
precision = precision_score( y_test, y_pred, average='weighted' ) 
recall = recall_score( y_test, y_pred, average='weighted' ) 
f1 = f1_score( y_test, y_pred, average='weighted' ) 

print("\n===== DECISION TREE =====") 
print(f"Accuracy : {accuracy:.4f}") 
print(f"Precision: {precision:.4f}") 
print(f"Recall : {recall:.4f}") 
print(f"F1 Score : {f1:.4f}")
cm2 = confusion_matrix(y_test, y_pred) 
print("\nConfusion Matrix:\n") 
print(cm2) 


model = RandomForestClassifier( n_estimators=100, random_state=1 ) 
model.fit(X_train, y_train) 
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred) 
precision = precision_score( y_test, y_pred, average='weighted' ) 
recall = recall_score( y_test, y_pred, average='weighted' ) 
f1 = f1_score( y_test, y_pred, average='weighted' ) 
print("\n===== RANDOM FOREST =====") 
print(f"Accuracy : {accuracy:.4f}") 
print(f"Precision: {precision:.4f}") 
print(f"Recall : {recall:.4f}") 
print(f"F1 Score : {f1:.4f}") 

cm3 = confusion_matrix(y_test, y_pred) 
print("\nConfusion Matrix:\n") 
print(cm3) 