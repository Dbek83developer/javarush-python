# Все дороги ведут в Рим

# Найти кратчайшие пути между всеми парами вершин взвешенного графа.
# Подсказка: Используется таблица, где строки и столбцы соответствуют вершинам графа.
# Значение в ячейке представляет кратчайшее расстояние между двумя вершинами.

INF = float('inf')


def floyd_warshall(graph):
    v = len(graph)
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    print(dist)

    for k in range(v):
        for i in range(v):
            for j in range(v):
                # print(dist[i][j], dist[i][k] + dist[k][j])
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist



# Пример использования функции:
graph = [
    [0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]
]

shortest_paths = floyd_warshall(graph)
for row in shortest_paths:
    print(row)