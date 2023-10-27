import math

class Circle:
    def __init__(self, radius):
        if radius > 0:
            self.radius = radius
        else:
            raise ValueError("Радиус должен быть положительным числом")

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius


radius = float(input("Введите радиус круга: "))
circle = Circle(radius)
print("Площадь круга:", circle.area())
print("Длина окружности:", circle.circumference())

