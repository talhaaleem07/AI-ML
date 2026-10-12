# ============================================================
# UPDATED VERSION - PAKISTAN HOUSE PRICE PREDICTION
# EDA + PREPROCESSING + LINEAR REGRESSION
# USING GRADIENT DESCENT
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# ============================================================
# REVISED, LEAKAGE-FREE ASSIGNMENT WORKFLOW
# ============================================================
# This block is intentionally before the original classroom draft below.
# SystemExit prevents the old code from running after this finished workflow.
exec(r'''
from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

PATH = Path(__file__).with_name("pakistan house prediction dataset.csv")
TARGET, CURRENT_YEAR = "Price_PKR", 2026
NUM = ["Area_SqFt", "Bedrooms", "Bathrooms", "Floors", "Year_Built", "Garage"]
CAT = ["City", "Location", "Condition", "Property_Type", "Furnished", "Corner_Property", "Park_Facing"]

def numeric(s):
    s=s.astype("string").str.replace(",","",regex=False)
    return pd.to_numeric(s.str.replace(r"(?i)\bsq\.?\s*ft\.?\b","",regex=True).str.strip(),errors="coerce")

def category(s):
    out=s.astype("string").str.strip().str.replace(r"\s+"," ",regex=True).str.title()
    return out.astype(object).where(out.notna(),np.nan)

def show_metrics(label,y,p):
    mse=mean_squared_error(y,p); mae=mean_absolute_error(y,p); rmse=np.sqrt(mse); r2=r2_score(y,p)
    print(f"\n{label}\nMSE: {mse:,.2f}\nMAE: {mae:,.2f}\nRMSE: {rmse:,.2f}\nR²: {r2:.4f}")
    return mae,rmse,r2

class CustomGradientDescent:
    def __init__(self,lr=.03,iterations=10000): self.lr,self.iterations=lr,iterations; self.loss_history=[]
    def fit(self,X,y):
        self.weights=np.zeros(X.shape[1])
        for i in range(self.iterations):
            error=X@self.weights-y; loss=float(np.mean(error**2)); self.loss_history.append(loss)
            self.weights-=self.lr*(2/len(X))*(X.T@error); self.n_iterations_=i+1
            if i%500==0: print(f"Iteration {i}: Loss = {loss:.6f}")
        return self
    def predict(self,X): return X@self.weights

def add_features(X):
    X=X.copy()
    # Predictor-only features; Price_Per_SqFt is never created because it leaks target data.
    X["House_Age"]=CURRENT_YEAR-X["Year_Built"]
    X["Bathrooms_Per_Bedroom"]=X["Bathrooms"]/X["Bedrooms"]
    X["Area_Per_Bedroom"]=X["Area_SqFt"]/X["Bedrooms"]
    return X

def get_number(label,minimum,maximum=None):
    while True:
        try:
            value=float(input(label))
            if value<=minimum or (maximum is not None and value>maximum): raise ValueError
            return value
        except ValueError: print("Invalid value. Please try again.")

def main():
    raw=pd.read_csv(PATH)
    print("="*60+"\nDATASET VERIFICATION\n"+"="*60)
    print("Dataset file:",PATH.name,"\nDataset shape:",raw.shape,"\nTarget column:",TARGET)
    print("Columns:",raw.columns.tolist(),"\nData types:\n",raw.dtypes.to_string())
    print("Missing values:\n",raw.isna().sum().to_string())
    print("Duplicate rows:",raw.duplicated().sum(),"\nDuplicate IDs:",raw.ID.duplicated().sum())
    print("Numeric columns:",NUM+[TARGET],"\nCategorical columns:",CAT,"\n"+"="*60)

    d=raw.drop_duplicates().copy()
    for c in NUM+[TARGET]: d[c]=numeric(d[c])
    for c in CAT: d[c]=category(d[c])
    suspicious=(d[TARGET]<1_000_000)|(d[TARGET]>500_000_000)
    print("\nSUSPICIOUS RECORDS BEFORE HANDLING")
    print("Area <= 0:",int((d.Area_SqFt<=0).sum())," Price corruption candidates:",int(suspicious.sum()))
    print(d.loc[suspicious,["ID","Area_SqFt","City","Location",TARGET]].sort_values(TARGET).to_string(index=False))
    repeated=d[d.ID.duplicated(False)]; conflicts=[i for i,g in repeated.groupby("ID") if len(g.drop_duplicates())>1]
    print("Conflicting repeated IDs (reported, not removed merely for repeating):",conflicts)
    for c in ["Area_SqFt","Bedrooms","Bathrooms","Floors"]: d.loc[d[c]<=0,c]=np.nan
    d.loc[d.Garage<0,"Garage"]=np.nan
    d.loc[(d.Year_Built<1900)|(d.Year_Built>CURRENT_YEAR),"Year_Built"]=np.nan
    remove=d[TARGET].isna()|suspicious
    print("Exact duplicate rows removed:",raw.duplicated().sum()," Rows removed for missing/corrupted target:",int(remove.sum()))
    d=d.loc[~remove].reset_index(drop=True)

    print("\nEDA\nFirst rows:\n",raw.head().to_string())
    print("\nNumeric summary:\n",d[NUM+[TARGET]].describe().to_string())
    for c in CAT: print("\n",c,"\n",d[c].value_counts(dropna=False).head(20).to_string())
    corr=d[NUM+[TARGET]].corr(); print("\nCorrelation matrix:\n",corr.to_string())

    X,y=d.drop(columns=[TARGET,"ID"]),d[TARGET] # ID is never a feature.
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=42)
    Xtr,Xte=add_features(Xtr),add_features(Xte)
    engineered=NUM+["House_Age","Bathrooms_Per_Bedroom","Area_Per_Bedroom"]
    # Imputers, scaler and encoder are fitted ONLY on the training data.
    prep=ColumnTransformer([("num",Pipeline([("impute",SimpleImputer(strategy="median")),("scale",StandardScaler())]),engineered),("cat",Pipeline([("impute",SimpleImputer(strategy="constant",fill_value="Unknown")),("onehot",OneHotEncoder(handle_unknown="ignore",sparse_output=False))]),CAT)])
    A=prep.fit_transform(Xtr); B=prep.transform(Xte); A=np.c_[np.ones(len(A)),A]; B=np.c_[np.ones(len(B)),B]
    print(f"\nTraining samples: {len(Xtr)}\nTesting samples: {len(Xte)}\nNumber of features: {A.shape[1]-1}")
    baseline=show_metrics("Baseline (training mean)",yte,np.full(len(yte),ytr.mean()))
    scaler_y=StandardScaler(); model=CustomGradientDescent().fit(A,scaler_y.fit_transform(ytr.to_numpy().reshape(-1,1)).ravel())
    prediction=scaler_y.inverse_transform(model.predict(B).reshape(-1,1)).ravel(); result=show_metrics("Custom Gradient Descent",yte,prediction)
    # Fair log-target experiment; its metrics are converted back to PKR.
    log_model=CustomGradientDescent().fit(A,np.log1p(ytr.to_numpy())); show_metrics("Log1p target comparison",yte,np.expm1(log_model.predict(B)))
    print("\nFINAL REPORT")
    print(f"Dataset file used: {PATH.name}\nOriginal dataset shape: {raw.shape}\nCleaned dataset shape: {d.shape}\nBaseline MAE/RMSE/R²: {baseline[0]:,.2f} / {baseline[1]:,.2f} / {baseline[2]:.4f}\nGradient Descent MAE/RMSE/R²: {result[0]:,.2f} / {result[1]:,.2f} / {result[2]:.4f}\nFinal training loss: {model.loss_history[-1]:.8f}\nIterations: {model.n_iterations_}\nImprovement over previous R² 0.2257: {result[2]-.2257:+.4f}")

    plt.figure(); plt.hist(d[TARGET],bins=40); plt.title("Price Distribution")
    plt.figure(); plt.scatter(d.Area_SqFt,d[TARGET],alpha=.6); plt.title("Area vs Price")
    plt.figure(); d.City.value_counts().plot(kind="bar"); plt.title("City Distribution")
    plt.figure(); plt.imshow(corr,cmap="coolwarm",vmin=-1,vmax=1); plt.colorbar(); plt.xticks(range(len(corr)),corr.columns,rotation=45,ha="right"); plt.yticks(range(len(corr)),corr.index); plt.title("Correlation Matrix")
    plt.figure(); plt.plot(model.loss_history); plt.title("Gradient Descent Loss Curve")
    plt.figure(); plt.scatter(yte,prediction,alpha=.6); lo=min(yte.min(),prediction.min()); hi=max(yte.max(),prediction.max()); plt.plot([lo,hi],[lo,hi],"r--"); plt.title("Actual vs Predicted")
    if "agg" not in plt.get_backend().lower(): plt.show()

    print("\nHOUSE PRICE PREDICTOR")
    u=pd.DataFrame({"Area_SqFt":[get_number("Area: ",0)],"Bedrooms":[get_number("Bedrooms: ",0)],"Bathrooms":[get_number("Bathrooms: ",0)],"Floors":[get_number("Floors: ",0)],"Year_Built":[get_number("Year built: ",1899,CURRENT_YEAR)],"Garage":[get_number("Garage: ",-1)]})
    for c in CAT: u[c]=[category(pd.Series([input(c.replace("_"," ")+": ")])).iloc[0]]
    up=scaler_y.inverse_transform(model.predict(np.c_[np.ones(1),prep.transform(add_features(u))]).reshape(-1,1))[0,0]
    print(f"Estimated House Price: PKR {max(up,0):,.0f}")
main()
''')
raise SystemExit


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv("pakistan house prediction dataset.csv")

