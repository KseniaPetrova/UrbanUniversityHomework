"""Домашняя работа по уроку "Различие атрибутов класса и экземпляра."

Ваша задача:
Создайте новый класс Building с атрибутом total
Создайте инициализатор для класса Building, который будет увеличивать атрибут
количества созданных объектов класса Building total
В цикле создайте 40 объектов класса Building и выведите их на экран командой print
Полученный код напишите в ответ к домашнему заданию"""


class Building:

    total = 0

    def __init__(self):
        Building.total += 1

    def __str__(self):
        return f' {Building.total}'


for _ in range(40):
    building = Building()
    print(building)