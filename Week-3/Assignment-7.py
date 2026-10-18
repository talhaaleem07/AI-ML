import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# # Remaining 
# # Merging and Concatination

# a = pd.DataFrame({'id':[1,2,3],'name':['Ali','Sara','Zain']})
# b = pd.DataFrame({'id':[1,2,4],'marks':[85,92,70]})

# print(pd.merge(a, b, on='id', how='inner'))
# print(pd.merge(a, b, on='id', how='right'))
# print(pd.merge(a, b, on='id', how='left'))
# print(pd.merge(a, b, on='id', how='outer'))

# combined_df = pd.concat([a, b], ignore_index=True)
# print(combined_df)

# # Pandas Plotting

# # df = pd.DataFrame({'dept':['IT', 'HR', 'Sales'], 'revenue':[250, 170, 300]})
# # df.plot(x = 'dept', y = 'revenue', kind = 'bar')
# # plt.show()

# # df = pd.DataFrame({'dept':['IT', 'HR', 'Sales'], 'sales':[250, 170, 300]})
# # df.plot(x = 'dept', y = 'sales', kind = 'line')
# # plt.show()

# # df.plot(x = 'dept', y = 'sales', kind = 'bar')
# # plt.show()

# # Seaborn: Distribution & Categorical Plots

# # df = pd.DataFrame({'dept':['IT','IT','HR','HR'], 'salary':[80,95,60,65]})
# # sns.boxplot(x='dept', y='salary', data=df)
# # plt.show()

# # df = pd.DataFrame({'exam_scores':[85, 92, 60, 76, 70]})
# # sns.histplot(x='exam_scores', data=df)
# # plt.show()

# # Seaborn: Heatmap (Matrix Plots)

# # df = pd.DataFrame({'age':[20, 25, 30, 35], 'income':[30, 45, 55, 65], 'score':[70, 75, 80, 85]})
# # sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
# # plt.show()

# # df = pd.DataFrame({'age':[20, 25, 30, 35], 'income':[30, 45, 55, 65], 'score':[70, 75, 80, 85], 'marks':[85, 92, 60, 76]})
# # sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
# # plt.show()

# # df = pd.DataFrame({'age':[20, 25, 30, 35], 'income':[30, 45, 55, 65], 'score':[70, 75, 80, 85], 'marks':[85, 92, 60, 76]})
# # sns.heatmap(df.corr())
# # plt.show()

# # Task
# # Pandas Series

# a = [1, 7, 2]
# myvar = pd.Series(a, index = ["x", "y", "z"])
# print(myvar)

# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories, index = ["day1", "day2"])
# print(myvar)

# # Pandas DataFrames

# data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
# myvar = pd.DataFrame(data)
# print(myvar)
# print(myvar.loc[[0, 1]])

# data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print(df) 

# # Pandas Read CSV

# df = pd.read_csv('data.csv')
# print(df.to_string()) 

# # Pandas - Analyzing DataFrames

# df = pd.read_csv('data.csv')
# print(df.head(10))
# print(df.head())
# print(df.tail(10))
# print(df.tail())

