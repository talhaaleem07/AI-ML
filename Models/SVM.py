# Support Vector Machine (SVM)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

df = pd.read_csv('students_week5.csv')
X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
Y = df['result']
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42, stratify=Y)

scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

for kernel in ['linear', 'rbf']:
    model = SVC(kernel=kernel, C=1.0)
    model.fit(X_train, Y_train)
    acc = accuracy_score(Y_test, model.predict(X_test))
    print(f'SVM ({kernel}): Accuracy: {acc:.3f}')
