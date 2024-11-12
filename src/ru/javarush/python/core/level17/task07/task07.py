# Утро Адама: ищем ребро

# Напишите функцию для проверки наличия ребра между двумя вершинами в графе, представленном в виде матрицы смежности.
# Функция должна принимать матрицу смежности и два индекса вершин и возвращать True,
# если между вершинами существует ребро, и False в противном случае.


def has_edge(matrix, vertex1, vertex2):
    # print(len(matrix))
    if not len(matrix) > vertex1 or len(matrix) > vertex2 or vertex1 < 0 or vertex2 < 0:
        return False
    if matrix[vertex1][vertex2] == 1:
        return True
    else:
        return False


# Пример использования:
adj_matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

print(has_edge(adj_matrix, 0, 1))  # True
print(has_edge(adj_matrix, 0, 2))  # False