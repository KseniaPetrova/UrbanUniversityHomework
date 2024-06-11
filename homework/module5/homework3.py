"""Домашняя работа по уроку "Перегрузка операторов."

Ваша задача:
Создайте новый класс Building
Создайте инициализатор для класса Building, который будет задавать целочисленный
атрибут этажности self.numberOfFloors и строковый атрибут self.buildingType
Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
Полученный код напишите в ответ к домашнему заданию"""

class Building:

    def __init__(self, numberOfFloors: int, buildingType: str):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return (self.numberOfFloors == other.numberOfFloors
                and self.buildingType == other.buildingType)

house1 = Building(7, 'Общага')
house2 = Building(19, 'Многоэтажка')
house3 = Building(7, 'Общага')

print(house1 == house2)
print(house1 == house3)