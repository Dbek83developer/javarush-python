# Общий подмассив

# Даны два массива чисел. Необходимо найти элементы первого массива, которые существуют во втором массиве.

def common_subarray(arr1, arr2):
    seen = set()
    duplicates = []
    for item in arr1:
        if item in arr2:
            duplicates.append(item)
        # else:
        #     seen.add(item)
    return duplicates


# Пример использования
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

result = common_subarray(arr1, arr2)
print(result)
