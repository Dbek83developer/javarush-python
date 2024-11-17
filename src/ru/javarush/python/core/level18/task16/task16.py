# Выбор среднего элемента

# Добавь в функцию quick_sort возможность передавать способ выбора среднего значение через lambda-функцию.
# Предложи 5 вариантов выбора среднего числа для быстрой сортировки.

# Напишите тут ваш код

def quick_sort(arr, pivot_selection):
    if len(arr) <= 1:
        return arr  # Базовый случай: массив с 0 или 1 элементом уже отсортирован

    pivot = pivot_selection(arr)  # Выбираем опорный элемент
    left = [x for x in arr if x < pivot]  # Элементы, меньшие опорного
    middle = [x for x in arr if x == pivot]  # Элементы, равные опорному
    right = [x for x in arr if x > pivot]  # Элементы, большие опорного

    return quick_sort(left, pivot_selection) + middle + quick_sort(right, pivot_selection)

# 5 вариантов выбора функции pivot_selection
# 1. Первый элемент
pivot_first = lambda arr: arr[0]

# 2. Последний элемент
pivot_last = lambda arr: arr[len(arr) - 1] # Напишите тут ваш код

# 3. Средний элемент
pivot_middle = lambda arr: arr[len(arr) // 2] # Напишите тут ваш код

# 4. Случайный элемент
import random
pivot_random = lambda arr: arr[random.randint(0, len(arr) - 1)] # Напишите тут ваш код

# 5. Среднее арифметическое из трех: первый, последний и средний
pivot_median_three = lambda arr: (arr[0] + arr[len(arr) // 2] + arr[len(arr) - 1]) // 3 # Напишите тут ваш код

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
print(quick_sort(arr, pivot_first))
print(quick_sort(arr, pivot_last))
print(quick_sort(arr, pivot_middle))
print(quick_sort(arr, pivot_random))
print(quick_sort(arr, pivot_median_three))
