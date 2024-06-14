# import hashlib
#
# def hash_password(password):
#     # Просто хешируем пароль
#     hashed_password = hashlib.sha256(password.encode()).hexdigest()
#     return hashed_password
#
# def verify_password(input_password, stored_hash):
#     # Проверка введенного пароля
#     hashed_input_password = hashlib.sha256(input_password.encode()).hexdigest()
#     return hashed_input_password == stored_hash
#
# # Пример использования
# password = "secure_password"
# stored_hash = hash_password(password)
#
# # При аутентификации в системе
# user_input_password = "secure_password"
# if verify_password(user_input_password, stored_hash):
#     print("Аутентификация успешна.")
# else:
#     print("Неверный пароль.")
# import hashlib


class UrTube:

    def __init__(self):
        """Атрибуты: users(список объектов User), videos(список объектов Video),
        current_user(текущий пользователь, User)"""
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, login, password, age):
        self.users.append(User(nickname, login, password, age))

    def check(self, nickname):
        for user in ur.users:
            if user.nickname == nickname:
                return print(f'Пользователь найден')

    def __str__(self):
        """Определяет строковое представление объекта"""
        return f' i am f string {self.users}'

class User:

    def __init__(self, nickname: str, login: str, password: str, age: int):
        """nickname(имя пользователя, строка), password(в хэшированном виде, строка), age(возраст, число)"""
        self.userCode = login
        self.nickname = nickname
        self.login = login
        self.password = password  # hashlib.sha256(password.encode()).hexdigest()
        self.age = age


if __name__ == '__main__':
    ur = UrTube()
    user1 = User(nickname='Oleg', login='Oleg123', password='123qwe', age=25)
    user2 = User('Max', 'Maxim789', '321zxc', 22)
    # UrTube.register(user1.nickname, user1.login, user1.password, user1.age)
    ur.register(nickname=user1.nickname, login=user1.login, password=user1.password, age=user1.age)
    ur.register(user2.nickname, user2.login, user2.password, user2.age)
    # for user in ur.users:
    #     print([getattr(user, attr) for attr in ['nickname', 'login', 'password', 'age']])
    for user in ur.users:
        print(getattr(user, 'nickname'))

    # for user in ur.users:
    #     if getattr(user, 'nickname') == 'Oleg':
    #         print('yrs')
    ur.check(input('Enter nick'))

