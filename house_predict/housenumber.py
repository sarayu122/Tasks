import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("Datasets/AmesHousing.csv")

df["Lot Frontage"] = df["Lot Frontage"].fillna(df["Lot Frontage"].median())

df.drop(["Street", "Alley", "Utilities", "Pool QC", "Order", "PID"], axis=1, inplace=True)

df["SalePrice"] = np.log1p(df["SalePrice"])
df["Misc Val"] = np.log1p(df["Misc Val"])
df["Lot Area"] = np.log1p(df["Lot Area"])
df["Low Qual Fin SF"] = np.log1p(df["Low Qual Fin SF"])
df["3Ssn Porch"] = np.log1p(df["3Ssn Porch"])

X = df.drop("SalePrice", axis=1)
y = df["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42,)

numeric_features = X.select_dtypes(include=[np.number]).columns
categorical_features = X.select_dtypes(exclude=[np.number]).columns

numeric_transformer = Pipeline(
	steps=[
		("imputer", SimpleImputer(strategy="median")),
	]
)

categorical_transformer = Pipeline(
	steps=[
		("imputer", SimpleImputer(strategy="most_frequent")),
		("onehot", OneHotEncoder(handle_unknown="ignore")),
	]
)

preprocessor = ColumnTransformer(
	transformers=[
		("num", numeric_transformer, numeric_features),
		("cat", categorical_transformer, categorical_features),
	]
)

model = Pipeline(
	steps=[
		("preprocessor", preprocessor),
		("regressor", LinearRegression()),
	]
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
print("MAE:", mae)
print("RMSE:", rmse)
print("R2:", r2)

sample_predictions = pd.DataFrame(
	{
		"Actual": np.expm1(y_test.head(5)),
		"Predicted": np.expm1(y_pred[:5]),
	}
)

print(sample_predictions)
