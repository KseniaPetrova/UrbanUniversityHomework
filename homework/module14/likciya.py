import sqlite3
from random import randint

# подключение к базе
connection = sqlite3.connect('database.db')

# курсор взаимодействия
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS UsersTable (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')    # команды пишутся капсом. название таблиц с большой буквы, поля пишутся маленькми буквами
# PRIMARY KEY - автоматически проставляет id

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON UsersTable (email)")

# добавление инфы, пользователей
# cursor.execute("INSERT INTO UsersTable (username, email, age) VALUES (?, ?, ?)",
#                ("newuser", "ex@mail.ru", "28"))
# for i in range(30):
#     cursor.execute("INSERT INTO UsersTable (username, email, age) VALUES (?, ?, ?)",
#                    (f"newuser{i}", f"ex{i}@mail.ru", str(randint(18,80))))

#Обновление данных
# cursor.execute("UPDATE UsersTable SET age = ? WHERE username = ?",
#                (29, "newuser"))

#Удаление данных
# cursor.execute("DELETE FROM UsersTable WHERE username = ?",
#                (f"newuser",))

#ыбираем всех юзеров, сохраняем их в users и выводим на экран
# cursor.execute("SELECT * FROM UsersTable")
# users = cursor.fetchall()
# for user in users:
#     print(user)

#ВЫБРАТЬ username, age ИЗ UsersTable ГДЕ age > 29
# cursor.execute("SELECT username, age FROM UsersTable WHERE age > ?", (29,))
# users = cursor.fetchall()
# for user in users:
#     print(user)

#ВЫБРАТЬ age, СРЕДНЕЕ (от возраста) ИЗ UsersTable СГРУПИРОВАТЬ ПО ВОЗРАСТУ
# cursor.execute("SELECT age, AVG(age) FROM UsersTable GROUP BY AGE")
# users = cursor.fetchall()
# for user in users:
#     print(user)



connection.commit()  # сохранение текущего состояния
connection.close()









