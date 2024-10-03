# Создаем объекты.

# Создайте класс Car с атрибутами make, model и year.
# Добавьте метод display_info(), который выводит информацию о машине.
# Затем создайте объект этого класса и вызовите метод display_info().

# Напишите тут ваш код
class Car:
    make = "GM"
    model = "Ravon3"
    year = 2018

    def display_info(self):
        print(f"{self.make}, {self.model}, {self.year}")


my_car = Car()
my_car.display_info()