print("=" * 60)
print("              DATASET INFORMATION")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
print(df.info())


# ============================================================
# 2. BASIC EDA
# ============================================================

print("\n" + "=" * 60)
print("                 BASIC EDA")
print("=" * 60)

print("\nStatistical Summary:")
print(df.describe(include="all"))


# ============================================================
# 3. MISSING VALUES
# ============================================================

print("\n" + "=" * 60)
print("                 MISSING VALUES")
print("=" * 60)

missing_values = df.isnull().sum()

missing_percentage = (
    df.isnull().sum() / len(df) * 100
)

missing_report = pd.DataFrame({
    "Missing Values": missing_values,
    "Percentage": missing_percentage
})

print(missing_report)


# ============================================================
# 4. DUPLICATE ROWS
# ============================================================

print("\n" + "=" * 60)
print("                 DUPLICATE ROWS")
print("=" * 60)

duplicate_count = df.duplicated().sum()

print("Number of duplicate rows:", duplicate_count)

if duplicate_count > 0:
    df = df.drop_duplicates().reset_index(drop=True)
    print("Duplicate rows removed.")

print("New dataset shape:", df.shape)


# ============================================================
# 5. UNIQUE VALUES OF CATEGORICAL COLUMNS
# ============================================================

print("\n" + "=" * 60)
print("              CATEGORICAL VALUES")
print("=" * 60)

