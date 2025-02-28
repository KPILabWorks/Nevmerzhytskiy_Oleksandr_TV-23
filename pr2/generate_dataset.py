import pandas as pd
import numpy as np

# Параметри генерації
num_records = 50000
cities = ["Kyiv", "Lviv", "Odesa", "Kharkiv", "Dnipro"]
start_date = pd.Timestamp("2015-01-01")
end_date = pd.Timestamp("2025-01-01")

# Генерація випадкових дат
dates = pd.date_range(start_date, end_date).to_list()
random_dates = np.random.choice(dates, size=num_records)

# Генерація випадкових міст
random_cities = np.random.choice(cities, size=num_records)

# Генерація погодних показників
temperatures = np.random.uniform(-20, 35, size=num_records)  # Від -20 до +35°C
humidity = np.random.uniform(30, 100, size=num_records)  # Від 30% до 100%
wind_speed = np.random.uniform(0, 20, size=num_records)  # Від 0 до 20 м/с

# Створення DataFrame
df = pd.DataFrame({
    "date": random_dates,
    "city": random_cities,
    "temperature": temperatures.round(1),
    "humidity": humidity.round(1),
    "wind_speed": wind_speed.round(1),
})

# Збереження в CSV
df.to_csv("weather_data.csv", index=False)

print("Генерація завершена! Файл weather_data.csv збережено.")
