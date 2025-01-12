# Случайный миллион

# Создайте массив из 1 миллиона элементов случайных значений.
# Используйте функции merge_sort и quick_sort для сортировки значений.
# Выедите результаты на экран.


import random
import time

# Генерация массива из 1 миллиона случайных значений
array = [random.randint(0, 1000000) for _ in range(1000000)]


# Реализация функции merge_sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Реализация функции quick_sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Сортировка и вывод времени выполнения для merge_sort
start_time = time.time()
sorted_array_merge = merge_sort(array.copy())
merge_sort_time = time.time() - start_time
print(f"Merge Sort Time: {merge_sort_time} seconds")
# print(sorted_array_merge)

# Сортировка и вывод времени выполнения для quick_sort
start_time = time.time()
sorted_array_quick = quick_sort(array.copy())
quick_sort_time = time.time() - start_time
print(f"Quick Sort Time: {quick_sort_time} seconds")
# print(sorted_array_quick)
