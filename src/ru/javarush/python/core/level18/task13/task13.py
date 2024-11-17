# Объединение массивов

# У тебя есть два отсортированных массива чисел, напиши код, который объединит их в один отсортированный массив.


def merge_sorted_arrays(arr1, arr2):
    i = j = k = 0
    arr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
        k += 1

        # Проверка на оставшиеся элементы
    while i < len(arr1):
        arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        arr.append(arr2[j])
        j += 1
    return arr


# Пример использования
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merged_array = merge_sorted_arrays(arr1, arr2)
print(merged_array)  # Вывод: [1, 2, 3, 4, 5, 6, 7, 8]