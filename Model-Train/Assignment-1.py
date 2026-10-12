import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


# ============================================================
# 1. LOAD DATA
# ============================================================

file = "pakistan house prediction dataset.csv"

df = pd.read_csv(file)

print("Original dataset shape:", df.shape)


# ============================================================
# 2. CLEAN COLUMN NAMES
# ============================================================

df.columns = df.columns.str.strip()


# ============================================================
# 3. CONVERT NUMERIC COLUMNS
# ============================================================

numeric_columns = [
    "Area_SqFt",
    "Bedrooms",
    "Bathrooms",
    "Floors",
    "Year_Built",
    "Garage",
    "Price_PKR"
]

for column in numeric_columns:

    df[column] = (
        df[column]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace("sqft", "", case=False, regex=False)
        .str.strip()
    )

    df[column] = pd.to_numeric(df[column], errors="coerce")


# ============================================================
# 4. REMOVE DUPLICATE ROWS
# ============================================================

df = df.drop_duplicates()

print("After removing duplicates:", df.shape)


# ============================================================
# 5. REMOVE INVALID VALUES
# ============================================================

df.loc[df["Area_SqFt"] <= 0, "Area_SqFt"] = np.nan
df.loc[df["Bedrooms"] <= 0, "Bedrooms"] = np.nan
df.loc[df["Bathrooms"] <= 0, "Bathrooms"] = np.nan
df.loc[df["Floors"] <= 0, "Floors"] = np.nan
df.loc[df["Garage"] < 0, "Garage"] = np.nan

# Year should be between 1900 and 2026
df.loc[
    (df["Year_Built"] < 1900) |
    (df["Year_Built"] > 2026),
    "Year_Built"
] = np.nan


# ============================================================
# 6. REMOVE BAD TARGET VALUES
# ============================================================

# Remove houses with missing price
df = df.dropna(subset=["Price_PKR"])

# Remove extremely suspicious prices
df = df[
    (df["Price_PKR"] >= 1_000_000) &
    (df["Price_PKR"] <= 500_000_000)
]

print("After cleaning:", df.shape)


# ============================================================
# 7. FEATURES AND TARGET
# ============================================================

X = df.drop(columns=["Price_PKR", "ID"])

y = df["Price_PKR"]


# ============================================================
# 8. CREATE USEFUL FEATURES
# ============================================================

# Age of house
X["House_Age"] = 2026 - X["Year_Built"]

# Bathrooms compared with bedrooms
X["Bathrooms_Per_Bedroom"] = (
    X["Bathrooms"] / X["Bedrooms"]
)

# Area available for each bedroom
X["Area_Per_Bedroom"] = (
    X["Area_SqFt"] / X["Bedrooms"]
)


# ============================================================
# 9. TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# ============================================================
# 10. COLUMN TYPES
# ============================================================

numeric_features = [
    "Area_SqFt",
    "Bedrooms",
    "Bathrooms",
    "Floors",
    "Year_Built",
    "Garage",
    "House_Age",
    "Bathrooms_Per_Bedroom",
    "Area_Per_Bedroom"
]

categorical_features = [
    "City",
    "Location",
    "Condition",
    "Property_Type",
    "Furnished",
    "Corner_Property",
    "Park_Facing"
]


# ============================================================
# 11. PREPROCESSING
# ============================================================

# Numeric data
numeric_processing = Pipeline([
    ("fill_missing", SimpleImputer(strategy="median")),
    ("scale", StandardScaler())
])


# Categorical data
categorical_processing = Pipeline([
    ("fill_missing", SimpleImputer(strategy="constant",
                                   fill_value="Unknown")),

    ("one_hot", OneHotEncoder(
        handle_unknown="ignore",
        sparse_output=False
    ))
])


# Combine both
preprocessor = ColumnTransformer([
    ("numbers", numeric_processing, numeric_features),
    ("categories", categorical_processing, categorical_features)
])


# Fit only on training data
X_train = preprocessor.fit_transform(X_train)

# Transform test data
X_test = preprocessor.transform(X_test)


# ============================================================
# 12. SCALE TARGET
# ============================================================

target_scaler = StandardScaler()

y_train_scaled = target_scaler.fit_transform(
    y_train.values.reshape(-1, 1)
).ravel()

