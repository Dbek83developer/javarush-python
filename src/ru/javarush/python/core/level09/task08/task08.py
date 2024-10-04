# Фигуры.

# Создайте базовый класс Shape, который будет иметь метод area для вычисления площади.
# Затем создайте два дочерних класса Rectangle и Circle, которые будут наследовать от Shape
# и переопределять метод area для вычисления площади прямоугольника и круга соответственно.
import math


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        pi = 3.14
        return pi * self.r**2


# Пример использования
rect = Rectangle(3, 4)
print(f"Area of rectangle: {rect.area()}")

circle = Circle(5)
print(f"Area of circle: {circle.area()}")