categorical_columns = df.select_dtypes(
    include=["object"]
).columns

for column in categorical_columns:
    print("\n", column)
    print(df[column].value_counts(dropna=False).head(20))


# ============================================================
# 6. CLEAN NUMERIC COLUMNS
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

    if column in df.columns:

        df[column] = (
            df[column]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.replace("sqft", "", case=False, regex=False)
            .str.strip()
        )

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


# ============================================================
# 7. CLEAN CATEGORICAL COLUMNS
# ============================================================

categorical_features = [
    "City",
    "Location",
    "Condition",
    "Property_Type",
    "Furnished",
    "Corner_Property",
    "Park_Facing"
]

for column in categorical_features:

    if column in df.columns:

        df[column] = (
            df[column]
            .astype("string")
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
            .str.title()
        )


# ============================================================
# 8. CHECK NUMERIC DATA AFTER CLEANING
# ============================================================

print("\n" + "=" * 60)
print("          CLEANED NUMERIC COLUMNS")
print("=" * 60)

print(df[numeric_columns].describe())


# ============================================================
# 9. INVALID VALUE CHECK
# ============================================================

print("\n" + "=" * 60)
print("              INVALID VALUES")
print("=" * 60)

print("\nArea <= 0:")
print(df[df["Area_SqFt"] <= 0][
    ["Area_SqFt", "Price_PKR"]
])

