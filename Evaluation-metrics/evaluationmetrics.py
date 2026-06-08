import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score


def confusion_matrix_binary(y_true, y_pred):
	y_true = np.asarray(y_true).astype(int)
	y_pred = np.asarray(y_pred).astype(int)

	tp = np.sum((y_true == 1) & (y_pred == 1))
	tn = np.sum((y_true == 0) & (y_pred == 0))
	fp = np.sum((y_true == 0) & (y_pred == 1))
	fn = np.sum((y_true == 1) & (y_pred == 0))

	return np.array([[tn, fp], [fn, tp]])


def accuracy_np(y_true, y_pred):
	y_true = np.asarray(y_true).astype(int)
	y_pred = np.asarray(y_pred).astype(int)
	return np.mean(y_true == y_pred)


def precision_np(y_true, y_pred):
	cm = confusion_matrix_binary(y_true, y_pred)
	tn, fp, fn, tp = cm[0, 0], cm[0, 1], cm[1, 0], cm[1, 1]
	denominator = tp + fp
	return 0.0 if denominator == 0 else tp / denominator


def recall_np(y_true, y_pred):
	cm = confusion_matrix_binary(y_true, y_pred)
	tn, fp, fn, tp = cm[0, 0], cm[0, 1], cm[1, 0], cm[1, 1]
	denominator = tp + fn
	return 0.0 if denominator == 0 else tp / denominator


def f1_np(y_true, y_pred):
	precision = precision_np(y_true, y_pred)
	recall = recall_np(y_true, y_pred)
	denominator = precision + recall
	return 0.0 if denominator == 0 else 2 * precision * recall / denominator


if __name__ == "__main__":
	y_true = np.array([1, 0, 1, 1, 0, 0, 1, 0, 1, 0])
	y_pred = np.array([1, 0, 0, 1, 0, 1, 1, 0, 1, 0])

	print("NumPy implementation")
	print("Confusion Matrix:\n", confusion_matrix_binary(y_true, y_pred))
	print("Accuracy:", round(accuracy_np(y_true, y_pred), 4))
	print("Precision:", round(precision_np(y_true, y_pred), 4))
	print("Recall:", round(recall_np(y_true, y_pred), 4))
	print("F1 Score:", round(f1_np(y_true, y_pred), 4))

	print("\nsklearn.metrics comparison")
	print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))
	print("Accuracy:", round(accuracy_score(y_true, y_pred), 4))
	print("Precision:", round(precision_score(y_true, y_pred, zero_division=0), 4))
	print("Recall:", round(recall_score(y_true, y_pred, zero_division=0), 4))
	print("F1 Score:", round(f1_score(y_true, y_pred, zero_division=0), 4))
