# Сортировка чисел

# Напишите функцию, которая использует сортировку выбором для сортировки списка чисел по возрастанию.


def selection_sort(arr):
    n = len(arr)
    srt_arr = arr
    for i in range(n):
        index = i
        for j in range(i + 1, n):
            if srt_arr[j] < srt_arr[index]:
                index = j
        srt_arr[i], srt_arr[index] = srt_arr[index], srt_arr[i]
    return srt_arr

# Пример использования
numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)  # Вывод: [11, 12, 22, 25, 64]