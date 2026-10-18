# # Guassian Naive Bayes

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import GaussianNB
# from sklearn.metrics import accuracy_score, confusion_matrix

# df = pd.read_csv('students_week5.csv')
# X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
# y = df['result']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# model = GaussianNB()
# model.fit(X_train, y_train)
# pred = model.predict(X_test)
# print('Accuracy:', accuracy_score(y_test, pred))
# print(confusion_matrix(y_test, pred))

# new_student = X_test.iloc[[0]]
# print('Pass Probability:', model.predict_proba(new_student)[0][1].round(2))

# All 4 Classifiers Head to Head

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv('students_week5.csv')
X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y = df['result']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

models = {'Logistic Regression': LogisticRegression(max_iter=1000),
          'SVM (RBF)': SVC(), 'KNN (k=5)': KNeighborsClassifier(5),
          'Naive Bayes': GaussianNB()}
for name, m in models.items():
    pipe = make_pipeline(StandardScaler(), m).fit(X_train, y_train)
    print(f'{name:20s} Accuracy = {pipe.score(X_test, y_test):.3f}')

# Helper repeated in each section: fit, predict, then report every requested metric.

# ==========================================
# Naive Bayes
# ==========================================
# model = MultinomialNB()
# model.fit(X_train, y_train)
# prediction = model.predict(X_test)
# accuracy = accuracy_score(y_test, prediction)
# precision = precision_score(y_test, prediction, zero_division=0)
# recall = recall_score(y_test, prediction, zero_division=0)
# f1 = f1_score(y_test, prediction, zero_division=0)
# results.append(("Naive Bayes", accuracy, precision, recall, f1))
# print("\nNaive Bayes Results")
# print(f"Accuracy: {accuracy:.2%}")
# print(f"Precision: {precision:.2%}")
# print(f"Recall: {recall:.2%}")
# print(f"F1-score: {f1:.2%}")
# print("Confusion Matrix:\n", confusion_matrix(y_test, prediction))
# print(classification_report(y_test, prediction, target_names=["ham", "spam"], zero_division=0))
