"""
Задание "Они все так похожи":
По названию задачи можно понять, что все геометрические фигуры обладают схожими свойствами,
такими как: длины сторон, цвет и др.

Давайте попробуем реализовать простейшие классы для некоторых таких фигур и при этом
применить наследование (в будущем, изучая сторонние библиотеки, вы будете замечать схожие
классы, уже написанные кем-то ранее):

Общее ТЗ:
Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут
обладать методами изменения размеров, цвета и т.д.
Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны
интерфейсы взаимодействия (методы) - геттеры и сеттеры.

Подробное ТЗ:

Атрибуты класса Figure: sides_count = 0
Каждый объект класса Figure должен обладать следующими атрибутами:
Атрибуты(инкапсулированные): __sides(список сторон (целые числа)),
__color(список цветов в формате RGB)
Атрибуты(публичные): filled(закрашенный, bool)
И методами:
Метод get_color, возвращает список RGB цветов.
Метод __is_valid_color - служебный, принимает параметры r, g, b,
который проверяет корректность переданных значений
перед установкой нового цвета. Корректным цвет:
все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
Метод set_color принимает параметры r, g, b - числа и изменяет
атрибут __color на соответствующие значения, предварительно проверив их на корректность.
Если введены некорректные данные, то цвет остаётся прежним.
Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон,
возвращает True если все стороны
целые положительные числа и кол-во новых сторон совпадает с текущим,
False - во всех остальных случаях.
Метод get_sides должен возвращать значение я атрибута __sides.
Метод __len__ должен возвращать периметр фигуры.

Атрибуты класса Circle: sides_count = 1
Каждый объект класса Circle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).

Атрибуты класса Triangle: sides_count = 3
Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника)
Метод get_square возвращает площадь треугольника.

Атрибуты класса Cube: sides_count = 12
Каждый объект класса Cube должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure.
Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
Метод get_volume, возвращает объём куба.

ВАЖНО!
При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать
массив с единичными сторонами и в том кол-ве, которое требует фигура.
Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

Примечания (рекомендации):
Рекомендуется сделать дополнительные (свои проверки) работы методов объектов каждого класса.
Делайте каждый класс и метод последовательно и проверяйте работу каждой части отдельно.
Для проверки принадлежности к типу рекомендуется использовать функцию isinstance.
Помните, служебные инкапсулированные методы можно и нужно использовать только внутри текущего класса.
Вам не запрещается вводить дополнительные атрибуты и методы, творите, но не переборщите!
"""
import math


class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=False):
        self.__color = list(color)
        if self.__is_valid_sides(*sides):
            if isinstance(self, Cube):
                self.__sides = list(sides) * self.sides_count
            else:
                self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count
        self.filled = filled  # (закрашенный, bool)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for color in [r, g, b]:
            if isinstance(color, int) and 0 <= color <= 255:
                return True
            else:
                return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):  # принимает картеж
        if isinstance(self, Cube):
            cond_1 = len(sides) == 1
        else:
            cond_1 = len(sides) == self.sides_count
        cond_2 = all([isinstance(side, int) and side > 0 for side in sides])
        return cond_1 and cond_2  # True and True или False and False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            if isinstance(self, Cube):
                self.__sides = list(new_sides) * 12
            else:
                self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple, *sides):
        super().__init__(color, sides)
        self.__radius = self.get_radius()

    def get_square(self):  # возвращает площадь круга через длину окружности
        return (self.__len__() ** 2) / (4 * math.pi)

    def get_radius(self):
        self.__radius = self.__len__() / (2 * math.pi)
        return self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple, *sides):
        if self.__is_triangle_exists(*sides):
            super().__init__(color, sides)
            self.__height = self.get_height_triangle(sides[0], sides[1], sides[2])
        else:
            raise ValueError("Невозможно создать треугольник с указанными сторонами")

    def get_height_triangle(self, a, b, c):
        p = (a + b + c) / 2
        height = 2 * math.sqrt(p * (p - a) * (p - b) / a)
        return height

    def get_square(self, a, b, c):
        p = (a + b + c) / 2
        square = math.sqrt(p * (p - a) * (p - b) * (p - c))

    def __is_triangle_exists(self, a, b, c):
        if a + b > c and b + c > a and a + c > b:
            return True
        else:
            return False


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple, *sides):
        super().__init__(color, sides)


    def get_volume(self):
        volume = self.get_sides()[0] ** 3
        return volume



""" Код для проверки: """
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

print("# Проверка на изменение цветов:")
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print("Круг с цветами 55 66 77 - ", circle1.get_color())
print("Куб с цветами 222, 35, 130 - ", cube1.get_color())
print('\n')

print("# Проверка на изменение сторон:")
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15) # Изменится
print("Сторона куба 6 - ", cube1.get_sides())
print("Сторона круга 15 - ", circle1.get_sides())
print('\n')

print("# Проверка периметра (круга)")
print("Периметр круга 15 - ", len(circle1))
print('\n')

print('# Проверка объёма (куба):')
print("Объем куба - ", cube1.get_volume())


