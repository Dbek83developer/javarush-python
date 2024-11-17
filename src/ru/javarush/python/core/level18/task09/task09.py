# Сортировка вставками

# Напишите функцию, которая использует сортировку вставками для сортировки списка строк в алфавитном порядке.


def insertion_sort(strings):
    for i in range(1, len(strings)):
        key = strings[i]
        j = i - 1
        # Перемещаем элементы arr[0..i - 1], которые больше ключа, на одну позицию вперёд
        while j >= 0 and key < strings[j]:
            strings[j + 1] = strings[j]
            j -= 1
        strings[j + 1] = key  # Вставляем ключ на правильное место
    sorted = strings
    return sorted  # Возвращаем отсортированный массив


# Пример использования:
strings = ["banana", "apple", "cherry", "date"]
sorted_strings = insertion_sort(strings)
print(sorted_strings)  # Output: ['apple', 'banana', 'cherry', 'date']