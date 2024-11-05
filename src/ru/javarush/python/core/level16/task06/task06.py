# Лучший поиск
import array
import time
import random
# Напишите программу которая выяснит, что какой способ поиска в массиве из 1000 элементов быстрее:
# Способ 1: 10 раз воспользоваться линейным поиском.
# Способ 2: отсортировать массив + 10 раз воспользоваться бинарным поиском.


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def measure_time(search_func, arr, target):
    start_time = time.time()
    for _ in range(10):
        search_func(arr, target)
    end_time = time.time()
    return end_time - start_time


matrix = [random.randint(1, 10000) for _ in range(1000)]
sorted_matrix = sorted(matrix)

target = -1
linear_time = measure_time(linear_search, matrix, target)
binary_time = measure_time(binary_search, sorted_matrix, target)
print(f"Linear search time: {linear_time:.12f}, Binary search time: {binary_time:.12f}")
#
# print(matrix)
# print(sorted_matrix)