y_test_scaled = target_scaler.transform(
    y_test.values.reshape(-1, 1)
).ravel()


# ============================================================
# 13. ADD INTERCEPT
# ============================================================

X_train = np.c_[np.ones(X_train.shape[0]), X_train]

X_test = np.c_[np.ones(X_test.shape[0]), X_test]


# ============================================================
# 14. GRADIENT DESCENT
# ============================================================

weights = np.zeros(X_train.shape[1])

learning_rate = 0.03
iterations = 15000

best_loss = float("inf")
patience = 500
no_improvement = 0

for i in range(iterations):

    # Prediction
    predictions = X_train @ weights

    # Error
    error = predictions - y_train_scaled

    # Mean Squared Error
    loss = np.mean(error ** 2)

    # Gradient
    gradient = (
        2 / len(X_train)
    ) * (X_train.T @ error)

    # Update weights
    weights = weights - learning_rate * gradient


    # Early stopping
    if loss < best_loss - 0.000001:

        best_loss = loss
        no_improvement = 0

    else:

        no_improvement += 1


    if no_improvement >= patience:

        print("Training stopped early at iteration:", i + 1)
        break


print("\nTraining completed!")
print("Final training loss:", loss)
print("Iterations:", i + 1)


# ============================================================
# 15. MAKE PREDICTIONS
# ============================================================

train_prediction_scaled = X_train @ weights

test_prediction_scaled = X_test @ weights


# Convert predictions back to PKR
train_prediction = target_scaler.inverse_transform(
    train_prediction_scaled.reshape(-1, 1)
).ravel()

test_prediction = target_scaler.inverse_transform(
    test_prediction_scaled.reshape(-1, 1)
).ravel()


# ============================================================
# 16. MODEL PERFORMANCE
# ============================================================

train_r2 = r2_score(y_train, train_prediction)

test_r2 = r2_score(y_test, test_prediction)

mae = mean_absolute_error(
    y_test,
    test_prediction
)

mse = mean_squared_error(
    y_test,
    test_prediction
)

rmse = np.sqrt(mse)


print("\n========================================")
print("       MODEL PERFORMANCE")
print("========================================")

print("Training R² :", round(train_r2, 4))
print("Testing R²  :", round(test_r2, 4))

print("MAE         :", round(mae, 2))
print("RMSE        :", round(rmse, 2))

print("========================================")


# ============================================================
# 17. PREDICT A NEW HOUSE
# ============================================================

print("\n========================================")
print("       HOUSE PRICE PREDICTOR")
print("========================================")


area = float(input("Area (sq ft): "))
bedrooms = float(input("Bedrooms: "))
bathrooms = float(input("Bathrooms: "))
floors = float(input("Floors: "))
year = float(input("Year Built: "))
garage = float(input("Garage: "))

city = input("City: ")
location = input("Location: ")
condition = input("Condition: ")
property_type = input("Property Type: ")
furnished = input("Furnished (Yes/No): ")
corner = input("Corner Property (Yes/No): ")
park = input("Park Facing (Yes/No): ")


# Create new house
new_house = pd.DataFrame([{
    "Area_SqFt": area,
    "Bedrooms": bedrooms,
    "Bathrooms": bathrooms,
    "Floors": floors,
    "Year_Built": year,
    "Garage": garage,

    "City": city,
    "Location": location,
    "Condition": condition,
    "Property_Type": property_type,
    "Furnished": furnished,
    "Corner_Property": corner,
    "Park_Facing": park
}])


# Create same features used during training
new_house["House_Age"] = 2026 - new_house["Year_Built"]

new_house["Bathrooms_Per_Bedroom"] = (
    new_house["Bathrooms"] /
    new_house["Bedrooms"]
)

new_house["Area_Per_Bedroom"] = (
    new_house["Area_SqFt"] /
    new_house["Bedrooms"]
)


# Transform new house
new_house = preprocessor.transform(new_house)

# Add intercept
new_house = np.c_[
    np.ones(new_house.shape[0]),
    new_house
]


# Predict
new_price_scaled = new_house @ weights

new_price = target_scaler.inverse_transform(
    new_price_scaled.reshape(-1, 1)
)[0][0]


print("\nEstimated House Price:")
print(f"PKR {new_price:,.0f}")

print("========================================")
