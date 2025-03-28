import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import contextily as ctx

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Завантаження даних
url = '2.5_day.csv'
df = pd.read_csv(url)

# Фільтрація даних (землетруси магнітудою > 1)
df = df[df['mag'] > 1]

# Створення геодатафрейму
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')

# Перетворення в проекцію меркатора
gdf = gdf.to_crs(epsg=3857)

# Візуалізація
fig, ax = plt.subplots(figsize=(15, 15))

# Колірне кодування магнітуди
cmap = plt.get_cmap("Reds")
norm = plt.Normalize(vmin=gdf['mag'].min(), vmax=gdf['mag'].max())

# Нанесення точок із кольором відповідно до магнітуди
scatter = ax.scatter(
    gdf.geometry.x, gdf.geometry.y,
    s=gdf['mag'] * 5,  # Розмір точок
    c=gdf['mag'],       # Колірна шкала
    cmap=cmap, norm=norm, alpha=0.7, edgecolors="black"
)

# Додавання базової карти
ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron)

# Додавання кольорової шкали
cbar = fig.colorbar(scatter, ax=ax, orientation='vertical')
cbar.set_label('Magnitude', fontsize=14)

# Підписи для найсильніших землетрусів (магнітуда > 5)
top_quakes = gdf[gdf['mag'] > 5]
for _, row in top_quakes.iterrows():
    ax.text(row.geometry.x, row.geometry.y, f"{row['mag']:.1f}",
            fontsize=10, ha='right', color='white', bbox=dict(facecolor='black', alpha=0.5))

# Заголовок
ax.set_title("Earthquake Map (last 2.5 days)", fontsize=16)

# Вимкнення осей
ax.set_xticks([])
ax.set_yticks([])

# Показати карту
plt.show()
