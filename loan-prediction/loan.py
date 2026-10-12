import warnings

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import RepeatedStratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

warnings.filterwarnings('ignore')

# 1. Data load

df = pd.read_csv('loan_data_set.csv').drop(columns=['Loan_ID'])
y = df.pop('Loan_Status').map({'Y': 1, 'N': 0})

def add_features(data):
    data = data.copy()
    income = data['ApplicantIncome'] + data['CoapplicantIncome']
    emi = data['LoanAmount'] * 1000 / data['Loan_Amount_Term']   # LoanAmount hazaaron me hai
    data['TotalIncome'] = income
    data['EMI'] = emi
    data['IncomeAfterEMI'] = income - emi
    data['LoanToIncome'] = data['LoanAmount'] * 1000 / income
    return data

X = add_features(df)

# 2. Model

# Pipeline: missing values bharna + text ko numbers me badalna + Random Forest.
# Ye sab train data se seekhta hai, is liye test data ki information leak nahi hoti.
text_cols = X.select_dtypes(exclude='number').columns
num_cols = X.select_dtypes(include='number').columns

preprocess = ColumnTransformer([
    ('num', SimpleImputer(strategy='median'), num_cols),
    ('cat', Pipeline([
        ('fill', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore')),
    ]), text_cols),
])

model = Pipeline([
    ('prep', preprocess),
    ('forest', RandomForestClassifier(
        n_estimators=300,
        max_depth=5,          # chhota dataset hai, deep trees overfit karte hain
        min_samples_leaf=5,
        random_state=42,
    )),
])

# 3. Accuracy

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
model.fit(X_train, y_train)
print('Test accuracy (20% data):', round(model.score(X_test, y_test), 3))

# Ek split lucky/unlucky ho sakta hai, is liye 5-fold x 5 baar bhi check karte hain
cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=5, random_state=42)
scores = cross_val_score(model, X, y, cv=cv)
print(f'Cross-validation accuracy: {scores.mean():.3f} (+/- {scores.std():.3f})')

model.fit(X, y)   # final model poore data par train

importances = pd.Series(
    model.named_steps['forest'].feature_importances_,
    index=model.named_steps['prep'].get_feature_names_out(),
)
print('\nTop 8 Feature Importance:')
print(importances.sort_values(ascending=False).head(8).round(3))


# 4. Customer se sawal

def ask(question, options):
    """Sahi option milne tak dobara poochta hai (capital/space ka farq nahi parta)."""
    lookup = {option.lower(): option for option in options}
    while True:
        answer = input(f'{question} ({"/".join(options)}): ').strip().lower()
        if answer in lookup:
            return lookup[answer]
        print('  Galat input, dobara try karein.')

def ask_number(question, minimum=0):
    while True:
        try:
            value = float(input(f'{question}: '))
            if value >= minimum:
                return value
        except ValueError:
            pass
        print(f'  Sahi number likhein (>= {minimum}).')

print('\n--- Loan Eligibility ---')

customer = pd.DataFrame([{
    'Gender': ask('Gender', ['Male', 'Female']),
    'Married': ask('Married', ['Yes', 'No']),
    'Dependents': ask('Dependents', ['0', '1', '2', '3+']),
    'Education': ask('Education', ['Graduate', 'Not Graduate']),
    'Self_Employed': ask('Self Employed', ['Yes', 'No']),
    'ApplicantIncome': ask_number('Applicant monthly income'),
    'CoapplicantIncome': ask_number('Coapplicant monthly income'),
    'LoanAmount': ask_number('Loan amount in THOUSANDS (150 = 150,000)', minimum=1),
    'Loan_Amount_Term': ask_number('Loan term in months (e.g. 360)', minimum=1),
    'Credit_History': float(ask('Credit history (1 = Good, 0 = Bad)', ['1', '0'])),
    'Property_Area': ask('Property area', ['Urban', 'Semiurban', 'Rural']),
}])

if customer['ApplicantIncome'][0] + customer['CoapplicantIncome'][0] == 0:
    raise SystemExit('Total income 0 se zyada honi chahiye.')

# 5. Prediction

customer = add_features(customer)[X.columns]
chance = model.predict_proba(customer)[0, 1]

if chance >= 0.5:
    print(f'\n✅ Customer is eligible for the loan (approval chance: {chance:.0%})')
else:
    print(f'\n❌ Customer is not eligible for the loan (approval chance: {chance:.0%})')


