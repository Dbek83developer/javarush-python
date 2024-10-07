# Использованиее метода reduce()

# Напишите класс, который управляет своей сериализацией с помощью метода __reduce__(),
# чтобы при сериализации и десериализации сохранялись только определенные поля.

# Напишите тут ваш код
import pickle

class CustomClass:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


    def __reduce__(self):
        return (self.__class__, (self.name, self.age))

    def __repr__(self):
        return f"CustomClass(name={self.name}, age={self.age})"


# Создание объекта
obj = CustomClass("Alex", 25, "London")

# Сериализация объекта
serialized_obj = pickle.dumps(obj)
print("Сериализованный объект:", serialized_obj)

# Десериализация объекта
deserialized_obj = pickle.loads(serialized_obj)
print("Десериализованный объект:", deserialized_obj)