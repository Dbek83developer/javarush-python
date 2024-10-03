# Защищайтесь.

# Создайте класс Car, который будет иметь публичный атрибут brand и защищенный атрибут _model_.
# Добавьте методы для получения и установки значения защищенного атрибута _model.
# Создайте объект класса Car, установите значения атрибутов и выведите их на экран.

# Напишите тут ваш код
class Car:
    def __init__(self, brand):
        self.brand = brand
        self._model_ = ''

    def get_model(self):
        return self._model_

    def set_model(self, model):
        self._model_ = model


car = Car("GM")
car.set_model("Ravon3")
print(car.brand)
print(car.get_model())
