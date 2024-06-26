"""
Задача "Съедобное, несъедобное":
Разнообразие животного мира давно будоражит умы человечества. Царства, классы, виды...
Почему бы и нам не попробовать выстроить что-то подобное используя наследования классов?

Необходимо описать пример иерархии животного мира, используя классы и принцип наследования.

Создайте:
2 класса родителя: Animal, Plant
Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный),
name - индивидуальное название каждого животного.
Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения

4 класса наследника:
Mammal, Predator для Animal.
Flower, Fruit для Plant.

У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
eat(food) - метод, где food - это параметр, принимающий объекты классов растений.

Метод eat должен работать следующим образом:
Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>",
меняется атрибут fed на True.
Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>",
меняется атрибут alive на False.
Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.

У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)

Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.

Пункты задачи:
Создайте классы Animal и Plant с соответствующими атрибутами и методами
Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами.
При необходимости переопределите значения атрибутов.
Создайте объекты этих классов.
"""


class Animal:
    """Для класса Animal (животные)  атрибуты alive = True(живой) и
    fed = False(накормленный), name - индивидуальное название каждого животного."""
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Plant:
    """Для класса Plant (растения) атрибут edible = False(съедобность),
    name - индивидуальное название каждого растения"""
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    """Класс Млекопитающее
    У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
    eat(food) - метод, где food - это параметр, принимающий объекты классов растений.
    Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>",
    меняется атрибут alive на False.
    Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет."""
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            Animal.fed = True
            return
        else:
            print(f'{self.name} не стал есть {food.name}')
            Animal.alive = False


class Predator(Animal):
    """Класс Хищник"""
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            Animal.fed = True
            return
        else:
            print(f'{self.name} не стал есть {food.name}')
            Animal.alive = False


class Flower(Plant):
    """Класс Цветы
    атрибут edible = False(съедобность)"""
    edible = False
    pass


class Fruit(Plant):
    """Класс Фрукты"""
    edible = True
    pass



a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик

print(a1.alive)  # True
print(a2.fed)  # False
a1.eat(p1)  # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)  # Хатико съел Заводной апельсин
print(a1.alive)  # False
print(a2.fed)  # True







