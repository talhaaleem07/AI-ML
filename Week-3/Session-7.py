import pandas as pd

# Introduction to Pandas and Creating DataFrame

# data = {'name': ['Ali', 'Sara', 'Zain'],
#         'marks':[85, 92, 78]}
# df = pd.DataFrame(data)
# print(df)


# data = {'name': ['Ali', 'Sara', 'Zain'],
#         'city': ['Lahore', 'Islamabad', 'Karachi'],
#         'score':[85, 92, 78]}
# df = pd.DataFrame(data)
# print(df)

# Series vs DataFrame
# A series is a single labled column of data
# A Dataframe is a collection of series

# s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# print(s)

# df = pd.DataFrame({'name':['Ali', 'Sara'], 'marks':[85, 92]})
# print(df['name'])

# c = pd.Series(['Lahore', 'Islamabad', 'Karachi', 'Peshawar', 'Multan'], index=['c1', 'c2', 'c3', 'c4', 'c5'])
# print(c)

# df = pd.DataFrame({'name':['Ali', 'Sara'], 'age':[20, 21]})
# # age_column = df['age']
# # print(type(age_column))
# print(df['age'])

# Selection and indexing(columns, conditionals)

# df = pd.DataFrame({'name':['Ali', 'Sara'], 'marks':[85, 92]})
# print(df[df['marks']>90])

# df = pd.DataFrame({'name':['Ali', 'Sara', 'Talha', 'Zain', 'Tayyab'], 'marks':[85, 92, 60, 76, 70]})
# print(df[df['marks']>75])

# selected_columns = df[['name', 'marks']]
# print(selected_columns)
# print(df[['name', 'marks']])

# DataFrame Operations (Sort, Unique, Apply)

# df = pd.DataFrame({'name':['Ali', 'Sara', 'Talha', 'Zain', 'Tayyab'], 'marks':[85, 92, 60, 76, 70]})

# df['grade'] = df['marks'].apply(lambda x: 'Pass' if x>=80 else 'Fail')
# print(df.sort_values('marks', ascending=False))

# df = pd.DataFrame({'name':['Ali', 'Sara', 'Talha', 'Zain', 'Tayyab'], 'marks':[85, 92, 60, 76, 70]})

# df['grade'] = df['marks'].apply(lambda x: 'High' if x>=80 else 'Low')
# print(df.sort_values('marks', ascending=False))

# print(df.value_counts('grade'))

# Handling Missing Data

# df = pd.DataFrame({'a': [1, 2, None], 'b': [4, None, 6]})
# print(df.isnull())
# print(df.fillna(0))
# print(df.dropna())

# # df = pd.DataFrame({'a': [3, 2, None], 'b': [4, None, 5]})
# # print(df.isnull())

# GroupBy
# sales = pd.DataFrame({'dept': ['IT', 'IT', 'HR', 'HR'], 'sales': [100, 150, 80, 90]})
# print(sales.groupby('dept')['sales'].sum())

# product = pd.DataFrame({'category':[], 'price':[]})
# a = (product.groupby('category')['price'])
# print(a.mean())
# print(a.count())

# merging and concatination ?

# a = pd.DataFrame({'id':[1,2,3],'name':['', '', '']})
# b = pd.DataFrame({'id':[1,2,4],'marks':[85, ]})
# print(pd.merge(a, b, on ='id', how='inner'))


import matplotlib.pyplot as plt

# 1. Prepare the data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 2. Create the plot
plt.plot(x, y)

# 3. Add labels and a title (optional but recommended)
plt.title("Simple Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# 4. Display the chart
plt.show()
