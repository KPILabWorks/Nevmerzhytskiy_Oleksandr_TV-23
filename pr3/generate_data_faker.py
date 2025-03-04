from faker import Faker
import random
import pandas as pd

# Ініціалізація Faker
faker = Faker()


# Функція для генерації випадкових даних
def generate_energy_data(num_records):
    data = []

    for _ in range(num_records):
        consumer_type = random.choice(['Домогосподарство', 'Підприємство'])
        consumption = random.uniform(50, 500) if consumer_type == 'Домогосподарство' else random.uniform(1000, 5000)
        generation = random.uniform(0, consumption)  # Генерація не може перевищувати споживання

        data.append({
            'ID': faker.uuid4(),
            'Consumer Type': consumer_type,
            'Consumption (kWh)': round(consumption, 2),
            'Generation (kWh)': round(generation, 2),
            'Date': faker.date_this_year()
        })

    return pd.DataFrame(data)


# Генерація 100 записів
energy_data = generate_energy_data(10000)

# Збережемо згенеровані дані у CSV файл
file_path = 'energy_data.csv'
energy_data.to_csv(file_path, index=False)

print("Генерація завершилась успішно, Дані збережено до energy_data.csv")

