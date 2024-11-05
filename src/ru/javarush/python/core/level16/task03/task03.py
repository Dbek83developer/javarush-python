# Бинарный поиск

# Напишите функцию, которая выполняет бинарный поиск заданного элемента в отсортированном массиве чисел.
# Функция должна возвращать индекс найденного элемента или -1, если элемент не найден.

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

# Пример использования:
sorted_array = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(sorted_array, target)
print(f"Элемент {target} найден на индексе {result}")