# Подмассив

# Дан массив длинны n состоящий из целых чисел.
# Найти подмассив фиксированного размера k с максимальной суммой.


def max_subarray_sum(arr, k):
    n = len(arr)
    # summa = 0
    mas = [0]
    for i in range(n - k + 1):
        summa = 0
        for j in range(i, k + i):
            summa += arr[j]
        if mas[0] < summa:
            mas[0] = summa

    return mas[0]

# Пример использования
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print(max_subarray_sum(arr, k))  # Вывод: 24 (7 + 8 + 9)