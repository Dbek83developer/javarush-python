# Случайный аргумент
import random


# Напишите функцию  print_random(a,b,c), которая выводит на экран случайно выбранный переданный аргумент.

# Напишите тут ваш код
def print_random(a, b, c):
    print(random.choice([a, b, c]))


# print_random(2, 3, 5)