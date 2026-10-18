# # Multivariate Linear Regression

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score

# df = pd.read_csv('Breast Cancer Wisconsin (Diagnostic) Data Set.csv')
# df = df.drop(columns=['id', 'Unnamed: 32'])
# df['diagnosis'] = df['diagnosis'].map({'B': 0, 'M': 1})

# X = df.drop(columns=['diagnosis'])
# Y = df['diagnosis']

# X_train, X_test, Y_train, Y_test = train_test_split(
#     X, Y, test_size=0.2, random_state=42
# )

# model = LinearRegression()
# model.fit(X_train, Y_train)
# Y_pred = model.predict(X_test)
# mse = mean_squared_error(Y_test, Y_pred)
# r2 = r2_score(Y_test, Y_pred)

# print("Mean Squared Error:", mse)
# print("R2 Score:", r2)

# # Polynomial Regression

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model import LinearRegression
# from sklearn.pipeline import make_pipeline
# from sklearn.metrics import mean_squared_error, r2_score

# df = pd.read_csv('Breast Cancer Wisconsin (Diagnostic) Data Set.csv')
# df = df.drop(columns=['id', 'Unnamed: 32'])
# df['diagnosis'] = df['diagnosis'].map({'B': 0, 'M': 1})

# X = df.drop(columns=['diagnosis'])
# Y = df['diagnosis']
# X_train, X_test, Y_train, Y_test = train_test_split(
#     X, Y, test_size=0.2, random_state=42
# )

# model = make_pipeline(
#     PolynomialFeatures(degree=2),
#     LinearRegression()
# )

# model.fit(X_train, Y_train)
# Y_pred = model.predict(X_test)
# mse = mean_squared_error(Y_test, Y_pred)
# r2 = r2_score(Y_test, Y_pred)

# print("Mean Squared Error:", mse)
# print("R2 Score:", r2)

# # Logistic Regression

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import accuracy_score

# df = pd.read_csv('Breast Cancer Wisconsin (Diagnostic) Data Set.csv')
# df = df.drop(columns=['id', 'Unnamed: 32'])
# df['diagnosis'] = df['diagnosis'].map({'B': 0, 'M': 1})

# X = df.drop(columns=['diagnosis'])
# Y = df['diagnosis']
# X_train, X_test, Y_train, Y_test = train_test_split(
#     X, Y, test_size=0.2, random_state=42
# )

# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# model = LogisticRegression(max_iter=1000)
# model.fit(X_train, Y_train)
# Y_pred = model.predict(X_test)
# accuracy = accuracy_score(Y_test, Y_pred)
# print("Accuracy:", accuracy)

# # MultiClass: Low / Medium / High

# import pandas as pd

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import accuracy_score

# df = pd.read_csv('Breast Cancer Wisconsin (Diagnostic) Data Set.csv')
# df = df.drop(columns=['id', 'Unnamed: 32'])
# low = df['radius_mean'].quantile(0.33)
# high = df['radius_mean'].quantile(0.66)
# df['risk_level'] = pd.cut(
#     df['radius_mean'],
#     bins=[-float('inf'), low, high, float('inf')],
#     labels=['Low', 'Medium', 'High']
# )

# X = df.drop(columns=['diagnosis', 'risk_level'])
# Y = df['risk_level']
# X_train, X_test, Y_train, Y_test = train_test_split(
#     X, Y, test_size=0.2, random_state=42
# )

# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# model = LogisticRegression(max_iter=1000)
# model.fit(X_train, Y_train)
# Y_pred = model.predict(X_test)
# accuracy = accuracy_score(Y_test, Y_pred)
# print("Accuracy:", accuracy)


import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge, LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score

# ---------------- Data prep (shared) ----------------
def load_data(path='Titanic-Dataset.csv'):
    df = pd.read_csv(path)

    # Feature engineering
    df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
    df['Title'] = df['Title'].replace(
        {'Mlle': 'Miss', 'Ms': 'Miss', 'Mme': 'Mrs'})
    rare = df['Title'].value_counts()[lambda s: s < 10].index
    df['Title'] = df['Title'].replace(list(rare), 'Rare')

    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    df['TicketGroup'] = df.groupby('Ticket')['Ticket'].transform('count')
    df['HasCabin'] = df['Cabin'].notna().astype(int)
    df['Deck'] = df['Cabin'].str[0].fillna('U')

    # Missing values
    df['Age'] = df['Age'].fillna(df.groupby(['Title', 'Pclass'])['Age'].transform('median'))
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    df['FarePerPerson'] = df['Fare'] / df['TicketGroup']
    df['Fare'] = np.log1p(df['Fare'])
    df['FarePerPerson'] = np.log1p(df['FarePerPerson'])

    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    df['IsChild'] = (df['Age'] < 13).astype(int)

    df = df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])
    df = pd.get_dummies(df, columns=['Embarked', 'Title', 'Deck'], drop_first=True, dtype=int)
    return df

