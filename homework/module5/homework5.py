"""
Дополнительное практическое задание по модулю: "Классы и объекты."

Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности.

Задание "Свой YouTube":
Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные
ролики на тему IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса
требуются хотя бы базовые знания программирования.

Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые
будут выполнять похожий функционал на сайте.

Всего будет 3 класса: UrTube, Video, User.

Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы
добавления видео, авторизации и регистрации пользователя и т.д.

Подробное ТЗ:

Каждый объект класса User должен обладать следующими атрибутами и методами:
Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
Каждый объект класса Video должен обладать следующими атрибутами и методами:
Атрибуты: title(заголовок, строка), duration(продолжительность, секунды),
time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
 Атрибуты: users(список объектов User), videos(список объектов Video),
 current_user(текущий пользователь, User)
Метод log_in, который принимает на вход аргументы: login, password и пытается найти пользователя
в users с такими же логином и паролем. Если такой пользователь существует,
то current_user меняется на найденного. Помните, что password передаётся в виде строки,
а сравнивается по хэшу.
Метод register, который принимает три аргумента: nickname, password, age, и добавляет
пользователя в список, если пользователя не существует (с таким же nickname). Если существует,
выводит на экран: "Пользователь {nickname} уже существует". После регистрации,
вход выполняется автоматически.
Метод log_out для сброса текущего пользователя на None.
Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best'
(не учитывать регистр).
Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
После текущее время просмотра данного видео сбрасывается.
Для метода watch_video так же учитывайте следующие особенности:
Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае
выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к.
есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
После воспроизведения нужно выводить: "Конец видео"

Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
watch_video('Лучший язык программирования 2024 года!')

Вывод в консоль:
['Лучший язык программирования 2024 года']
['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
Войдите в аккаунт, чтобы смотреть видео
Вам нет 18 лет, пожалуйста покиньте страницу
1 2 3 4 5 6 7 8 9 10 Конец видео
Пользователь vasya_pupkin уже существует
urban_pythonist

Примечания:
Не забывайте для удобства использовать dunder(магические) методы: __str__, __repr__, __contains__,
__eq__ и др.
Чтобы не запутаться рекомендуется после реализации каждого метода проверять как он работает,
тестировать разные вариации.
"""
import time
import hashlib


class User:

    def __init__(self, nickname: str, password: str, age: int):
        """nickname(ник пользователя, строка, уникальное значение), password(в хэшированном виде, строка),
        age(возраст, число)"""
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age


class Video:

    def __init__(self, title: str, duration: int, adult_mode=False):
        """title(заголовок, строка), duration(продолжительность, секунды),
        time_now(секунда остановки (изначально 0)),
        adult_mode(ограничение по возрасту, bool (False по умолчанию))"""
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.title

