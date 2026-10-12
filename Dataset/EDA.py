# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt

# df = sns.load_dataset('tips')
# print(df)

# print(df.shape)
# print(df.head())
# print(df.dtypes)

# print(df.describe())

# print(df['day'].value_counts())

# sns.histplot(df['total_bill'])
# plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

# print(df)
# print(df.shape)
# print(df.head())
# print(df.dtypes)

# print(df.describe())

# print(df['day'].value_counts())

# sns.histplot(df['total_bill'], bins=20, kde=True)
# plt.title('Distribution of Total Bill')
# plt.show()

# p = df.groupby('day')['total_bill'].mean()
# print(p)
# print(p.max())

# df.plot(kind = 'scatter', x = 'total_bill', y = 'tip')
# plt.show()

# sns.scatterplot(x='total_bill', y='tip', data=df)
# plt.show()

# a = df[['total_bill', 'tip', 'size']]
# sns.heatmap(a.corr(), annot=True, cmap='coolwarm')
# plt.show()

df = pd.read_csv('Books_Data_Clean.csv')
print(df)