print("\nBedrooms <= 0:")
print(df[df["Bedrooms"] <= 0][
    ["Bedrooms", "Price_PKR"]
])

print("\nBathrooms <= 0:")
print(df[df["Bathrooms"] <= 0][
    ["Bathrooms", "Price_PKR"]
])

print("\nYear Built outside expected range:")
print(
    df[
        (df["Year_Built"] < 1900) |
        (df["Year_Built"] > 2026)
    ][
        ["Year_Built", "Price_PKR"]
    ]
)


# ============================================================
# 10. HANDLE INVALID NUMERIC VALUES
# ============================================================

# Area cannot be zero or negative
df.loc[
    df["Area_SqFt"] <= 0,
    "Area_SqFt"
] = np.nan

# Bedrooms cannot be zero or negative
df.loc[
    df["Bedrooms"] <= 0,
    "Bedrooms"
] = np.nan

# Bathrooms cannot be zero or negative
df.loc[
    df["Bathrooms"] <= 0,
    "Bathrooms"
] = np.nan

# Floors cannot be zero or negative
df.loc[
    df["Floors"] <= 0,
    "Floors"
] = np.nan

# Garage cannot be negative
df.loc[
    df["Garage"] < 0,
    "Garage"
] = np.nan

# Year must be reasonable
df.loc[
    (df["Year_Built"] < 1900) |
    (df["Year_Built"] > 2026),
    "Year_Built"
] = np.nan


# ============================================================
# 11. REMOVE EXTREME CORRUPTED TARGET VALUES
# ============================================================

# Keep prices within a reasonable range.
# The dataset contains obvious corrupted values such as
# 9,999,999,999 and 10,000,000,000.

df = df[
    (df["Price_PKR"] > 0) &
    (df["Price_PKR"] < 500_000_000)
].copy()


# ============================================================
# 12. EDA - PRICE DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

plt.hist(
    df["Price_PKR"].dropna(),
    bins=40
)

plt.title("House Price Distribution")
plt.xlabel("Price (PKR)")
plt.ylabel("Number of Houses")

plt.show()


# ============================================================
# 13. EDA - AREA VS PRICE
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Area_SqFt"],
    df["Price_PKR"],
    alpha=0.6
)

plt.title("Area vs House Price")
plt.xlabel("Area (Sq Ft)")
plt.ylabel("Price (PKR)")

plt.show()


# ============================================================
# 14. EDA - CITY DISTRIBUTION
# ============================================================

if "City" in df.columns:

    plt.figure(figsize=(10, 6))

    df["City"].value_counts().plot(
        kind="bar"
    )

    plt.title("Number of Houses by City")
    plt.xlabel("City")
    plt.ylabel("Number of Houses")

    plt.xticks(rotation=45)

    plt.show()


# ============================================================
# 15. CORRELATION ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("              CORRELATION MATRIX")
print("=" * 60)

correlation_columns = [
    "Area_SqFt",
    "Bedrooms",
    "Bathrooms",
    "Floors",
    "Year_Built",
    "Garage",
    "Price_PKR"
]

correlation_matrix = df[
    correlation_columns
].corr()

print(correlation_matrix)


# ============================================================
# 16. TARGET CORRELATION
# ============================================================

print("\n" + "=" * 60)
print("         CORRELATION WITH PRICE")
print("=" * 60)

price_correlation = (
    correlation_matrix["Price_PKR"]
    .sort_values(ascending=False)
)

print(price_correlation)


# ============================================================
# 17. HANDLE MISSING VALUES
# ============================================================

print("\n" + "=" * 60)
print("          MISSING VALUES BEFORE")
print("=" * 60)

print(df.isnull().sum())


# Target cannot be imputed for supervised learning
df = df.dropna(
    subset=["Price_PKR"]
).reset_index(drop=True)


# Numeric columns -> median
for column in numeric_columns:

    if column == "Price_PKR":
        continue

    if column in df.columns:

        df[column] = df[column].fillna(
            df[column].median()
        )


