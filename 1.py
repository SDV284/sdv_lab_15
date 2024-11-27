import pandas as pd

# Оригінальний словник
car_data = {
    "audi": (250000, 3),
    "ferrari": (3500000, 7),
    "bmw": (500000, 6),
    "toyota": (600000, 12)
}

# Перетворення словника на датафрейм
df = pd.DataFrame.from_dict(
    car_data, 
    orient='index', 
    columns=['Вартість', 'Вік']
).reset_index()

df.rename(columns={"index": "Модель"}, inplace=True)

# Виведення датафрейму
print("Датафрейм:")
print(df)

# Групування: наприклад, вартість та середній вік
aggregated = df.groupby(pd.cut(df['Вік'], bins=[0, 5, 10, 15], labels=['0-5 років', '6-10 років', '11-15 років']), observed=True).agg({'Вартість': 'mean', 'Вік': 'mean'}).rename_axis("Група за віком")

print("\nАгреговані дані:")
print(aggregated)