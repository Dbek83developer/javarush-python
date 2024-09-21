# Случайная функция
import random


# Напишите функцию generate_random_number(), которая выводит на экран случайное число от -200 до 0.

# Напишите тут ваш код
def generate_random_number():
    rand_num = random.randint(-200, 0)
    print(rand_num)


generate_random_number()
