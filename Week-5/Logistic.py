# Logistic regression

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# df = pd.read_csv('students_week5.csv')
# X = df.drop(columns = ['student_id', 'final_score', 'result', 'performance'])
# Y = df['result']
# X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 42, stratify=Y)

# scalar = StandardScaler()
# X_train = scalar.fit_transform(X_train)
# X_test = scalar.transform(X_test)

# model = LogisticRegression(max_iter=1000)
# model.fit(X_train, Y_train)
# pred = model.predict(X_test)
# print('Accuracy:', accuracy_score(Y_test, pred))
# print(confusion_matrix(Y_test, pred))
# print(classification_report(Y_test, pred))

# MultiClass: Low / Medium / High

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('students_week5.csv')
X = df.drop(columns = ['student_id', 'final_score', 'result', 'performance'])
Y = df['performance']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 42, stratify=Y)

scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)
print('Accuracy:', accuracy_score(Y_test, model.predict(X_test)))
print(confusion_matrix(Y_test, model.predict(X_test)))
print(model.predict_proba(X_test[:3]).round(2))
