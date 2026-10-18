import pandas as pd

# Feature Engineering - Creating New Features

# df = pd.DataFrame({'height_cm': [170, 180, 160], 'weight_kg': [65, 80, 55]})
# df['bmi'] = df['weight_kg'] / (df['height_cm'] / 100) ** 2
# print(df)

# df = pd.DataFrame({'price': [170, 180, 160], 'quantity': [65, 80, 55]})
# df['total_cost'] = df['price'] * df['quantity']
# print(df)

# df = pd.DataFrame({'total_income': [170, 180, 160], 'total_expenses': [65, 80, 55]})
# df['saving_rate'] = df['total_income'] / df['total_expenses']
# print(df)

# Feature Selection and Binning

# df = pd.DataFrame({'study_hrs':[1,2,3,4,5], 'sleep_hrs':[8,7,6,8,7], 'marks':[50,55,65,70,85]})
# print(df.corr()['marks'])

# ages = pd.Series([5,17,25,45,68,80])
# print(pd.cut(ages, bins=[0,12,19,59,100], labels=['Child','Teen','Adult','Senior']))

# Compute Correletaion of 3 numeric columns against a target column which feature looks least useful

# ETL Batch vs Stream processing
# OLTP , OLAP IMP
# ETL imp
# How to make ETL scripts


# Automation with SKlearn Pipeline

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([[1],[2],[3],[4],[5],[6],[7],[8]])
y = np.array([40, 45, 52, 60, 68, 75, 82, 90])

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LinearRegression())
])
pipe.fit(x, y)
print(pipe.predict([[9]]))
