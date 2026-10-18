import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score



# 1. LOAD DATASET

df = pd.read_csv("pakistan house prediction dataset.csv")

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())



# 2. EDA

print("\nStatistical Summary:")
print(df.describe())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# 3. AREA TO NUMERIC

df["Area_SqFt"] = (
    df["Area_SqFt"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.extract(r"(\d+\.?\d*)")[0]
    .astype(float)
)


# 4. PRICE TO NUMERIC


df["Price_PKR"] = (
    df["Price_PKR"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.extract(r"(\d+\.?\d*)")[0]
    .astype(float)
)


# 5. YEAR TO NUMERIC

df["Year_Built"] = (
    df["Year_Built"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.extract(r"(\d{4})")[0]
    .astype(float)
)


# =====================================================
# 6. SQ FT TO MARLA
# =====================================================

# 1 Marla = 272.25 Sq Ft

df["marla"] = df["Area_SqFt"] / 272.25


# =====================================================
# 7. REMOVE DUPLICATES
# =====================================================

df = df.drop_duplicates()


# =====================================================
# 8. REMOVE MISSING AREA AND PRICE
# =====================================================

df = df.dropna(
    subset=[
        "Area_SqFt",
        "Price_PKR"
    ]
)


# =====================================================
# 9. REMOVE INVALID / EXTREME VALUES
# =====================================================

df = df[
    (df["Area_SqFt"] > 0) &
    (df["Price_PKR"] >= 1000000) &
    (df["Price_PKR"] <= 300000000)
]


# =====================================================
# 10. NUMERICAL MISSING VALUES
# =====================================================

df["Bedrooms"] = df["Bedrooms"].fillna(
    df["Bedrooms"].median()
)

df["Bathrooms"] = df["Bathrooms"].fillna(
    df["Bathrooms"].median()
)

df["Floors"] = df["Floors"].fillna(
    df["Floors"].median()
)

df["Year_Built"] = df["Year_Built"].fillna(
    df["Year_Built"].median()
)

df["Garage"] = df["Garage"].fillna(
    df["Garage"].median()
)


# =====================================================
# 11. CATEGORICAL MISSING VALUES
# =====================================================

df["City"] = df["City"].fillna("Unknown")

df["Location"] = df["Location"].fillna("Unknown")

df["Condition"] = df["Condition"].fillna("Unknown")

df["Property_Type"] = df["Property_Type"].fillna("Unknown")

df["Furnished"] = df["Furnished"].fillna("Unknown")

df["Corner_Property"] = df["Corner_Property"].fillna("Unknown")

df["Park_Facing"] = df["Park_Facing"].fillna("Unknown")


# =====================================================
# 12. CLEAN CATEGORICAL VALUES
# =====================================================

df["City"] = (
    df["City"]
    .astype(str)
    .str.strip()
)

df["Location"] = (
    df["Location"]
    .astype(str)
    .str.strip()
)

df["Condition"] = (
    df["Condition"]
    .astype(str)
    .str.strip()
)

df["Property_Type"] = (
    df["Property_Type"]
    .astype(str)
    .str.strip()
    .str.title()
)

df["Furnished"] = (
    df["Furnished"]
    .astype(str)
    .str.strip()
    .str.lower()
)

df["Corner_Property"] = (
    df["Corner_Property"]
    .astype(str)
    .str.strip()
    .str.lower()
)

df["Park_Facing"] = (
    df["Park_Facing"]
    .astype(str)
    .str.strip()
    .str.lower()
)


# =====================================================
# 13. LABEL ENCODING
# =====================================================

city_le = LabelEncoder()

location_le = LabelEncoder()

condition_le = LabelEncoder()

property_type_le = LabelEncoder()

furnished_le = LabelEncoder()

corner_le = LabelEncoder()

park_le = LabelEncoder()


df["City_encoded"] = city_le.fit_transform(
    df["City"]
)

df["Location_encoded"] = location_le.fit_transform(
    df["Location"]
)

df["Condition_encoded"] = condition_le.fit_transform(
    df["Condition"]
)

df["Property_Type_encoded"] = property_type_le.fit_transform(
    df["Property_Type"]
)

df["Furnished_encoded"] = furnished_le.fit_transform(
    df["Furnished"]
)

df["Corner_Property_encoded"] = corner_le.fit_transform(
    df["Corner_Property"]
)

df["Park_Facing_encoded"] = park_le.fit_transform(
    df["Park_Facing"]
)


# =====================================================
# 14. CLEANED DATA INFORMATION
# =====================================================

print("\n================================")
print("AFTER PREPROCESSING")
print("================================")

print("Cleaned Dataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())


# =====================================================
# 15. FEATURES
# =====================================================

X = df[
    [
        "marla",
        "Bedrooms",
        "Bathrooms",
        "Floors",
        "Year_Built",
        "Garage",
        "City_encoded",
        "Location_encoded",
        "Condition_encoded",
        "Property_Type_encoded",
        "Furnished_encoded",
        "Corner_Property_encoded",
        "Park_Facing_encoded"
    ]
]

y = df["Price_PKR"]


# =====================================================
# 16. TRAIN TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =====================================================
# 17. FEATURE SCALING
# =====================================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)


# =====================================================
# 18. ADD BIAS
# =====================================================

X_train = np.c_[
    np.ones(X_train.shape[0]),
    X_train
]

X_test = np.c_[
    np.ones(X_test.shape[0]),
    X_test
]


# =====================================================
# 19. GRADIENT DESCENT
# =====================================================

weights = np.zeros(
    X_train.shape[1]
)

learning_rate = 0.01

iterations = 20000

n = len(y_train)


for i in range(iterations):

    predictions = X_train @ weights

    error = predictions - y_train

    gradient = (2 / n) * (
        X_train.T @ error
    )

    weights = weights - (
        learning_rate * gradient
    )


# =====================================================
# 20. TEST PREDICTION
# =====================================================

y_pred = X_test @ weights


# =====================================================
# 21. EVALUATION
# =====================================================

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


print("\n================================")
print("MODEL EVALUATION")
print("================================")

print("MSE  :", mse)

print("MAE  :", mae)

print("RMSE :", rmse)

print("R2   :", r2)


# =====================================================
# 22. USER INPUT
# =====================================================

print("\n================================")
print("HOUSE PRICE PREDICTION")
print("================================")


marla = float(
    input("Enter Area in Marla: ")
)

bedrooms = float(
    input("Enter Bedrooms: ")
)

bathrooms = float(
    input("Enter Bathrooms: ")
)

floors = float(
    input("Enter Floors: ")
)

year_built = float(
    input("Enter Year Built: ")
)

garage = float(
    input("Enter Garage: ")
)


# =====================================================
# 23. CITY SELECTION
# =====================================================

print("\nAvailable Cities:")

cities = list(city_le.classes_)

for i, value in enumerate(cities):

    print(i, "-", value)


city_number = int(
    input("Select City Number: ")
)

city = cities[city_number]


# =====================================================
# 24. LOCATION SELECTION
# =====================================================

print("\nAvailable Locations:")

locations = list(location_le.classes_)

for i, value in enumerate(locations):

    print(i, "-", value)


location_number = int(
    input("Select Location Number: ")
)

location = locations[location_number]


# =====================================================
# 25. CONDITION SELECTION
# =====================================================

print("\nAvailable Conditions:")

conditions = list(condition_le.classes_)

for i, value in enumerate(conditions):

    print(i, "-", value)


condition_number = int(
    input("Select Condition Number: ")
)

condition = conditions[condition_number]


# =====================================================
# 26. PROPERTY TYPE SELECTION
# =====================================================

print("\nAvailable Property Types:")

property_types = list(
    property_type_le.classes_
)

for i, value in enumerate(property_types):

    print(i, "-", value)


property_type_number = int(
    input("Select Property Type Number: ")
)

property_type = property_types[
    property_type_number
]


# =====================================================
# 27. FURNISHED
# =====================================================

print("\nFurnished:")

print("0 - no")

print("1 - yes")


furnished_number = int(
    input("Select Furnished: ")
)


if furnished_number == 1:

    furnished = "yes"

else:

    furnished = "no"


# =====================================================
# 28. CORNER PROPERTY
# =====================================================

print("\nCorner Property:")

print("0 - no")

print("1 - yes")


corner_number = int(
    input("Select Corner Property: ")
)


if corner_number == 1:

    corner_property = "yes"

else:

    corner_property = "no"


# =====================================================
# 29. PARK FACING
# =====================================================

print("\nPark Facing:")

print("0 - no")

print("1 - yes")


park_number = int(
    input("Select Park Facing: ")
)


if park_number == 1:

    park_facing = "yes"

else:

    park_facing = "no"


# =====================================================
# 30. ENCODE USER INPUT
# =====================================================

city_encoded = city_le.transform(
    [city]
)[0]


location_encoded = location_le.transform(
    [location]
)[0]


condition_encoded = condition_le.transform(
    [condition]
)[0]


property_type_encoded = property_type_le.transform(
    [property_type]
)[0]


furnished_encoded = furnished_le.transform(
    [furnished]
)[0]


corner_encoded = corner_le.transform(
    [corner_property]
)[0]


park_encoded = park_le.transform(
    [park_facing]
)[0]


# =====================================================
# 31. CREATE NEW HOUSE
# =====================================================

new_house = np.array([[
    marla,
    bedrooms,
    bathrooms,
    floors,
    year_built,
    garage,
    city_encoded,
    location_encoded,
    condition_encoded,
    property_type_encoded,
    furnished_encoded,
    corner_encoded,
    park_encoded
]])


# =====================================================
# 32. SCALE NEW HOUSE
# =====================================================

new_house = scaler.transform(
    new_house
)


# =====================================================
# 33. ADD BIAS
# =====================================================

new_house = np.c_[
    np.ones(new_house.shape[0]),
    new_house
]


# =====================================================
# 34. PREDICT PRICE
# =====================================================

predicted_price = new_house @ weights


# =====================================================
# 35. FINAL RESULT
# =====================================================

print("\n================================")
print("PREDICTED HOUSE PRICE")
print("================================")

print(
    "Predicted Price:",
    round(predicted_price[0], 2),
    "PKR"
)