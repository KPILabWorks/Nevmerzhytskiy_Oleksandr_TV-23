import pandas as pd
import numpy as np
import functools
import time
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import seaborn as sns

# Використання стилю Seaborn
sns.set_theme(style="whitegrid")

# Завантаження дата-сету
df = pd.read_csv("weather_data.csv", parse_dates=["date"])
df["year"] = df["date"].dt.year  # Додаємо колонку з роком

# Функція з кешуванням
@functools.lru_cache(maxsize=None)
def get_avg_temperature_cached(city: str, year: int) -> float:
    """Кешована функція для обчислення середньої температури."""
    filtered = df[(df["city"] == city) & (df["year"] == year)]
    if filtered.empty:
        return np.nan
    return filtered["temperature"].mean()

# Функція без кешування
def get_avg_temperature_no_cache(city: str, year: int) -> float:
    """Функція без кешування."""
    filtered = df[(df["city"] == city) & (df["year"] == year)]
    if filtered.empty:
        return np.nan
    return filtered["temperature"].mean()

# Вимірювання часу без кешу
start_time = time.time()
df["avg_temp_no_cache"] = df.apply(lambda row: get_avg_temperature_no_cache(row["city"], row["year"]), axis=1)
no_cache_time = time.time() - start_time

# Очистка кешу перед тестом
get_avg_temperature_cached.cache_clear()

# Вимірювання часу з кешем
start_time = time.time()
df["avg_temp_cached"] = df.apply(lambda row: get_avg_temperature_cached(row["city"], row["year"]), axis=1)
cached_time = time.time() - start_time

# Обчислення прискорення
speedup = no_cache_time / cached_time if cached_time > 0 else float("inf")

# ======= ПОБУДОВА ГРАФІКІВ =======

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Гістограма часу виконання
axes[0].bar(["Без кешу", "З кешем"], [no_cache_time, cached_time], color=["red", "green"], alpha=0.7)
axes[0].set_ylabel("Час виконання (сек)", fontsize=12)
axes[0].set_title("Час виконання функції", fontsize=14)
axes[0].grid(axis="y", linestyle="--", alpha=0.6)

# Додаємо значення на стовпчики
for i, v in enumerate([no_cache_time, cached_time]):
    axes[0].text(i, v + 0.05, f"{v:.3f} сек", ha="center", fontsize=12, fontweight="bold")

# Лінійний графік прискорення
axes[1].plot(["Без кешу", "З кешем"], [1, speedup], marker="o", linestyle="--", color="blue", markersize=8, linewidth=2)
axes[1].set_ylabel("Прискорення (разів)", fontsize=12)
axes[1].set_title("Прискорення кешування", fontsize=14)
axes[1].grid(axis="y", linestyle="--", alpha=0.6)

# Додаємо значення на точки графіка
axes[1].text(1, speedup, f"{speedup:.2f}x", ha="left", fontsize=12, fontweight="bold", color="blue")

# Відображення графіків
plt.tight_layout()
plt.show()
