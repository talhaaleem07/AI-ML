# Data Cleaning (Duplicates and Outliers)

import pandas as pd
import numpy as np

# df = pd.DataFrame({'name':['Ali', 'Sara', 'Ali'], 'marks':[85, 92, 85]})
# print(df.duplicated())
# print(df.drop_duplicates())

# df = pd.DataFrame({'name':['Ali', 'Sara', 'Ali'], 'marks':[85, 92, 85]})
# print(df.duplicated())
# print(df.drop_duplicates())

# # create a series of 8 numbers including one extreme outlier, and use the IQR method to detect it
# import pandas as pd

# df = pd.DataFrame({'marks':[10, 20, 30, 40, 50, 60, 70, 80]})
# print(df)
# print(df['marks'].describe())

# Data Transmission

# prices = pd.Series([100, 500, 1000, 50000])
# log_prices = np.log(prices)
# print(log_prices)

# prices = pd.Series([10, 5000, 100000, 50000000])
# log_prices = np.log(prices)
# print(log_prices)

# Encoding CAtegorical Variables

# from sklearn.preprocessing import LabelEncoder

# sizes = ['small', 'medium', 'large', 'medium']
# le = LabelEncoder()
# print(le.fit_transform(sizes))

# colors = ['red', 'blue', 'gray', 'green']
# le = LabelEncoder()
# print(le.fit_transform(colors))

# Feature Scaling (Standard and MinMax)

from sklearn.preprocessing import StandardScaler, MinMaxScaler

# vals = np.array([[10], [20], [30], [40], [50]])
# print(StandardScaler().fit_transform(vals).flatten())
# print(MinMaxScaler().fit_transform(vals).flatten())

vals = np.array([[10], [20], [30], [40], [50]])
print(StandardScaler().fit_transform(vals).flatten())
print(StandardScaler().fit_transform(vals).flatten().mean())
print(MinMaxScaler().fit_transform(vals).flatten())
