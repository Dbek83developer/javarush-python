# Домашние животные.

# Напишите функцию check_type для проверки, является ли переданный объект экземпляром класса Animal или его подклассов.
# Используйте функцию isinstance() для выполнения проверки.
# Затем создайте классы Animal, Dog, Cat и проверьте несколько объектов.

# Напишите тут ваш код
def check_type(cls):
    return isinstance(cls, Animal)


class Animal:
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
cat = Cat()
print(check_type(dog))
print(check_type(cat))
