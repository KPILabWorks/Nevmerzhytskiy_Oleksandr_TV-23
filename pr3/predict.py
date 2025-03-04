from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns


# Завантажимо дані
energy_data = pd.read_csv('energy_data.csv')


# Перетворимо категоріальну змінну 'Consumer Type' в числову за допомогою one-hot encoding
X = energy_data[['Generation (kWh)', 'Consumer Type']].copy()
X = pd.get_dummies(X, drop_first=True)

# Цільова змінна
y = energy_data['Consumption (kWh)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error (MAE): {mae:.2f}')
print(f'Root Mean Squared Error (RMSE): {rmse}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'R²: {r2:.2f}')


# Візуалізація результатів
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.title('Real vs Predicted Energy Consumption')
plt.xlabel('Actual Consumption (kWh)')
plt.ylabel('Predicted Consumption (kWh)')
plt.grid(True)
plt.show()

