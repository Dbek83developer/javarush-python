# Автопарк.

# Напишите функцию check_subclass для проверки, является ли один класс подклассом другого.
# Используйте функцию issubclass() для выполнения проверки.
# Затем создайте классы Vehicle, Car, Bicycle, и проверьте, являются ли Car и Bicycle подклассами Vehicle.

# Напишите тут ваш код
def check_subclass(first, second):
    return issubclass(first, second)


class Vehicle:
    pass


class Car(Vehicle):
    pass


class Bicycle(Vehicle):
    pass


print(check_subclass(Car, Vehicle))
print(check_subclass(Bicycle, Vehicle))
