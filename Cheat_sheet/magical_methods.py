# Дандер методы
class Cats:

    def __new__(cls, *args, **kwargs):
        """Вызывается первым:
       - cls указатель на класс
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
        Срабатывает единожды при вызове.
        self - указатель на объект"""
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

    def __le__(self, other):  # меньше чем
        """Перегрузка стандартного оператора <=
                Возвращает True False"""
        return self.age <= other.age

    def __gt__(self, other):  # больше чем
        """Перегрузка стандартного оператора >
                Возвращает True False"""
        return self.age > other.age

    def __ge__(self, other):  # больше чем
        """Перегрузка стандартного оператора >=
                Возвращает True False"""
        return self.age >= other.age

    def __eq__(self, other):  # оператор ==
        """Перегрузка стандартного оператора ==
                Возвращает True False"""
        return self.age == other.age and self.name == other.name

    def __ne__(self, other):
        """Перегрузка стандартного оператора !=
                        Возвращает True False"""
        return self.age == other.age and self.name == other.name

    def __contains__(self, item):
        """Перегрузка стандартного оператора in
                        Возвращает True False"""
        return item in self.name

    def __bool__(self):
        """Переопределение логической интерпретации объекта.
        Оператор перегрузки"""
        return bool(self.age)

    # Эмуляция математических операций
    # Перегрузка операторов
    #
    # object.__add__(self, other) - сложение +
    # object.__sub__(self, other) - вычитание -
    # object.__mul__(self, other) - умножение *
    # object.__truediv__(self, other) - деление /
    # object.__floordiv__(self, other) - целочисленное деление //
    # object.__mod__(self, other) - остаток от деления %
    # object.__pow__(self, other) - возведение в степень **
    # object.__lshift__(self, other) - побитовый сдвиг влево <<
    # object.__rshift__(self, other) - побитовый сдвиг вправо >>
    # object.__and__(self, other) - побитовое И &
    # object.__xor__(self, other) - побитовое исключающее ИЛИ ^
    # object.__or__(self, other) - побитовое ИЛИ |
    #
    # должны возвращать объект

    # для операций расширенного присвоения служат методы
    # object.__iadd__(self, other) - +=
    # object.__isub__(self, other) - -=
    # object.__imul__(self, other) - *=
    # object.__itruediv__(self, other) - /+
    # object.__ifloordiv__(self, other) - //=
    # object.__imod__(self, other) - %=
    # object.__ipow__(self, other) - **=
    # object.__ilshift__(self, other) - <<=
    # object.__irshift__(self, other) - >>=
    # object.__iand__(self, other) - &=
    # object.__ixor__(self, other) - ^=
    # object.__ior__(self, other) - |=
    #
    # они изменяют сам объект (по месту, inplace)

    def __str__(self):
        """Возвращает строку, которая может быть показана конечному пользователю"""
        return f'{self.name}'

    def __del__(self):
        """Диструктор. Удаляет объект из памяти"""
        print(f'{self.name} покинул область памяти')

    def __repr__(self):
        """Возвращает строку, которая может быть использована для создания нового объекта того же типа"""
        return f'Cats({self.name})'



pes = Cats(name='Пёс', age=2, breed='Метис', color='Серый', weight=4.76)
persic = Cats(name='Персик', age=12, breed='Без породы', color='Рыжий', weight=7.39)

print(pes < persic)  # работа метода __lt__  True
print(pes == persic)  # работа метода __eq__ False
print(persic)  # работа метода __str__ "Персик" иначе <__main__.Cats object at 0x00000217AA41EA20>
print((repr(pes))) # Cats(Пёс)
print("Пёс" in pes) # True | работа метода __contains__
if pes == persic:
    print('Одногодки')
# Вариант вызова метода ↑ или ↓
if Cats.__eq__(self=pes, other=persic):
    print('Одногодки')

class Backpack:
    """ Рюкзак """

    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    def add(self, item):
        """ Положить в рюкзак """
        self.content.append(item)
        print("В рюкзак положили:", item)

    def __str__(self):
        return 'Backpack: ' + ', '.join(self.content)

    def __bool__(self):
        return self.content != []

    def __len__(self):
        return len(self.content)


my_backpack = Backpack()
# my_backpack.add(item='ноутбук')
print(bool(my_backpack), len(my_backpack))
if my_backpack:
    print('Рюкзак не пуст!')
    print('В нем лежит', len(my_backpack), 'предметов')
else:
    print('Вот рюкзак пустой, он предмет простой...')


# все специальные методы перечислены в
#   https://docs.python.org/3/reference/datamodel.html#special-method-names

