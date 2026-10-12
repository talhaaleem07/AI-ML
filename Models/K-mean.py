# K-means Clustering

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('students_week5.csv')

X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
Y = df['result']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42, stratify=Y)

# without scaling first -- then with scaling

raw = KNeighborsClassifier(n_neighbors=5).fit(X_train, Y_train)
print(f'KNN without scaling:', accuracy_score(Y_test, raw.predict(X_test)))
scalar = StandardScaler()
X_train_s, X_test_s = scalar.fit_transform(X_train), scalar.transform(X_test)

for k in [1, 3, 5, 7, 9, 15, 25]:
    Knn = KNeighborsClassifier(n_neighbors=k).fit(X_train_s, Y_train)
    acc = accuracy_score(Y_test, Knn.predict(X_test_s))
    print(f'k={k:>2}: Accuracy = {acc:.3f}')
