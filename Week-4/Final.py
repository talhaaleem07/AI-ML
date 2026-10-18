import numpy as np
import pandas as pd

np.random.seed(42)
pd.options.display.float_format = "{:,.4f}".format
df = pd.read_csv("pakistan house prediction dataset.csv")
print("Shape:", df.shape)
print("\nColumn types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum()[df.isna().sum() > 0])
print("\nDuplicate rows:", df.duplicated().sum())
print("\nFirst 5 rows:\n", df.head())
df = df.drop_duplicates().drop(columns="ID")
def to_number(col):
    col = col.astype(str).str.replace(",", "", regex=False)
    return pd.to_numeric(col.str.extract(r"(-?\d+\.?\d*)")[0], errors="coerce")

for c in ["Area_SqFt", "Year_Built", "Price_PKR"]:
    df[c] = to_number(df[c])
for c in ["City", "Location", "Condition", "Property_Type"]:
    df[c] = df[c].str.strip().str.lower()
for c in ["Furnished", "Corner_Property", "Park_Facing"]:
    df[c] = (df[c].str.strip().str.lower() == "yes").astype(int)
city_of = df.dropna(subset=["City"]).groupby("Location")["City"].agg(lambda x: x.mode()[0])
df["City"] = df["City"].fillna(df["Location"].map(city_of))
df = df.dropna(subset=["Price_PKR"])
df = df[df["Price_PKR"].between(1e6, 1e9)]
df = df[df["Area_SqFt"].isna() | df["Area_SqFt"].between(200, 15000)]

df["House_Age"] = 2026 - df["Year_Built"]
df = df.drop(columns="Year_Built").reset_index(drop=True)
print("\n--- After cleaning ---  Rows:", len(df))
print("\nStatistics:\n", df[["Area_SqFt", "House_Age", "Price_PKR"]].describe())
print("\nCorrelation with Price:\n", df.corr(numeric_only=True)["Price_PKR"].drop("Price_PKR").sort_values())
print("\nMedian price (PKR) by City:\n", df.groupby("City")["Price_PKR"].median())
print("\nMedian price (PKR) by Condition:\n", df.groupby("Condition")["Price_PKR"].median())
y = np.log(df["Price_PKR"].values)
X = pd.get_dummies(df.drop(columns="Price_PKR"),
                   columns=["City", "Location", "Condition", "Property_Type"],
                   drop_first=True, dtype=float)
X["Area_SqFt"] = np.log(X["Area_SqFt"])

idx = np.random.permutation(len(X))
cut = int(0.8 * len(X))
X_train, X_test = X.iloc[idx[:cut]], X.iloc[idx[cut:]]
y_train, y_test = y[idx[:cut]], y[idx[cut:]]
medians = X_train.median()
X_train, X_test = X_train.fillna(medians), X_test.fillna(medians)
mean, std = X_train.mean(), X_train.std().replace(0, 1)
X_train = ((X_train - mean) / std).values
X_test = ((X_test - mean) / std).values
def gradient_descent(X, y, lr=0.1, epochs=5000):
    m, n = X.shape
    w, b = np.zeros(n), 0.0
    for epoch in range(epochs):
        error = X @ w + b - y
        w -= lr * (X.T @ error) / m
        b -= lr * error.mean()
        if epoch % 1000 == 0:
            print(f"Epoch {epoch:4d}  loss = {(error ** 2).mean() / 2:.5f}")
    return w, b

print("\n--- Training ---")
w, b = gradient_descent(X_train, y_train)
def evaluate(y_true, y_pred):
    err = y_true - y_pred
    mse = np.mean(err ** 2)
    return {"MSE": mse,
            "MAE": np.mean(np.abs(err)),
            "RMSE": np.sqrt(mse),
            "R2": 1 - np.sum(err ** 2) / np.sum((y_true - y_true.mean()) ** 2)}

pred_train, pred_test = X_train @ w + b, X_test @ w + b

results = pd.DataFrame({
    "Train (log price)": evaluate(y_train, pred_train),
    "Test (log price)": evaluate(y_test, pred_test),
    "Test (PKR)": evaluate(np.exp(y_test), np.exp(pred_test)),
})
print("\n--- Evaluation ---\n", results)
MARLA_TO_SQFT = 272.25

def predict_price(location, marla, bedrooms, bathrooms=None, floors=None, garage=None,
                  house_age=None, condition="good", property_type="house",
                  furnished=0, corner=0, park_facing=0):
    location = location.strip().lower()
    if location not in city_of.index:
        raise ValueError(f"Unknown location '{location}'. Valid: {sorted(city_of.index)}")

    row = pd.Series(0.0, index=X.columns)
    row["Area_SqFt"] = np.log(marla * MARLA_TO_SQFT)
    row["Bedrooms"] = bedrooms
    row["Bathrooms"] = bathrooms if bathrooms is not None else medians["Bathrooms"]
    row["Floors"] = floors if floors is not None else medians["Floors"]
    row["Garage"] = garage if garage is not None else medians["Garage"]
    row["House_Age"] = house_age if house_age is not None else medians["House_Age"]
    row["Furnished"], row["Corner_Property"], row["Park_Facing"] = furnished, corner, park_facing
    for col in [f"City_{city_of[location]}", f"Location_{location}",
                f"Condition_{condition.lower()}", f"Property_Type_{property_type.lower()}"]:
        if col in row.index:
            row[col] = 1.0

    scaled = ((row - mean) / std).values
    return float(np.exp(scaled @ w + b))
print("\n--- Predict House Price ---")
loc = input("Location (e.g. dha phase 5): ")
marla = float(input("Size in marla: "))
beds = int(input("Bedrooms: "))
print(f"\nPredicted price: PKR {predict_price(loc, marla, beds):,.0f}")