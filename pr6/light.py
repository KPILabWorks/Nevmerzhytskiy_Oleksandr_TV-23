import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


def load_data(file_path):
    return pd.read_csv(file_path)


def analyze_data(data, label):
    """Розрахунок базової статистики"""
    avg = data['Illuminance (lx)'].mean()
    min_val = data['Illuminance (lx)'].min()
    max_val = data['Illuminance (lx)'].max()
    std_dev = data['Illuminance (lx)'].std()

    print(f"{label}")
    print(f"Середнє освітлення: {avg:.2f} лк")
    print(f"Мінімальне освітлення: {min_val:.2f} лк")
    print(f"Максимальне освітлення: {max_val:.2f} лк")
    print(f"Стандартне відхилення: {std_dev:.2f} лк")
    print(f"Коефіцієнт варіації: {std_dev / avg * 100:.2f}%\n")

    return {
        'label': label,
        'mean': avg,
        'min': min_val,
        'max': max_val,
        'std_dev': std_dev,
        'variation': std_dev / avg * 100
    }


def plot_data(datasets):
    plt.figure(figsize=(14, 8))
    for data in datasets:
        time = data['Time (s)'] / 3600  # переводимо в години
        illuminance = data['Illuminance (lx)']
        label = data['label'].iloc[0]  # беремо перший елемент (весь стовпець однаковий)
        mean_value = data['mean'].iloc[0]

        plt.plot(time, illuminance, label=f"{label} (середнє={mean_value:.1f} лк)")

    plt.title('Порівняння рівня освітленості', fontsize=18)
    plt.xlabel('Час (години)', fontsize=15)
    plt.ylabel('Освітленість (лк)', fontsize=15)
    plt.yscale('log')  # логарифмічна шкала
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.legend(fontsize=13)
    plt.tight_layout()
    plt.show()


def main():
    files = {
        'Природне освітлення': 'natural_light.csv',
        'Штучне освітлення 1': 'artificial_light1.csv',
        'Штучне освітлення 2': 'artificial_light2.csv'
    }

    all_data = []
    analysis_results = []

    for label, file in files.items():
        data = load_data(file)
        if 'Illuminance (lx)' not in data.columns:
            print(f"У файлі {file} немає стовпця 'Illuminance (lx)'!")
            continue

        analysis = analyze_data(data, label)
        analysis_results.append(analysis)

        data['label'] = label
        data['mean'] = analysis['mean']
        all_data.append(data)

    # Побудова графіка
    plot_data(all_data)

    # Порівняння
    print("\nПорівняння джерел світла")
    max_mean = max(analysis_results, key=lambda x: x['mean'])
    min_variation = min(analysis_results, key=lambda x: x['variation'])

    print(f"Найвище середнє освітлення має: {max_mean['label']} ({max_mean['mean']:.2f} лк)")
    print(
        f"Найстабільніше освітлення має: {min_variation['label']} (Коефіцієнт варіації {min_variation['variation']:.2f}%)")


if __name__ == "__main__":
    main()
