# Дандер методы
class Cats:

    def __new__(cls, *args, **kwargs):
        """Вызывается первым:
       - Этот метод отвечает за создание самого объекта.
       - Он вызывается до __init__().
       - Он должен вернуть новый экземпляр класса"""
        print('__new__ cat')
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, age, breed, color, weight=0.0):
        """Метод, который используется для инициализации объекта класса.
        Он вызывается автоматически при создании нового объекта,
        и его задача - настроить объект для последующего использования.
        Срабатывает единожды при вызове."""
        self.name = name
        self.age = age
        self. breed = breed
        self.color = color
        self.weight = weight

    def __len__(self):
        """Измерит количество символов
         возвращает типом данных int"""
        # return int(self.weight)
        # return len(self.name)
        return self.age

    def __lt__(self, other):  # меньше чем
        """Перегрузка стандартного оператора <
                Возвращает True False"""
        return self.age < other.age

    def __gt__(self, other):  # больше чем
        """Перегрузка стандартного оператора >
                Возвращает True False"""
        return self.age > other.age

    def __eq__(self, other):  # оператор ==
        """Перегрузка стандартного оператора ==
                Возвращает True False"""
        return self.age == other.age and self.name == other.name

    def __bool__(self):
        """Переопределение логической интерпретации объекта"""
        return bool(self.age)

    def __str__(self):
        """Определяет строковое представление объекта"""
        return f'{self.name}'

    def __del__(self):
        """Диструктор. Удаляет объект из памяти"""
        print(f'{self.name} покинул область памяти')



pes = Cats(name='Пёс', age=2, breed='Метис', color='Серый', weight=4.76)
persic = Cats(name='Персик', age=12, breed='Без породы', color='Рыжий', weight=7.39)

print(pes < persic)  # работа метода __lt__  True
print(pes == persic)  # работа метода __eq__ False
print(persic)  # работа метода __str__ "Персик" иначе <__main__.Cats object at 0x00000217AA41EA20>