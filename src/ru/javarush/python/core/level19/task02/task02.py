# Решение в лоб

# Написать решение в лоб для подсчёта количества вхождений каждого элемента в массиве.

def count_occurrences(arr):
    count_dict = {}
    n = len(arr)
    for item in arr:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    return count_dict


# Пример использования:
arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(count_occurrences(arr))
