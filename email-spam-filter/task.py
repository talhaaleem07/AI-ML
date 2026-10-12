import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# Load and inspect the dataset.
data = pd.read_csv("Spam.csv")
print("Shape:", data.shape)
print("\nHead:")
print(data.head())
print("\nInfo:")
data.info()
print("\nColumns:", data.columns.tolist())
print("\nMissing values:", data.isnull().sum().sum())
print("Duplicate rows:", data.duplicated().sum())
print("Text column: none; all input columns are precomputed numeric features.")
print("Target column: spam (0 = ham, 1 = spam)")
print("\nTarget distribution:")
print(data["spam"].value_counts(dropna=False))

# Remove missing values and duplicate rows; keep the numeric predictors and valid labels.
data = data.dropna().drop_duplicates()
data["spam"] = pd.to_numeric(data["spam"], errors="coerce")
data = data.dropna(subset=["spam"])
data = data[data["spam"].isin([0, 1])]
data["spam"] = data["spam"].astype(int)
X = data.drop(columns=["spam"])
y = data["spam"]
print("\nRows after cleaning:", len(data))
print("Class distribution after cleaning:")
print(y.value_counts())

# Hold out a stratified test set, as requested.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Store each model's measured test scores for the comparison at the end.
results = []

# ==========================================
# Logistic Regression
# ==========================================
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)
prediction = model.predict(X_test)
accuracy = accuracy_score(y_test, prediction)
precision = precision_score(y_test, prediction, zero_division=0)
recall = recall_score(y_test, prediction, zero_division=0)
f1 = f1_score(y_test, prediction, zero_division=0)
results.append(("Logistic Regression", accuracy, precision, recall, f1))
print("\nLogistic Regression Results")
print(f"Accuracy: {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall: {recall:.2%}")
print(f"F1-score: {f1:.2%}")
print("Confusion Matrix:\n", confusion_matrix(y_test, prediction))
print(classification_report(y_test, prediction, target_names=["ham", "spam"], zero_division=0))

# ==========================================
# Support Vector Machine (SVM)
# ==========================================
model = SVC()
model.fit(X_train, y_train)
prediction = model.predict(X_test)
accuracy = accuracy_score(y_test, prediction)
precision = precision_score(y_test, prediction, zero_division=0)
recall = recall_score(y_test, prediction, zero_division=0)
f1 = f1_score(y_test, prediction, zero_division=0)
results.append(("SVM", accuracy, precision, recall, f1))
print("\nSVM Results")
print(f"Accuracy: {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall: {recall:.2%}")
print(f"F1-score: {f1:.2%}")
print("Confusion Matrix:\n", confusion_matrix(y_test, prediction))
print(classification_report(y_test, prediction, target_names=["ham", "spam"], zero_division=0))

# ==========================================
# K-Nearest Neighbors
# ==========================================
model = KNeighborsClassifier()
model.fit(X_train, y_train)
prediction = model.predict(X_test)
accuracy = accuracy_score(y_test, prediction)
precision = precision_score(y_test, prediction, zero_division=0)
recall = recall_score(y_test, prediction, zero_division=0)
f1 = f1_score(y_test, prediction, zero_division=0)
results.append(("KNN", accuracy, precision, recall, f1))
print("\nKNN Results")
print(f"Accuracy: {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall: {recall:.2%}")
print(f"F1-score: {f1:.2%}")
print("Confusion Matrix:\n", confusion_matrix(y_test, prediction))
print(classification_report(y_test, prediction, target_names=["ham", "spam"], zero_division=0))

# ==========================================
# Gaussian Naive Bayes
# ==========================================
model = GaussianNB()
model.fit(X_train, y_train)
prediction = model.predict(X_test)
accuracy = accuracy_score(y_test, prediction)
precision = precision_score(y_test, prediction, zero_division=0)
recall = recall_score(y_test, prediction, zero_division=0)
f1 = f1_score(y_test, prediction, zero_division=0)
results.append(("Gaussian Naive Bayes", accuracy, precision, recall, f1))
print("\nGaussian Naive Bayes Results")
print(f"Accuracy: {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall: {recall:.2%}")
print(f"F1-score: {f1:.2%}")
print("Confusion Matrix:\n", confusion_matrix(y_test, prediction))
print(classification_report(y_test, prediction, target_names=["ham", "spam"], zero_division=0))

# Print a comparison based on the actual held-out test predictions.
print("\nModel Comparison")
print(f"{'Model':<24} {'Accuracy':>10} {'Precision':>11} {'Recall':>9} {'F1':>9}")
print("-" * 67)
for name, accuracy, precision, recall, f1 in results:
    print(f"{name:<24} {accuracy:>9.2%} {precision:>10.2%} {recall:>8.2%} {f1:>8.2%}")
best = max(results, key=lambda row: row[1])
print(f"\nBest model: {best[0]} ({best[1]:.2%} accuracy)")
print("Above 90% accuracy:", "yes" if best[1] > 0.90 else "no")
