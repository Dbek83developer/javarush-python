# Путь между городами

# Напишите функцию для нахождения кратчайшего пути между двумя городами в транспортной сети
# с использованием алгоритма Дейкстры.
# Функция должна возвращать кратчайший путь и его стоимость.

import heapq


def dijkstra(graph, start, end):
    # Priority queue to hold (cost, node, path) tuples
    queue = [(0, start, [])]
    # Dictionary to store the minimum cost to reach each node
    visited = {}

    while queue:
        # Get the node with the lowest cost
        (cost, node, path) = heapq.heappop(queue)

        # Skip if the node has been visited with a lower cost
        if node in visited and visited[node] <= cost:
            continue

        # Mark the node as visited with the current cost
        visited[node] = cost
        # Update the path
        path = path + [node]

        # If we reach the target, return the path and total cost
        if node == end:
            return path, cost

        # Check neighbors and add them to the queue with updated costs
        for neighbor, travel_cost in graph.get(node, {}).items():
            if neighbor not in visited or cost + travel_cost < visited[neighbor]:
                heapq.heappush(queue, (cost + travel_cost, neighbor, path))

    # If no path is found, return None
    return None, float("inf")


# Пример графа: словарь, где ключ - город, а значение - словарь соседей и расстояний до них
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Пример использования функции
start_city = 'A'
end_city = 'D'
distance, path = dijkstra(graph, start_city, end_city)
print(f"Кратчайший путь от {start_city} до {end_city} стоит {distance} и проходит через {path}.")