import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


reviews = pd.read_csv("Datasets/IMDB_dataset.csv")

print("Shape:", reviews.shape)
print("Columns:", reviews.columns.tolist())
print(reviews.head())

text_col = "review" if "review" in reviews.columns else reviews.columns[0]
target_col = "sentiment" if "sentiment" in reviews.columns else reviews.columns[1]

reviews = reviews[[text_col, target_col]].dropna()
reviews[target_col] = reviews[target_col].astype(str).str.lower().str.strip()

valid_labels = reviews[target_col].value_counts().index[:2]
reviews = reviews[reviews[target_col].isin(valid_labels)]

X = reviews[text_col]
y = reviews[target_col]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y,)

model = Pipeline(
	steps=[
		("tfidf", TfidfVectorizer(stop_words="english", max_features=20000)),
		("clf", LogisticRegression(max_iter=1000)),
	]
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nAccuracy:", round(accuracy_score(y_test, y_pred), 4))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

sample_reviews = [
	"This movie was amazing, the acting and story were great!",
	"Worst movie ever. Completely boring and a waste of time.",
]

sample_preds = model.predict(sample_reviews)
for text, pred in zip(sample_reviews, sample_preds):
	print(f"Review: {text}\nPredicted sentiment: {pred}\n")
