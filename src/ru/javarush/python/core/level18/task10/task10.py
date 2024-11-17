# Сортировка кортежей

# Напишите функцию, которая использует сортировку вставками для сортировки списка кортежей по первому элементу каждого кортежа.


def insertion_sort_tuples(arr):
    # Проходим по всем элементам массива, начиная со второго
    for i in range(1, len(arr)):
        key = arr[i]
        # print(key)
        j = i - 1
        # Перемещаем элементы arr[0..i - 1], которые больше ключа, на одну позицию вперёд
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Вставляем ключ на правильное место
    return arr  # Возвращаем отсортированный массив


# Example usage:
tuples_list = [(3, 'c'), (1, 'a'), (2, 'b'), (4, 'd')]
sorted_list = insertion_sort_tuples(tuples_list)
print(sorted_list)