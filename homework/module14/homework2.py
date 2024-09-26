"""
Задача "Средний баланс пользователя":
Для решения этой задачи вам понадобится решение предыдущей.
Для решения необходимо дополнить существующий код:
Удалите из базы данных not_telegram.db запись с id = 6.
Подсчитать общее количество записей.
Посчитать сумму всех балансов.
Вывести в консоль средний баланс всех пользователя.

"""
import sqlite3

connection = sqlite3.connect('not_telegram.db')

# курсор взаимодействия
cursor = connection.cursor()

# Удаление данных
cursor.execute("DELETE FROM Users WHERE id = ?",
               (6,))

# Подсчитает количество юзеров
cursor.execute("SELECT COUNT(*) FROM Users")
cout_users = cursor.fetchone()[0]  # позволяет получить элемент запроса

# Посчитает сумму
cursor.execute("SELECT SUM(balance) FROM Users")
sum_balance = cursor.fetchone()[0]

print(sum_balance/cout_users)

connection.commit()  # сохранение текущего состояния
connection.close()