def split(df, target, drop=()):
    X = df.drop(columns=[target, *drop])
    Y = df[target]
    return train_test_split(X, Y, test_size=0.2, random_state=42)

from sklearn.model_selection import RepeatedStratifiedKFold
cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=3, random_state=42)
df = load_data()
LEAN = (['Pclass', 'Sex', 'Age', 'FamilySize', 'IsAlone', 'FarePerPerson', 'HasCabin', 'IsChild']
        + [c for c in df.columns if c.startswith('Title_')])

# ---------------- 1. Multivariate Linear Regression ----------------
X_train, X_test, Y_train, Y_test = split(df, 'Survived')
model = make_pipeline(StandardScaler(), Ridge())
gs = GridSearchCV(model, {'ridge__alpha': np.logspace(-2, 3, 30)}, cv=cv, scoring='r2')
gs.fit(X_train, Y_train)
Y_pred = gs.predict(X_test)
print("=== Multivariate Linear Regression (Ridge) ===")
print("Best params:", gs.best_params_)
print("Mean Squared Error:", mean_squared_error(Y_test, Y_pred))
print("R2 Score:", r2_score(Y_test, Y_pred))
print("Accuracy (threshold 0.5):", accuracy_score(Y_test, (Y_pred >= 0.5).astype(int)))

# ---------------- 2. Polynomial Regression ----------------
model = make_pipeline(StandardScaler(), PolynomialFeatures(degree=2, include_bias=False),
                      StandardScaler(), Ridge())
gs = GridSearchCV(model, {'ridge__alpha': np.logspace(1, 4, 20)}, cv=cv, scoring='r2')
gs.fit(X_train, Y_train)
Y_pred = gs.predict(X_test)
print("\n=== Polynomial Regression (degree 2, Ridge) ===")
print("Best params:", gs.best_params_)
print("Mean Squared Error:", mean_squared_error(Y_test, Y_pred))
print("R2 Score:", r2_score(Y_test, Y_pred))
print("Accuracy (threshold 0.5):", accuracy_score(Y_test, (Y_pred >= 0.5).astype(int)))

# ---------------- 3. Logistic Regression ----------------
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000))
grid = {'logisticregression__C': np.logspace(-3, 2, 20),
        'logisticregression__penalty': ['l1', 'l2'],
        'logisticregression__solver': ['liblinear']}
gs = GridSearchCV(model, grid, cv=cv, scoring='accuracy')
gs.fit(X_train[LEAN], Y_train)
print("\n=== Logistic Regression ===")
print("Best params:", gs.best_params_)
print("Accuracy:", accuracy_score(Y_test, gs.predict(X_test[LEAN])))

# ---------------- 4. MultiClass: Fare tier Low / Medium / High ----------------
mc = df.copy()
mc['FareLevel'] = pd.qcut(np.expm1(mc['Fare']), q=3, labels=['Low', 'Medium', 'High'])
fare_cols = ['Fare', 'FarePerPerson']          # drop target-derived columns (no leakage)
X_train_m, X_test_m, Y_train_m, Y_test_m = split(mc, 'FareLevel', drop=fare_cols)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000))
gs = GridSearchCV(model, {'logisticregression__C': np.logspace(-2, 2, 15)}, cv=cv, scoring='accuracy')
gs.fit(X_train_m, Y_train_m)
print("\n=== MultiClass Logistic Regression (Low/Medium/High fare) ===")
print("Best params:", gs.best_params_)
print("Accuracy:", accuracy_score(Y_test_m, gs.predict(X_test_m)))

# ---------------- 5. SVM ----------------
model = make_pipeline(StandardScaler(), SVC())
grid = {'svc__C': [0.5, 1, 2, 5, 10],
        'svc__gamma': ['scale', 0.01, 0.03, 0.1]}
gs = GridSearchCV(model, grid, cv=cv, scoring='accuracy', n_jobs=-1)
gs.fit(X_train[LEAN], Y_train)
print("\n=== SVM ===")
print("Best params:", gs.best_params_, "| CV acc: %.4f" % gs.best_score_)
print("Accuracy:", accuracy_score(Y_test, gs.predict(X_test[LEAN])))

# ---------------- 6. KNN ----------------
model = make_pipeline(StandardScaler(), KNeighborsClassifier())
grid = {'kneighborsclassifier__n_neighbors': list(range(3, 26, 2)),
        'kneighborsclassifier__weights': ['uniform', 'distance']}
gs = GridSearchCV(model, grid, cv=cv, scoring='accuracy', n_jobs=-1)
gs.fit(X_train, Y_train)
print("\n=== KNN ===")
print("Best params:", gs.best_params_, "| CV acc: %.4f" % gs.best_score_)
print("Accuracy:", accuracy_score(Y_test, gs.predict(X_test)))