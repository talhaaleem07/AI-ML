# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score, mean_squared_error

# # 1. Data load karo
# df = pd.read_csv('House Price Prediction Dataset.csv')
# print(df.columns.tolist())  # sanity check — run this once to confirm names

# # 2. X = features, y = target
# X = df[['Area', 'Bedrooms', 'Bathrooms']]
# y = df['Price']

# # 3. Train test split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # 4. Model train karo
# model = LinearRegression()
# model.fit(X_train, y_train)

# # 5. Prediction + Check accuracy
# y_pred = model.predict(X_test)
# print("R-square:", r2_score(y_test, y_pred))
# print("MSE:", mean_squared_error(y_test, y_pred))

# # 6. Nayi house ki price predict karo
# new_house = pd.DataFrame([[1500, 3, 2]], columns=['Area', 'Bedrooms', 'Bathrooms'])
# print("Predicted Price:", model.predict(new_house)[0])

# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# from pathlib import Path
# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import StandardScaler, MinMaxScaler

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# df = pd.read_csv('House Price Prediction Dataset.csv')

# df['Area in marla'] = df['Area'] / 272.3
# print(df['Area in marla'])

# x = df[['Area in marla']]
# y = df['Price']

# X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# model = LinearRegression()
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)
# print(y_pred)

# r2 = r2_score(y_test, y_pred)
# print('R-square:', r2)

# mse = mean_squared_error(y_test, y_pred)
# print('MSE:', mse)

# mae = mean_absolute_error(y_test, y_pred)
# print('MAE:', mae)

import pandas as pd
import numpy as np

from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


# =========================================================
# 1. Load Dataset
# =========================================================

df = pd.read_csv("House Price Prediction Dataset.csv")

print("Dataset shape:", df.shape)


# =========================================================
# 2. Features and Target
# =========================================================

X = df.drop(columns=["Price", "Id"])
y = df["Price"]


# =========================================================
# 3. Feature Types
# =========================================================

numeric_features = [
    "Area",
    "Bedrooms",
    "Bathrooms",
    "Floors",
    "YearBuilt"
]

categorical_features = [
    "Location",
    "Condition",
    "Garage"
]


# =========================================================
# 4. Preprocessing
# =========================================================

numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])


preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)


# =========================================================
# 5. Linear Regression Model
# =========================================================

model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])


# =========================================================
# 6. Train/Test Split
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# =========================================================
# 7. Train
# =========================================================

model.fit(X_train, y_train)

print("\nModel trained successfully!")


# =========================================================
# 8. Test Predictions
# =========================================================

y_pred = model.predict(X_test)


# =========================================================
# 9. Evaluation
# =========================================================

r2 = r2_score(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

mae = mean_absolute_error(y_test, y_pred)


print("\n========== MODEL PERFORMANCE ==========")
print("R² Score :", r2)
print("MSE      :", mse)
print("RMSE     :", rmse)
print("MAE      :", mae)


# =========================================================
# 10. Cross-validation check
# =========================================================

cv = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model, X, y, cv=cv, scoring="r2")

print("\n========== CROSS-VALIDATION ==========")
print("Fold R² scores:", cv_scores)
print("Mean CV R²   :", cv_scores.mean())

if cv_scores.mean() <= 0:
    print(
        "WARNING: The dataset does not contain enough useful information "
        "to predict house prices reliably. Add better price-related data "
        "before trusting predictions."
    )


# =========================================================
# 11. User Input
# =========================================================

print("\n========================================")
print("       HOUSE PRICE PREDICTOR")
print("========================================")

marla = float(input("Enter house area in Marla: "))

bedrooms = int(input("Enter number of bedrooms: "))

bathrooms = int(input("Enter number of bathrooms: "))

floors = int(input("Enter number of floors: "))

year_built = int(input("Enter year built: "))

location = input("Enter location: ")

condition = input("Enter condition: ")

garage = input("Does the house have a garage? (Yes/No): ")


# =========================================================
# 12. Marla → Square Feet
# =========================================================

area_sqft = marla * 272.3


# =========================================================
# 13. Create Input Data
# =========================================================

new_house = pd.DataFrame({
    "Area": [area_sqft],
    "Bedrooms": [bedrooms],
    "Bathrooms": [bathrooms],
    "Floors": [floors],
    "YearBuilt": [year_built],
    "Location": [location],
    "Condition": [condition],
    "Garage": [garage]
})


# =========================================================
# 14. Predict
# =========================================================

predicted_price = model.predict(new_house)


# =========================================================
# 15. Result
# =========================================================

print("\n========== PREDICTION ==========")

print(f"Area: {marla} Marla")
print(f"Area: {area_sqft:.2f} sq ft")
print(f"Predicted Price: {predicted_price[0]:,.2f}")

print("================================")