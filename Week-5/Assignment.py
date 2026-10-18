# # Multivariate Linear Regression

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# import numpy as np

# df = pd.read_csv('clean_house_price_dataset.csv')

# X = df.drop(columns=['Price_PKR'])
# Y = df['Price_PKR']

# X_train, X_test, Y_train, Y_test = train_test_split(
#     X, Y,
#     test_size=0.2,
#     random_state=42
# )

# scalar = StandardScaler()

# X_train = scalar.fit_transform(X_train)
# X_test = scalar.transform(X_test)

# model = LinearRegression()
# model.fit(X_train, Y_train)
# pred = model.predict(X_test)

# print('MAE:', mean_absolute_error(Y_test, pred))
# print('MSE:', mean_squared_error(Y_test, pred))
# print('RMSE:', np.sqrt(mean_squared_error(Y_test, pred)))
# print('R2:', r2_score(Y_test, pred))

# # Polynomial Regression

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler, PolynomialFeatures
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# import numpy as np

# df = pd.read_csv('clean_house_price_dataset.csv')

# X = df.drop(columns=['Price_PKR'])
# Y = df['Price_PKR']

# X_train, X_test, Y_train, Y_test = train_test_split(
#     X, Y,
#     test_size=0.2,
#     random_state=42
# )

# poly = PolynomialFeatures(degree=2)
# X_train = poly.fit_transform(X_train)
# X_test = poly.transform(X_test)
# scalar = StandardScaler()

# X_train = scalar.fit_transform(X_train)
# X_test = scalar.transform(X_test)

# model = LinearRegression()
# model.fit(X_train, Y_train)
# pred = model.predict(X_test)

# print('MAE:', mean_absolute_error(Y_test, pred))
# print('MSE:', mean_squared_error(Y_test, pred))
# print('RMSE:', np.sqrt(mean_squared_error(Y_test, pred)))
# print('R2:', r2_score(Y_test, pred))

# # Logistic Regression

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# df = pd.read_csv('clean_house_price_dataset.csv')

# # Create binary target
# median_price = df['Price_PKR'].median()

# df['price_class'] = (df['Price_PKR'] >= median_price).astype(int)

# X = df.drop(columns=['Price_PKR', 'price_class'])
# Y = df['price_class']

# X_train, X_test, Y_train, Y_test = train_test_split(
#     X,
#     Y,
#     test_size=0.2,
#     random_state=42,
#     stratify=Y
# )

# scalar = StandardScaler()

# X_train = scalar.fit_transform(X_train)
# X_test = scalar.transform(X_test)

# model = LogisticRegression(max_iter=1000)
# model.fit(X_train, Y_train)
# pred = model.predict(X_test)

# print('Accuracy:', accuracy_score(Y_test, pred))

# print('\nConfusion Matrix:')
# print(confusion_matrix(Y_test, pred))

# print('\nClassification Report:')
# print(classification_report(Y_test, pred))

# print('\nProbabilities:')
# print(model.predict_proba(X_test[:3]).round(2))

# # MultiClass: Low / Medium / High

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# df = pd.read_csv('clean_house_price_dataset.csv')

# # Create Low / Medium / High categories

# low = df['Price_PKR'].quantile(0.33)
# high = df['Price_PKR'].quantile(0.66)

# def classify_price(price):

#     if price <= low:
#         return 'Low'

#     elif price <= high:
#         return 'Medium'

#     else:
#         return 'High'


# df['performance'] = df['Price_PKR'].apply(classify_price)

# X = df.drop(columns=['Price_PKR', 'performance'])
# Y = df['performance']

# X_train, X_test, Y_train, Y_test = train_test_split(
#     X,
#     Y,
#     test_size=0.2,
#     random_state=42,
#     stratify=Y
# )

# scalar = StandardScaler()

# X_train = scalar.fit_transform(X_train)
# X_test = scalar.transform(X_test)

# model = LogisticRegression(max_iter=1000)
# model.fit(X_train, Y_train)
# pred = model.predict(X_test)

# print('Accuracy:', accuracy_score(Y_test, pred))

# print('\nConfusion Matrix:')
# print(confusion_matrix(Y_test, pred))

# print('\nClassification Report:')
# print(
#     classification_report(
#         Y_test,
#         pred
#     )
# )

# print('\nFirst 3 Predictions:')
# print(pred[:3])

# print('\nPrediction Probabilities:')
# print(
#     model.predict_proba(X_test[:3]).round(2)
# )

# Support Vector Machine (SVM)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

df = pd.read_csv('clean_house_price_dataset.csv')

low = df['Price_PKR'].quantile(0.33)
high = df['Price_PKR'].quantile(0.66)

df['price_class'] = pd.cut(
    df['Price_PKR'],
    bins=[-float('inf'), low, high, float('inf')],
    labels=['Low', 'Medium', 'High']
)

X = df.drop(columns=['Price_PKR', 'price_class'])
Y = df['price_class']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42, stratify=Y
)

scalar = StandardScaler()

X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

for kernel in ['linear', 'rbf']:
    model = SVC(kernel=kernel, C=1.0)
    model.fit(X_train, Y_train)
    pred = model.predict(X_test)
    acc = accuracy_score(Y_test, pred)
    print(f'SVM ({kernel}): Accuracy = {acc:.3f}')

# KNN

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('clean_house_price_dataset.csv')

df['price_class'] = pd.qcut(df['Price_PKR'], 3, labels=['Low', 'Medium', 'High'])

X = df.drop(columns=['Price_PKR', 'price_class'])
Y = df['price_class']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42, stratify=Y)

scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

for k in [1, 3, 5, 7, 9]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, Y_train)
    pred = model.predict(X_test)
    print(f'KNN k={k}: Accuracy = {accuracy_score(Y_test, pred):.3f}')