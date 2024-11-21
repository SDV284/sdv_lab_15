import pandas as pd

# Завантаження даних
file_path = 'comptagevelo20162.csv'  # Замініть на ваш шлях до файлу
data = pd.read_csv(file_path)

# Конвертація колонки 'Date' у формат datetime
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

# Додавання колонки 'Month' для зберігання номеру місяця
data['Month'] = data['Date'].dt.month

# Обчислення загальної кількості велосипедистів для кожного місяця
monthly_totals = data.groupby('Month').sum(numeric_only=True).sum(axis=1)

# Визначення найпопулярнішого місяця
most_popular_month = monthly_totals.idxmax()
most_popular_month_total = monthly_totals.max()

print("Розподіл велосипедистів за місяцями:")
print(monthly_totals)
print(f"Найпопулярніший місяць: {most_popular_month}, із загальною кількістю проїздів: {most_popular_month_total}")
