# Системные функции.

# Напишите программу, которая создает несколько объектов различных типов и
# использует функции id(), hash(), и dir() для выполнения следующих операций:
# Определить и вывести уникальные идентификаторы объектов с помощью id().
# Вывести хеш-значения хешируемых объектов с помощью hash().
# Вывести список атрибутов и методов объекта с помощью dir().

# Напишите тут ваш код
class MyClass:
    def __init__(self):
        self.name = "Alice"

    def greet(self):
        print("Hello, " + self.name)


obj = MyClass()
a = [1, 2, 3,]
b = (1, 2, 3)
text = "Salom"
num = 1233123123
print(id(a))
print(id(b))
print(hash(num))
print(hash(text))
print(hash(b))
# print(hash(obj))
print(dir(obj))
print(dir(b))
print(dir(a))
print(dir(text))
print(dir(num))
