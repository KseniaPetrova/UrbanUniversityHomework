import math

class Figure:
    sides_count = 0

    def __init__(self, sides=None, color=None):
        if sides is None:
            self.__sides = [1] * self.sides_count
        else:
            if not self.__is_valid_sides(*sides):
                self.__sides = [1] * self.sides_count
            else:
                self.__sides = list(sides)
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
        if sides is None:
            super().__init__([2 * math.pi * radius], color)
        else:
            super().__init__(sides, color)
        self.__radius = radius

    def get_square(self):
        return math.pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, a, b, c, height, sides=None, color=None):
        if sides is None:
            super().__init__([a, b, c], color)
        else:
            super().__init__(sides, color)
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
circle = Circle(5, [10, 15, 6], color=[255, 0, 0])
triangle = Triangle(3, 4, 5, 6, [10, 6], color=[0, 255, 0])
cube = Cube(9, color=[0, 0, 255])
cube2 = Cube(9, [12], color=[255, 255, 255])

# Использование методов
print(circle.get_sides())  # [31.41592653589793]
print(triangle.get_sides())  # [1, 1, 1]
print(cube.get_sides())  # [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
print(cube2.get_sides())  # [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
