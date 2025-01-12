# Должен остаться только один

# Удалить дубликаты из отсортированного массива.


def remove_duplicates(sorted_arr):
    n = len(sorted_arr)
    if not sorted_arr:
        return []
    res = [sorted_arr[0]]
    for i in range(1, n):
        if sorted_arr[i] != sorted_arr[i - 1]:
            res.append(sorted_arr[i])
    return res

# Пример использования
sorted_arr = [1, 1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(sorted_arr))  # Output: [1, 2, 3, 4, 5]