# Это жизнь

# Вам необходимо отсортировать массив на устройстве с ограниченной памятью, где доступно всего 1 КБ дополнительной памяти.
# Какой алгоритм сортировки вы выберете?  Напишите его.

# Напишите тут ваш код

def in_place_quick_sort(arr, low, high):
    if low < high:
        index = partition(arr, low, high)
        in_place_quick_sort(arr, low, index - 1)
        in_place_quick_sort(arr, index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(arr)
    return i + 1

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
print(arr)
in_place_quick_sort(arr, 0, len(arr) - 1)
print(arr)