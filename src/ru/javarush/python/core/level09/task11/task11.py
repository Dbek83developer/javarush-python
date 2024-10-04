# Полиморфизм.

# Создайте базовый класс Shape с методом area, который будет возвращать площадь фигуры.
# Затем создайте дочерние классы Circle и Rectangle, которые будут переопределять метод area для расчета площади своих фигур.
# Используйте полиморфизм, чтобы создать список фигур и вычислить их площади.

import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method!")


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        pi = 3.14
        return pi*self.r**2


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
areas = [shape.area() for shape in shapes]

for area in areas:
    print(area)