# Сортировка выбором

# Напишите функцию, которая использует сортировку выбором для сортировки списка строк по их длине.

def selection_sort_by_length(strings):
    n = len(strings)
    sorted_str = strings
    for i in range(n):
        min_id = i
        for j in range(i + 1, n):
            if len(sorted_str[j]) < len(sorted_str[min_id]):
                min_id = j
        sorted_str[i], sorted_str[min_id] = sorted_str[min_id], sorted_str[i]
    return sorted_str


# Пример использования
strings = ["apple", "dog", "banana", "cat", "elephant"]
sorted_strings = selection_sort_by_length(strings)
print(sorted_strings)  # ['dog', 'cat', 'apple', 'banana', 'elephant']