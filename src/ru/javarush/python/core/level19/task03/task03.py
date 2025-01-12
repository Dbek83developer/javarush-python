# Сумма чисел

# Найти два числа в отсортированном массиве, которые в сумме дают заданное число target


def find_two_numbers(arr, target):
    # n = len(arr)
    mas = list()
    # first = arr[0]
    # for i in range(1, n):
    #     if arr[i] + first == target:
    #         mas.append(first)
    #         mas.append(arr[i])
    # return mas

    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            mas.append((arr[left], arr[right]))
            # return arr[left], arr[right]
            left += 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return mas


# Пример использования
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
result = find_two_numbers(sorted_array, target)
print(result)
if result:
    print(f"Сумма чисел {result[0]} и {result[1]} равна {target}")
else:
    print(f"Пары чисел, дающих в сумме {target}, не найдено")