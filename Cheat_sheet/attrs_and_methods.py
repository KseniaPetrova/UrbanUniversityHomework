# -*- coding: utf-8 -*-

# Атрибуты объекта-экземпляра не нужно описывать — как и переменные,
# они начинают существование в момент первого присваивания


class Robot:

    def __init__(self):
        self.name = 'R2D2'

    def hello(self):
        print('привет мир!')


robot = Robot()
robot.temperature = 1
while robot.temperature < 10:
    robot.temperature *= 2
print(robot.temperature)  # 16
del robot.temperature

# Атрибуты сохраняются в пространстве имен каждого объекта - у разных объектов они м.б. разные

robot_2 = Robot()
robot_2.name = 'Валли'

print(robot.name, robot_2.name)  # R2D2 Валли

print(robot, robot_2)  # <__main__.Robot object at 0x0000023D8FB9E1E0> <__main__.Robot object at 0x0000023D8FB9E210>
print(robot == robot_2, robot is robot_2)  # False False


# Полезные функции для работы с атрибутами
# hasattr(object, name) - проверка существования атрибута
# setattr(object, name, value) - установка атрибута со значением
# delattr(object, name) - удаление атрибута
# getattr(object, name, default=None) - получение атрибута
# name это строка!

attr_name = 'model'

if hasattr(robot, attr_name):
    print(robot.model)
else:
    setattr(robot, attr_name, 'android')
print(robot.model)
delattr(robot, attr_name)

# то есть можно устанавливать атрибуты динамически, по именам
for attr_name in ('weight', 'height', ):
    setattr(robot, attr_name, 42)    # устанавливает значение 42 для 'weight', 'height'
print(hasattr(robot, 'weight'))  # True
print(robot.weight)   # 42

# getattr(object, name, default=None) - получение атрибута
print(getattr(robot, 'weight'))  # 42
print(getattr(robot, 'speed', 10))  # 10