import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

URL = "https://raw.githubusercontent.com/MSc-AI/SpamEmail/main/spam_ham_dataset.csv"

df = pd.read_csv(URL)[["text", "label_num"]]      # label_num: 1 = spam, 0 = ham
df = df.dropna().drop_duplicates()
print("Emails after removing empty/duplicate rows:", len(df))
print(df["label_num"].value_counts().rename({0: "ham", 1: "spam"}), "\n")

def clean(text):
    text = text.lower()
    text = re.sub(r"^subject:", " ", text)              # drop the 'Subject:' header word
    text = re.sub(r"http\S+|www\.\S+", " url ", text)    # links -> 'url'
    text = re.sub(r"\S+@\S+", " emailaddr ", text)       # addresses -> 'emailaddr'
    text = re.sub(r"\d+", " num ", text)                 # numbers -> 'num'
    text = re.sub(r"[^a-z\s]", " ", text)                # remove punctuation/symbols
    return re.sub(r"\s+", " ", text).strip()

df["clean"] = df["text"].apply(clean)

X_train, X_test, y_train, y_test = train_test_split(
    df["clean"], df["label_num"], test_size=0.2, random_state=42, stratify=df["label_num"]
)

def tfidf():
    # unigrams + bigrams, ignore very rare words and common English stop-words
    return TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=2, sublinear_tf=True)

models = {
    "SVM (LinearSVC)":        Pipeline([("tfidf", tfidf()), ("clf", LinearSVC(C=1.0))]),
    "Naive Bayes (Multinom)": Pipeline([("tfidf", tfidf()), ("clf", MultinomialNB(alpha=0.1))]),
}

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("=" * 55)
    print(f"{name}   ->   Accuracy: {accuracy_score(y_test, pred) * 100:.2f}%")
    print(classification_report(y_test, pred, target_names=["ham", "spam"], digits=4))
    print("Confusion matrix [rows=true, cols=pred]:\n", confusion_matrix(y_test, pred))

best = models["SVM (LinearSVC)"]
samples = [
    "Congratulations!! You won a FREE $1000 gift card. Click http://win-now.biz to claim",
    "Hi team, attached is the gas meter flow report for Monday. Please review before the call",
]
for s, p in zip(samples, best.predict([clean(s) for s in samples])):
    print(f"\n[{'SPAM' if p else 'HAM'}] {s[:70]}...")