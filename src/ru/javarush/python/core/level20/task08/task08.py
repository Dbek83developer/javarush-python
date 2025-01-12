# Параллельный факториал

# Напишите программу, которая использует параллельное программирование для вычисления факториала большого числа.
# Разделите задачу на несколько процессов, каждый из которых будет вычислять часть произведения.
# Подсказка: Используйте модуль multiprocessing в Python для создания нескольких процессов.
# Разделите задачу вычисления факториала на подзадачи, каждая из которых будет вычислять произведение своего подотрезка.

import multiprocessing
from functools import reduce
from operator import mul


def partial_factorial(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result


def factorial(n, num_processes):
    if n == 0 or n == 1:
        return 1

    # Split the range into roughly equal parts
    chunk_size = n // num_processes
    ranges = [(i * chunk_size + 1, (i + 1) * chunk_size) for i in range(num_processes - 1)]
    ranges.append(((num_processes - 1) * chunk_size + 1, n))

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(partial_factorial, ranges)

    final_result = reduce(mul, results)
    return final_result


if __name__ == '__main__':
    number = 1000  # Example large number
    num_processes = 4  # Number of processes to use
    result = factorial(number, num_processes)
    print(f"The factorial of {number} is {result}")