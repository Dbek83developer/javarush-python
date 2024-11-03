# Создаем двумерный массив.
import numpy as np
# Создай квадратный массив 10х10 с использованием библиотеки numpy.
# Заполни его как таблицу умножения x*y. Выведи на экран.
# Класс list использовать нельзя.

matrix = np.empty((10, 10))
for i in range(10):
    for j in range(10):
        matrix[i, j] = (i+1)*(j+1)

print(matrix)