# Categorical columns -> mode
for column in categorical_features:

    if column in df.columns:

        if df[column].notna().any():

            mode_value = df[column].mode()[0]

            df[column] = df[column].fillna(
                mode_value
            )


print("\n" + "=" * 60)
print("          MISSING VALUES AFTER")
print("=" * 60)

print(df.isnull().sum())


# ============================================================
# 18. SEPARATE FEATURES AND TARGET
# ============================================================

X = df.drop(
    columns=["Price_PKR"]
)

y = df["Price_PKR"]


# ID should not be used for prediction
if "ID" in X.columns:
    X = X.drop(columns=["ID"])


# ============================================================
# 19. ONE-HOT ENCODING
# ============================================================

categorical_features = [
    column for column in categorical_features
    if column in X.columns
]

X = pd.get_dummies(
    X,
    columns=categorical_features,
    dtype=float
)


print("\n" + "=" * 60)
print("          AFTER ONE-HOT ENCODING")
print("=" * 60)

print("X shape:", X.shape)


# ============================================================
# 20. TRAIN TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


print("\n" + "=" * 60)
print("             TRAIN TEST SPLIT")
print("=" * 60)

print("Training data:", X_train.shape)
print("Testing data :", X_test.shape)


# ============================================================
# 21. FEATURE SCALING
# ============================================================

scaler_X = StandardScaler()

X_train_scaled = scaler_X.fit_transform(
    X_train
)

X_test_scaled = scaler_X.transform(
    X_test
)


# ============================================================
# 22. TARGET SCALING
# ============================================================

scaler_y = StandardScaler()

y_train_scaled = scaler_y.fit_transform(
    y_train.values.reshape(-1, 1)
).ravel()

y_test_scaled = scaler_y.transform(
    y_test.values.reshape(-1, 1)
).ravel()


# ============================================================
# 23. ADD INTERCEPT TERM
# ============================================================

X_train_gd = np.c_[
    np.ones(X_train_scaled.shape[0]),
    X_train_scaled
]

X_test_gd = np.c_[
    np.ones(X_test_scaled.shape[0]),
    X_test_scaled
]


# ============================================================
# 24. LINEAR REGRESSION WITH GRADIENT DESCENT
# ============================================================

class LinearRegressionGradientDescent:

    def __init__(
        self,
        learning_rate=0.01,
        iterations=5000
    ):

        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = None
        self.loss_history = []

    def fit(self, X, y):

        samples = X.shape[0]
        features = X.shape[1]

        self.weights = np.zeros(features)

        for i in range(self.iterations):

            predictions = X @ self.weights

            errors = predictions - y

            gradient = (
                (2 / samples)
                * (X.T @ errors)
            )

            self.weights -= (
                self.learning_rate * gradient
            )

            mse = np.mean(errors ** 2)

            self.loss_history.append(mse)

            # Print progress
            if i % 500 == 0:

                print(
                    f"Iteration {i}: "
                    f"Loss = {mse:.6f}"
                )

        return self

    def predict(self, X):

        return X @ self.weights


# ============================================================
# 25. CREATE MODEL
# ============================================================

model = LinearRegressionGradientDescent(
    learning_rate=0.01,
    iterations=5000
)


# ============================================================
# 26. TRAIN MODEL
# ============================================================

print("\n" + "=" * 60)
print("             MODEL TRAINING")
print("=" * 60)

model.fit(
    X_train_gd,
    y_train_scaled
)

print("\nModel trained successfully!")


# ============================================================
# 27. MAKE TEST PREDICTIONS
# ============================================================

y_pred_scaled = model.predict(
    X_test_gd
)


# Convert predictions back to PKR
y_pred = scaler_y.inverse_transform(
    y_pred_scaled.reshape(-1, 1)
).ravel()


# ============================================================
# 28. MODEL EVALUATION
# ============================================================

mse = mean_squared_error(
    y_test,
    y_pred
)

mae = mean_absolute_error(
    y_test,
    y_pred
)

rmse = np.sqrt(mse)

r2 = r2_score(
    y_test,
    y_pred
)


