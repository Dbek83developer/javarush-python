# Детектив

# Напиши функцию set_detector, которая проходится по списку(кортежу) своих аргументов и определяет - есть среди них множество или нет.
# Вызови функцию set_detector с разными вариантами параметров (с множеством и без).

# Напишите тут ваш код
alist = (1, 2, 3, 4, 'f', 3, 'dd')
tuple_1 = tuple(alist)
set_1 = set(alist)


def set_detector(*args):
    for item in args:
        # print(item)
        # print(type(item))
        if set == type(item):
            return True
    return False


set_detector(alist, tuple_1, set_1, )
set_detector(alist, tuple_1)
