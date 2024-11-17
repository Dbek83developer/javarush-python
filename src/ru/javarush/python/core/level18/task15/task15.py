# Быстрая сортировка

# Напишите функцию, которая реализует алгоритм быстрой сортировки для сортировки массива чисел.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Базовый случай: массив с 0 или 1 элементом уже отсортирован

    pivot = arr[len(arr) // 2]  # Выбираем опорный элемент
    left = [x for x in arr if x < pivot]  # Элементы, меньшие опорного
    middle = [x for x in arr if x == pivot]  # Элементы, равные опорному
    right = [x for x in arr if x > pivot]  # Элементы, большие опорного

    return quick_sort(left) + middle + quick_sort(right)


# Пример использования
array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = quick_sort(array)
print(sorted_array)