# Домашнее задание по уроку "Специальные методы классов"
#
# Ваша задача:
# Создайте новый класс House.
# Создайте инициализатор для класса House, который будет задавать атрибут этажности
# self.numberOfFloors = 0
# Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут
# numberOfFloors на параметр floors и выводить в консоль numberOfFloors
# Полученный код напишите в ответ к домашнему заданию

class House:

    def __init__(self, numberOfFloors = 0):
        self.numberOfFloors = numberOfFloors

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        return print(self.numberOfFloors)


h1 = House()
h1.setNewNumberOfFloors(6)
