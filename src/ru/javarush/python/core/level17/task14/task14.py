# Города и списки

# У вас есть алгоритм Дейкстры реализованный для матрицы смежности.
# Переделайте его для графе заданного списком смежности.


import heapq

def dijkstra(adj_list, start):
    # Инициализация
    distances = {vertex: float('infinity') for vertex in adj_list}
    distances[start] = 0
    priority_queue = [(0, start)]
    parents = {vertex: None for vertex in adj_list}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если текущее расстояние больше записанного, пропускаем вершину
        if current_distance > distances[current_vertex]:
            continue

        # Обновление расстояний до соседних вершин
        for neighbor, weight in adj_list[current_vertex]:
            distance = current_distance + weight

            # Если найден более короткий путь к соседней вершине
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, parents


# Пример использования:
adj_list = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
start = 0
print(dijkstra(adj_list, start))