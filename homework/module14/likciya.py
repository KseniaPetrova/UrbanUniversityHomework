import sqlite3
from random import randint

# подключение к базе
connection = sqlite3.connect('database.db')

# курсор взаимодействия
cursor = connection.cursor()
cursor.fetchall()
cursor.fetchone()
cursor.fetchmany()
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

#Выбираем всех юзеров, сохраняем их в users и выводим на экран
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

# Подсчитает количество юзеров
# cursor.execute("SELECT COUNT(*) FROM UsersTable")
# total1 = cursor.fetchone()[0]  # позволяет получить элемент запроса
# print(total1)

# Подсчитает количество юзеров где возраст больше 30
cursor.execute("SELECT COUNT(*) FROM UsersTable WHERE age > ?", (30,))
total1 = cursor.fetchone()[0]  # позволяет получить элемент запроса
print(total1)

# Посчитает сумму возрастов
cursor.execute("SELECT SUM(age) FROM UsersTable")
total1 = cursor.fetchone()[0]  # позволяет получить элемент запроса
print(total1)

# Вычислит минимальный возраст. с функцийе MAX вычислит маскимальный возраст
cursor.execute("SELECT MIN(age) FROM UsersTable")
total1 = cursor.fetchone()[0]  # позволяет получить элемент запроса
print(total1)

# Функция, которая добавляет пользователя в бд
def add_user(user_id, username, first_name):
    check_user = cursor.execute("SELRCT * FROM UsersTable WHERE id=?", (user_id,))

    if check_user.fetchone() is None:
        cursor.execute(f'''
    INSERT INTO UsersTable VALUES('{user_id}', '{username}', '{first_name}', 0)''')
        connection.commit()

# Выводит пользователей
def show_users():
    users_list = cursor.execute("SELECT * FROM UsersTable")
    message = ''
    for user in users_list:
        message += f"{user[0]} @{user[1]} {user[2]} \n"
    connection.commit()
    return message

# Выводит статистику
def show_stat():
    count_users = cursor.execute("SELECT COUNT(*) FROM UsersTable").fetchone()
    connection.commit()
    return count_users[0]

# Добавление в блок
def add_to_block(input_id):
    cursor.execute(f"UPDATE UsersTable SET block = ? WHERE id = ?",
        (1, input_id))
    connection.commit()

# Вытаскивание из в блока
def remove_block(input_id):
    cursor.execute(f"UPDATE UsersTable SET block = ? WHERE id = ?",
        (0, input_id))
    connection.commit()

# Проверяет есть ли пользователь в блокировке
def check_block(user_id):
    users = cursor.execute(f"SELECT block FROM UsersTable WHERE id = {user_id}").fetchone()
    connection.commit()
    return users[0]

connection.commit()  # сохранение текущего состояния
connection.close()









