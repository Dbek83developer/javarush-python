# Создаем свой массив
import numpy as np
# Создай массив с использованием библиотеки numpy.
# Добавь в него 10 случайных чисел от 0 до 1000. Отсортируй и выведи на экран.
# Класс list использовать нельзя.
# Sozdayem massiv
matrix = np.random.randint(0, 1000, 10)

# Sortirovka
sorted_array = np.sort(matrix)

# Pechat otsortirovanniy massiv
print(sorted_array)