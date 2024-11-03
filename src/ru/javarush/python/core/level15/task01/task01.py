# Настоящий массив.
import array
import random
# Создай массив с использованием библиотеки array.
# Добавь в него 10 случайных чисел от 0 до 1000. Отсортируй и выведи на экран.
# Класс list использовать нельзя.


def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n - i - 1):
            # Сравниваем соседние элементы
            if arr[j] > arr[j + 1]:
                # Меняем элементы местами, если они в неправильном порядке
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = array.array("i")
for num in range(10):
    arr.append(random.randint(1, 1000))
print(arr)
print(bubble_sort(arr))
