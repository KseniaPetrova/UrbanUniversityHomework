import math

class Figure:
    sides_count = 0

    def __init__(self, sides=None, color=None):
        self.__sides = sides or []
        self.__color = color or [0, 0, 0]
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= c <= 255 and isinstance(c, int) for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        return all(isinstance(s, int) and s > 0 for s in sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, radius, sides=None, color=None):
        super().__init__(sides or [2 * math.pi * radius], color)
        self.__radius = radius

    def get_square(self):
        return math.pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, a, b, c, height, sides=None, color=None):
        super().__init__(sides or [a, b, c], color)
        self.__height = height

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, side, color=None):
        super().__init__([side] * 12, color)

    def get_volume(self):
        return self.get_sides()[0] ** 3


# Создание объектов
circle = Circle(5, color=[255, 0, 0])
triangle = Triangle(3, 4, 5, 6, color=[0, 255, 0])
cube = Cube(2, color=[0, 0, 255])

# Использование методов
print(circle.get_color())  # [255, 0, 0]
print(circle.get_square())  # 78.53981633974483

print(triangle.get_color())  # [0, 255, 0]
print(triangle.get_square())  # 6.0

print(cube.get_color())  # [0, 0, 255]
print(cube.get_volume())  # 8
