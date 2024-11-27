import pandas as pd
import matplotlib.pyplot as plt

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

plt.style.use('ggplot') 

plt.rcParams['figure.figsize'] = (15, 5) 

fixed_df = pd.read_csv(file_path, 

                       sep=',', encoding='latin1',

                       parse_dates=['Date'], dayfirst=True,

                       index_col='Date')

fixed_df.plot(figsize=(15, 10))
plt.show()