print("\n" + "=" * 60)
print("             MODEL PERFORMANCE")
print("=" * 60)

print(f"R² Score : {r2:.4f}")
print(f"MSE      : {mse:,.2f}")
print(f"RMSE     : {rmse:,.2f}")
print(f"MAE      : {mae:,.2f}")

print("=" * 60)


# ============================================================
# 29. GRADIENT DESCENT LOSS CURVE
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    model.loss_history
)

plt.title(
    "Gradient Descent Loss Curve"
)

plt.xlabel(
    "Iterations"
)

plt.ylabel(
    "Mean Squared Error"
)

plt.show()


# ============================================================
# 30. ACTUAL VS PREDICTED
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    y_test,
    y_pred,
    alpha=0.6
)

# Perfect prediction line
min_value = min(
    y_test.min(),
    y_pred.min()
)

max_value = max(
    y_test.max(),
    y_pred.max()
)

plt.plot(
    [min_value, max_value],
    [min_value, max_value]
)

plt.title(
    "Actual vs Predicted House Prices"
)

plt.xlabel(
    "Actual Price (PKR)"
)

plt.ylabel(
    "Predicted Price (PKR)"
)

plt.show()


# ============================================================
# 31. USER INPUT HOUSE PRICE PREDICTION
# ============================================================

print("\n")
print("=" * 60)
print("             HOUSE PRICE PREDICTOR")
print("=" * 60)

print("\nEnter the details of the house:")


area = float(
    input("Area (sq ft): ")
)

bedrooms = float(
    input("Number of bedrooms: ")
)

bathrooms = float(
    input("Number of bathrooms: ")
)

floors = float(
    input("Number of floors: ")
)

year_built = float(
    input("Year built: ")
)

garage = float(
    input("Garage capacity: ")
)


city = input(
    "City: "
).strip().title()


location = input(
    "Location: "
).strip().title()


condition = input(
    "Condition (Excellent/Good/Fair/Poor/New/Needs Renovation): "
).strip().title()


property_type = input(
    "Property Type (House/Villa): "
).strip().title()


furnished = input(
    "Furnished? (Yes/No): "
).strip().title()


corner_property = input(
    "Corner Property? (Yes/No): "
).strip().title()


park_facing = input(
    "Park Facing? (Yes/No): "
).strip().title()


# ============================================================
# 32. CREATE USER DATAFRAME
# ============================================================

user_data = pd.DataFrame({

    "Area_SqFt": [area],

    "Bedrooms": [bedrooms],

    "Bathrooms": [bathrooms],

    "Floors": [floors],

    "Year_Built": [year_built],

    "City": [city],

    "Location": [location],

    "Condition": [condition],

    "Garage": [garage],

    "Property_Type": [property_type],

    "Furnished": [furnished],

    "Corner_Property": [corner_property],

    "Park_Facing": [park_facing]
})


# ============================================================
# 33. USER INPUT PREPROCESSING
# ============================================================

user_encoded = pd.get_dummies(
    user_data,
    columns=categorical_features,
    dtype=float
)


# Make sure user input has EXACTLY
# the same columns as training data

user_encoded = user_encoded.reindex(
    columns=X_train.columns,
    fill_value=0
)


# ============================================================
# 34. SCALE USER INPUT
# ============================================================

user_scaled = scaler_X.transform(
    user_encoded
)


# ============================================================
# 35. ADD INTERCEPT
# ============================================================

user_gd = np.c_[
    np.ones(user_scaled.shape[0]),
    user_scaled
]


# ============================================================
# 36. PREDICT USER HOUSE PRICE
# ============================================================

user_prediction_scaled = model.predict(
    user_gd
)


# Convert scaled prediction back to PKR

user_prediction = scaler_y.inverse_transform(
    user_prediction_scaled.reshape(-1, 1)
).ravel()[0]


# ============================================================
# 37. DISPLAY USER PREDICTION
# ============================================================

print("\n" + "=" * 60)
print("             PREDICTED HOUSE PRICE")
print("=" * 60)

print(
    f"\nEstimated House Price: "
    f"PKR {user_prediction:,.0f}"
)

print("=" * 60)

