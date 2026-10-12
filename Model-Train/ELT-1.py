import numpy as np
import pandas as pd


# 1. EXTRACT

df = pd.read_csv("pakistan house prediction dataset.csv")

print("=" * 50)
print("EXTRACT")
print("=" * 50)

print("Original Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())


# 2. TRANSFORM

print("\n" + "=" * 50)
print("TRANSFORM")
print("=" * 50)


# Remove duplicate rows

df = df.drop_duplicates().reset_index(drop=True)

print("\nShape After Removing Duplicates:", df.shape)


# Remove unnecessary ID column

if "ID" in df.columns:
    df = df.drop(columns=["ID"])


# Area Cleaning

df["Area_SqFt"] = (
    df["Area_SqFt"]
    .astype("string")
    .str.replace(",", "", regex=False)
    .str.extract(r"(\d+(?:\.\d+)?)", expand=False)
)

df["Area_SqFt"] = pd.to_numeric(
    df["Area_SqFt"],
    errors="coerce"
)


# Price Cleaning

df["Price_PKR"] = (
    df["Price_PKR"]
    .astype("string")
    .str.replace(",", "", regex=False)
    .str.extract(r"(\d+(?:\.\d+)?)", expand=False)
)

df["Price_PKR"] = pd.to_numeric(
    df["Price_PKR"],
    errors="coerce"
)


# Year Cleaning

df["Year_Built"] = (
    df["Year_Built"]
    .astype("string")
    .str.extract(r"(\d{4})", expand=False)
)

df["Year_Built"] = pd.to_numeric(
    df["Year_Built"],
    errors="coerce"
)


# Numeric Columns

numeric_columns = [
    "Bedrooms",
    "Bathrooms",
    "Floors",
    "Garage"
]

for column in numeric_columns:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# Text Columns Cleaning

text_columns = [
    "City",
    "Location",
    "Condition",
    "Property_Type",
    "Furnished",
    "Corner_Property",
    "Park_Facing"
]

for column in text_columns:

    df[column] = (
        df[column]
        .astype("string")
        .str.strip()
        .str.lower()
    )


# Missing Values


numeric_columns = [
    "Area_SqFt",
    "Year_Built",
    "Price_PKR",
    "Bedrooms",
    "Bathrooms",
    "Floors",
    "Garage"
]

for column in numeric_columns:

    df[column] = df[column].fillna(
        df[column].median()
    )



for column in text_columns:

    df[column] = df[column].fillna("unknown")


# Feature Engineering

# Convert Square Feet to Marla
# 1 Marla = 272.25 SqFt

df["Area_Marla"] = (
    df["Area_SqFt"] / 272.25
)


# Calculate Price per Marla

df["Price_Per_Marla"] = (
    df["Price_PKR"] /
    df["Area_Marla"]
)


# Remove invalid values

df = df[
    (df["Area_SqFt"] > 0) &
    (df["Price_PKR"] > 0) &
    (df["Area_Marla"] > 0)
]



# Round calculated columns

df["Area_Marla"] = df["Area_Marla"].round(2)

df["Price_Per_Marla"] = (
    df["Price_Per_Marla"].round(2)
)


# Final Transform Check

print("\nData After Transformation:")
print(df.head(20))

print("\nShape After Transformation:")
print(df.shape)

print("\nMissing Values After Transformation:")
print(df.isnull().sum())



# 3. LOAD


output_file = "cleaned_pakistan_house_dataset.csv"

df.to_csv(
    output_file,
    index=False
)

print("\nCleaned dataset saved as:")
print(output_file)



# FINAL CHECK


print("\nFinal Shape:")
print(df.shape)

print("\nFinal Columns:")
print(df.columns.tolist())

print("\nFinal Missing Values:")
print(df.isnull().sum())

print("\nTotal Duplicate Rows:")
print(df.duplicated().sum())

print("\nETL completed successfully!")