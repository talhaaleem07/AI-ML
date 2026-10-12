# Polynomial Regression

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

df = pd.read_csv('students_week5.csv')
X = df.drop(columns = ['student_id', 'final_score', 'result', 'performance'])
Y = df['final_score']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 42)

for degree in [1,2,3]:
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X_train, Y_train)
    train_r2 = r2_score(Y_train, model.predict(X_train))
    test_r2 = r2_score(Y_test, model.predict(X_test))
    print(f'Degree{degree}:, train R2 = {train_r2:.3f} | test R2 = {test_r2:.3f}')
