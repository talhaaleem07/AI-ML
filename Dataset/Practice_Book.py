import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.read_csv("Books_Data_Clean.csv")

# Round 1

# How Many Rows and Columns in the Dataset

print(df.shape)

# Which Column has missing values, and how many are missing in each

print(df.isnull().sum())

# What is the Average (mean) Book_average_rating across all books

print(df['Book_average_rating'].mean())

# What is the total gross sales across all 1070 books (sum, not average)

print(df['gross sales'].sum())

# Which genre appears most frequently in the dataset

print(df['genre'].value_counts())

# Which publisher has the highest total units sold

print(df.groupby('Publisher ')['units sold'].sum())

# Find the correlation between 'gross sales' and 'publisher revenue' is it strong or weak

print(df['gross sales'].corr(df['publisher revenue']))

# 

# Sort the dataset by 'Publishing Year' from smallest to largest. Do you notice anything unusual about the smallest values? investigate those rows what books are they

df_sorted = df.sort_values("Publishing Year")
min_year = df_sorted["Publishing Year"].min()
oldest_books = df_sorted[df_sorted["Publishing Year"] == min_year]

print("\nSmallest publishing year:", min_year)
print("\nBooks with the smallest publishing year:")
print(oldest_books)

# Round 2

# Handle the missing values you found in round 1 (Book Name, language_code,publishing Year). Decide a strategy for each columns and justify it in a comment

df["Book Name"] = df["Book Name"].fillna("Unknown")

df["language_code"] = df["language_code"].fillna("Unknown")

df["Publishing Year"] = df["Publishing Year"].fillna(
    df["Publishing Year"].median()
)

print("Missing values after handling:")
print(df[["Book Name", "language_code", "Publishing Year"]].isnull().sum())

# The 'genre' column has 4 categories. Apply One-Hot Encoding to it and print the result

genre_encoded = pd.get_dummies(df["genre"], prefix="genre")

print("\nOne-Hot Encoded Genre:")
print(genre_encoded)

# the Author rating column has a natural order:

rating_order = {
    "Novice": 0,
    "Intermediate": 1,
    "Excellent": 2,
    "Famous": 3
}

df["Author_Rating_encoded"] = df["Author_Rating"].map(rating_order)

print("\nAuthor Rating Encoding:")
print(df[["Author_Rating", "Author_Rating_encoded"]])

# Log Transformation

original_skew = df["gross sales"].skew()
print("\nOriginal skewness:", original_skew)
df["gross_sales_log"] = np.log1p(df["gross sales"])
log_skew = df["gross_sales_log"].skew()
print("Skewness after log transform:", log_skew)
if abs(log_skew) < abs(original_skew):
    print("Skewness improved after log transformation.")
else:
    print("Skewness did not improve.")

# StandardScaler

print("\nTransformed mean:")
print(StandardScaler().fit_transform(df[["units sold"]]).flatten().mean())
