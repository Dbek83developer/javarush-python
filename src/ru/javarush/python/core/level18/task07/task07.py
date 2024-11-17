# Сортировка пузырьком

# Напишите функцию, которая использует сортировку пузырьком для сортировки списка строк по их длине.

def bubble_sort_by_length(arr):
    n = len(arr)
    for i in range(n):
        # swapped = False
        for j in range(0, n - 1 - i):
            # print(arr[j])
            if len(arr[j]) > len(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
            #     swapped = True
            # if not swapped:
            #     break
    return arr


# Пример использования
strings = ["apple", "banana", "kiwi", "cherry", "mango"]
sorted_strings = bubble_sort_by_length(strings)
print(sorted_strings)