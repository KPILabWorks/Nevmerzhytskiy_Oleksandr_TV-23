import pandas as pd
import random
import string
import numpy as np
from datetime import datetime, timedelta

# Генерація випадкових назв товарів та категорій
products = [
    ("Laptop", "Electronics"), ("Smartphone", "Electronics"), ("Headphones", "Electronics"),
    ("Sneakers", "Footwear"), ("Jeans", "Clothing"), ("T-shirt", "Clothing"),
    ("Watch", "Accessories"), ("Backpack", "Accessories"), ("Sunglasses", "Accessories")
]


def generate_transactions(n):
    data = []
    start_date = datetime(2023, 1, 1)

    for i in range(n):
        transaction_id = f"T{i:07d}"
        user_id = f"U{random.randint(1000, 9999)}"
        product, category = random.choice(products)
        price = random.uniform(10, 2000)
        quantity = random.randint(1, 5)
        timestamp = start_date + timedelta(minutes=random.randint(0, 525600))  # Рік у хвилинах

        data.append([transaction_id, user_id, product, category, price, quantity, timestamp])

    return data


# Генеруємо дані
num_records = 10 ** 6  # 1 мільйон записів
data = generate_transactions(num_records)

df = pd.DataFrame(data, columns=["transaction_id", "user_id", "product", "category", "price", "quantity", "timestamp"])

# Зберігаємо в CSV файл
df.to_csv("transactions_dataset.csv", index=False)
