import pandas as pd
import functools

# Кешування ціни товару для категорії
@functools.lru_cache(maxsize=None)
def get_price_for_product(product):
    prices = {
        "Laptop": 1200, "Smartphone": 800, "Headphones": 150,
        "Sneakers": 100, "Jeans": 50, "T-shirt": 20,
        "Watch": 250, "Backpack": 40, "Sunglasses": 30
    }
    return prices.get(product, 0)

# Завантажуємо дані з CSV
df = pd.read_csv("transactions_dataset.csv")

# Додаємо колонку з кешованими цінами
df['price_cached'] = df['product'].apply(get_price_for_product)

# Тепер обчислюємо загальну вартість кожної транзакції, використовуючи кешовану ціну
df['total_price'] = df.apply(lambda row: row['price_cached'] * row['quantity'], axis=1)

# Зберігаємо оброблені дані в новий файл
df.to_csv("processed_transactions.csv", index=False)

# Виводимо кілька перших рядків, щоб перевірити результат
print(df.head())
