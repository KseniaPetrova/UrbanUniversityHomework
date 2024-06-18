import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.age = age

class Video:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        for user in self.users:
            if user.nickname == login and user.password == hashed_password:
                self.current_user = user
                print(f"Пользователь {login} вошёл в систему.")
                return
        print("Неверный логин или пароль.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} успешно зарегистрирован.")

    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта.")

    def add(self, *videos):
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)
                print(f"Видео {video.title} добавлено.")
            else:
                print(f"Видео {video.title} уже существует.")

    def get_videos(self, search_word):
        search_word = search_word.lower()
        return [video.title for video in self.videos if search_word in video.title.lower()]

    def watch_video(self, title):
        for video in self.videos:
            if video.title == title:
                if self.current_user is None:
                    print("Войдите в аккаунт, чтобы смотреть видео.")
                    return
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу.")
                    return
                while video.time_now < video.duration:
                    print(f"Видео воспроизводится на {video.time_now} секунде.")
                    video.time_now += 1
                    time.sleep(1)
                video.time_now = 0
                print("Конец видео.")
                return
        print(f"Видео с названием '{title}' не найдено.")


if __name__ == '__main__':
    ur = UrTube()
    # user1 = User('oleg', '123', 27)
    # user2 = User('Max', 'qwe', 22)
    user3 = User('nina', '123', 9)
    # ur.register(user1.nickname, user1.password, user1.age)
    # ur.register(user2.nickname, user2.password, user2.age)
    ur.register(user3.nickname, user3.password, user3.age)
    video1 = Video('Urban', 9600)
    video2 = Video('Urban', 3600)
    video3 = Video('Urban123', 10600)
    ur.add(video1, video2, video3)
    ur.watch_video('Urban')
    while True:
        choice = int(input('Вы хотите войти или зарегистрироваться? \n1 - Вход\n2 - Регистрация\n'))
        if choice == 1:
            ur.log_in(input('Введите логин: '), input('Введите пароль: '))
        elif choice == 2:
            ur.register(input('Введите ник: '), input('Введите пароль:'), int(input('Введите возраст: ')))
        elif choice == 3:
            break