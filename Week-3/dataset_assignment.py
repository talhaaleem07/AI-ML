from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

csv_path = Path(__file__).resolve().parent / 'Books_Data_Clean.csv'
df = pd.read_csv(csv_path)

print(df)
print('Shape:', df.shape)
print('\nFirst 5 rows:')
print(df.head())
print('\nData types:')
print(df.dtypes)
print('\nSummary statistics:')
print(df.describe())
print('\nGenre counts:')
print(df['genre'].value_counts())

sns.histplot(df['Book_average_rating'], bins=20, kde=True)
plt.title('Distribution of Book Average Rating')
plt.show()

book_rating_by_genre = df.groupby('genre')['Book_average_rating'].mean().sort_values(ascending=False)
print('\nAverage book rating by genre:')
print(book_rating_by_genre)
print('\nHighest average rating:', book_rating_by_genre.max())

df.plot(kind='scatter', x='Book_average_rating', y='sale price')
plt.title('Book Average Rating vs Sale Price')
plt.show()

sns.scatterplot(x='Book_average_rating', y='sale price', data=df)
plt.title('Book Average Rating vs Sale Price')
plt.show()

numeric_columns = df[['Book_average_rating', 'Book_ratings_count', 'gross sales', 'publisher revenue', 'sale price', 'units sold']]
sns.heatmap(numeric_columns.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
