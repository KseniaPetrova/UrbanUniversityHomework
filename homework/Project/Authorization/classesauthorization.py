class Database:
    """Класс базы данных пользователей хранящий логины и пароль"""
    def __init__(self):
        self.data = {}

    def add_base(self, login, password):
        self.data[login] = password


class User:
    """Класс пользователя содержащий логин и пароль"""
    def __init__(self, login, password, password_confirm):
        self.login = login
        if password == password_confirm:
            self.password = password


# if __name__ == '__main__':
#     data1 = Database()
#     user1 = User('Oleg', '123qwe', '123qwe')
#     user2 = User('Alex', '123', '123')
#     user3 = User('Max', 'qwe', 'qwe')
#     data1.add_base(user1.login, user1.password)
#     data1.add_base(user2.login, user2.password)
#     data1.add_base(user3.login, user3.password)
#     print(data1.data)

"""Логика работы регистрации"""
if __name__ == '__main__':
    database = Database()
    user1 = User('oleg', '123', '123')
    database.add_base(user1.login, user1.password)
    record = True
    while record:
        choice_entrance = int(input('Выберите действие: \n1 - Вход\n2 - Регистрация\n'))
        if choice_entrance == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print('Добро пожаловать')
                    break
                else:
                    print('Неверный пароль')
            else:
                print('Пользователь не найден.')
        if choice_entrance == 2:
            while True:
                user = User(input('Введите логин: '),
                            password := input('Ведите пароль: '),
                            password_confirm := input('Повторите пароль: '))
                if password != password_confirm:
                    print('Пароли не совпадают. Повторите ввод.')
                    continue
                else:
                    database.add_base(user.login, user.password)
                    print(f'Добро пожаловать, {user.login}!')
                    # record = False
                    break
            # break
    print(database.data)
