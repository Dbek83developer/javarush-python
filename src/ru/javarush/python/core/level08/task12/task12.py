# Длительность работы.
import time
import os


# Напишите программу, которая создает декоратор для измерения времени выполнения функции.
# Программа должна:
# Определить декоратор time_decorator, который измеряет и выводит время выполнения функции.
# Применить декоратор к функции compute_square(n), которая вычисляет квадрат числа и имитирует задержку с помощью time.sleep().
# Вызвать функцию compute_square(n).

# Напишите тут ваш код
import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start the timer
        result = func(*args, **kwargs)  # Call the original function with its arguments
        end_time = time.time()  # End the timer
        print(f"Execution time: {end_time - start_time} seconds")
        return result  # Return the result of the original function
    return wrapper

@time_decorator
def compute_square(n):
    time.sleep(5)
    return n * n


# Call the function
compute_square(9)