class UrTube:

    def __init__(self):
        """Атрибуты: users(список объектов User), videos(список объектов Video),
        current_user(текущий пользователь, User)"""
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        """Метод log_in, который принимает на вход аргументы: nickname, password
        и пытается найти пользователя в users с такими же логином и паролем.
        Если такой пользователь существует, то current_user меняется на найденного.
        Помните, что password передаётся в виде строки, а сравнивается по хэшу."""
        passHash = hashlib.sha256(password.encode()).hexdigest()
        for user_in in self.users:
            if getattr(user_in, 'nickname') == nickname and getattr(user_in, 'password') == passHash:
                self.current_user = user_in
                print(f'Добро пожаловать, {nickname}')
                return
        print(f'Неверный логин или пароль')

    def register(self, nickname: str, password: str, age: int):
        """Метод register, который принимает три аргумента: nickname, password, age, и добавляет
        пользователя в список, если пользователя не существует (с таким же nickname). Если существует,
        выводит на экран: "Пользователь {nickname} уже существует". После регистрации,
        вход выполняется автоматически."""
        for user in self.users:
            if (getattr(user, 'nickname')) == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Пользователь {nickname} успешно зарегистрирован.')

    def log_out(self):
        """Метод log_out для сброса текущего пользователя на None."""
        self.current_user = None
        print('Вы вышли из аккаунта.')

    def add(self, *videos):
        """Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
        если с таким же названием видео ещё не существует. В противном случае ничего не происходит."""
        for movie in videos:
            if movie not in self.videos:
                self.videos.append(movie)

        for video in videos:  # Оно работает, но я не понимаю почему.
            found = True
            for v in self.videos:
                if video.title == v.title:
                    print(f'Видео с таким именем {video.title} уже существует')
                    found = False
                    break
            if found:
                self.videos.append(video)
                print(f'Видео {video.title} добавлено')

    def get_videos(self, keyWords: str):
        """Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
        содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best'
        (не учитывать регистр)."""
        keyWords = keyWords.lower()
        listVideos = []
        for video in self.videos:
            for word in [getattr(video, 'title'.lower())]:
                word = word.lower()
                if word in keyWords or keyWords in word:
                    listVideos.append(getattr(video, 'title'))
        return listVideos

    def watch_video(self, title: str):
        """Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
        то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
        После текущее время просмотра данного видео сбрасывается.
        Для метода watch_video так же учитывайте следующие особенности:
        Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
        Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае
        выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
        Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к.
        есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
        После воспроизведения нужно выводить: 'Конец видео'"""
        # title = title.lower()
        # for video in self.videos:  # такое начало бы подошло чтобы выдавать несколько вариантов по ключевому слову
        #     for word in [getattr(video, 'title')]:
        #         word = word.lower()
        #         if word in title or title in word:
        for video in self.videos:
            if video.title == title:
                if self.current_user == None:
                    print('Войдите в аккаунт, чтобы продолжить')
                    return
                if video.adult_mode == True and getattr(self.current_user, 'age') < 18:
                    print('Видео доступно к просмотру лицам старше 18 лет')
                    return
                while video.time_now <= video.duration:
                    print(f"Видео воспроизводится на {video.time_now} секунде.")
                    video.time_now += 1
                    time.sleep(1)
                video.time_now = 0
                print("Конец видео.")
                return


if __name__ == '__main__':
    # Код для проверки:
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
    #
    # # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    # ur.watch_video('Для чего девушкам парень программист?')

    # # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

    # ur = UrTube()
    # user1 = User('oleg',  '123', 8)
    # user2 = User('Max',  'qwe', 22)
    # user3 = User('nina',  '123', 9)
    # ur.register(user1.nickname, user1.password, user1.age)
    # ur.register(user2.nickname, user2.password, user2.age)
    # ur.register(user3.nickname, user3.password, user3.age)
    # ur.log_out()
    # ur.log_in('oleg', '123')
    # video1 = Video('Urban', 36, True)
    # video2 = Video('Urban 18+', 66, True)
    # video3 = Video('Urban', 96, False)
    # video4 = Video('Bla bla bla urb ', 96, False)
    # video5 = Video('Zebra', 96, False)
    # video6 = Video('Otladchik', 90, False)
    # video7 = Video('Margo', 60, False)
    # video8 = Video('Uuuu suka', 96, False)
    # ur.add(video1, video2, video3, video4, video5, video6, video7, video8)
    # ur.get_videos('urb')
    # ur.watch_video('Urban')
    # # for user in ur.users:
    # #     print(getattr(user, 'nickname'))
    # # print(ur.users)
    # while True:
    #     a = []
    #     choice = int(input('Вы хотите войти или зарегистрироваться? \n1 - Вход\n2 - Регистрация\n'))
    #     if choice == 1:
    #         ur.log_in(input('Введите логин: '), input('Введите пароль: '))
    #     elif choice == 2:
    #         ur.register(input('Введите ник: '), input('Введите пароль:'), int(input('Введите возраст: ')))
    #         for user in ur.users:
    #             a.append(getattr(user, 'nickname'))
    #             a.append(getattr(user, 'password'))
    #     elif choice == 3:
    #         break
    #
    #     # print(ur.__str__())
    #     # for i in ur.users:
    #     #     print(type(i))
    #     print(a)



    # # Вывод  в консоль:
    # ['Лучший язык программирования 2024 года']
    # ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
    # Войдите в аккаунт, чтобы смотреть видео
    # Вам нет 18 лет, пожалуйста покиньте страницу
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    # 10
    # Конец видео
    # Пользователь vasya_pupkin уже существует
    # urban_pythonist


