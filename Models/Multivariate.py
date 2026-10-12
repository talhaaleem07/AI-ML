# Multivariate Linear Regression

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1. Load the dataset
df = pd.read_csv('students_week5.csv')
features = ['study_hours', 'attendance_pct', 'previous_score', 'sleep_hours', 'assignments_done', 'internet_access', 'extra_tuition', 'part_time_job', 'parent_education']
x = df[features]
y = df['final_score']

# 2. Split, Train, Predict
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
pred = model.predict(x_test)

# 3. Evaluate the model
print('R2:', round(r2_score(y_test, pred), 3))
print('RMSE:', round(mean_squared_error(y_test, pred) ** 0.5, 2))
print(pd.Series(model.coef_, index=features).round(2))

