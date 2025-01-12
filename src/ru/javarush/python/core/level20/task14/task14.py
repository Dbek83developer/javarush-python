# Минимальный элемент

# Напишите функцию, которая возвращает n-й минимальный элемент в массиве.
# Пояснение: В массиве есть самый минимальный элемент, затем есть 2-й минимальные, 3-й минимальные и т.д.


def nth_minimum(arr, n):
    if n <= 0 or len(arr) < n:
        return None

    sorted_arr = sorted(arr)
    return sorted_arr[n-1]


# Пример использования:
arr = [7, 2, 5, 3, 9, 1]
n = 3
print(nth_minimum(arr, n))  # Output: 3