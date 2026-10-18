# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier, export_text

# df = pd.read_csv("students_week5.csv")
# X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
# y = df['result']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# for depth in [3, None]:
#     tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
#     tree.fit(X_train, y_train)
#     print(f"max_depth={depth}: train = {tree.score(X_train, y_train):.3f}, f' | test = {tree.score(X_test, y_test):.3f}")

# small = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X_train, y_train)
# print(export_text(small, feature_names=list(X.columns)))

# Random forest

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('students_week5.csv')
X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
Y = df['result']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)
forest = RandomForestClassifier(n_estimators=200, random_state=42)
forest.fit(X_train, Y_train)
print(f'Random Forest test accuracy:', round(forest.score(X_test, Y_test), 3))

importances = pd.Series(forest.feature_importances_, index=X.columns)
print(importances.sort_values(ascending=False).round(3))

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score

# df = pd.read_csv('loan_data_set.csv')

# df = df.drop(columns=['Loan_ID'])
# df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
# df['Married'] = df['Married'].fillna(df['Married'].mode()[0])
# df['Dependents'] = df['Dependents'].fillna(df['Dependents'].mode()[0])
# df['Self_Employed'] = df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])
# df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
# df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].median())
# df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mode()[0])

# # Convert categorical columns into numbers
# df = pd.get_dummies(df, columns=['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area'], dtype=int)
# # Convert target
# df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})
# X = df.drop(columns=['Loan_Status'])
# Y = df['Loan_Status']

# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)
# forest = RandomForestClassifier(n_estimators=200, random_state=42)
# forest.fit(X_train, Y_train)
# print('Random Forest test accuracy:', round(forest.score(X_test, Y_test), 3))
# importances = pd.Series(forest.feature_importances_, index=X.columns)
# print('\nFeature Importance:')
# print(importances.sort_values(ascending=False).round(3))

# # Ask customer questions

# print('\n--- Loan Eligibility ---')

# gender = input('Gender (Male/Female): ')
# married = input('Married (Yes/No): ')
# dependents = input('Dependents (0/1/2/3+): ')
# education = input('Education (Graduate/Not Graduate): ')
# self_employed = input('Self Employed (Yes/No): ')

# applicant_income = float(input('Applicant Income: '))
# coapplicant_income = float(input('Coapplicant Income: '))
# loan_amount = float(input('Loan Amount: '))
# loan_term = float(input('Loan Term (months): '))
# credit_history = float(input('Credit History (1 = Good, 0 = Bad): '))

# property_area = input(
#     'Property Area (Urban/Semiurban/Rural): '
# )

# # Create customer DataFrame
# customer = pd.DataFrame([{
#     'ApplicantIncome': applicant_income,
#     'CoapplicantIncome': coapplicant_income,
#     'LoanAmount': loan_amount,
#     'Loan_Amount_Term': loan_term,
#     'Credit_History': credit_history,

#     'Gender_Female': 1 if gender.lower() == 'female' else 0,
#     'Gender_Male': 1 if gender.lower() == 'male' else 0,

#     'Married_No': 1 if married.lower() == 'no' else 0,
#     'Married_Yes': 1 if married.lower() == 'yes' else 0,

#     'Dependents_0': 1 if dependents == '0' else 0,
#     'Dependents_1': 1 if dependents == '1' else 0,
#     'Dependents_2': 1 if dependents == '2' else 0,
#     'Dependents_3+': 1 if dependents == '3+' else 0,

#     'Education_Graduate': 1 if education.lower() == 'graduate' else 0,
#     'Education_Not Graduate': 1 if education.lower() == 'not graduate' else 0,

#     'Self_Employed_No': 1 if self_employed.lower() == 'no' else 0,
#     'Self_Employed_Yes': 1 if self_employed.lower() == 'yes' else 0,

#     'Property_Area_Rural': 1 if property_area.lower() == 'rural' else 0,
#     'Property_Area_Semiurban': 1 if property_area.lower() == 'semiurban' else 0,
#     'Property_Area_Urban': 1 if property_area.lower() == 'urban' else 0
# }])

# # Make sure customer columns are in the same order
# customer = customer.reindex(columns=X.columns, fill_value=0)
# # Prediction
# prediction = forest.predict(customer)[0]
# if prediction == 1:
#     print('\n✅ Customer is eligible for the loan.')
# else:
#     print('\n❌ Customer is not eligible for the loan.')
