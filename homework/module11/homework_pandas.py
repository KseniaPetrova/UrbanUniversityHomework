import pandas as pd
"""
Библиотека pandas позволяет выполнять различные действия с таблицами: сортировка, группировка, вычисление среднего балла
"""
# загрузка данных из файла Excel
df = pd.read_excel('file ex.xlsx')
print(df)

# Средний балл студентов
average_score = df['Балл'].mean()
print(f"Средний балл студентов: {average_score:.2f}")

# Сортировка по баллам по убыванию
df_sorted = df.sort_values(by='Балл', ascending=False)
print(df_sorted)










