# Связный гаф: BFS-версия

# Напишите функцию для проверки, является ли граф связным с использованием BFS.
# Функция должна принимать граф в виде списков смежности и возвращать True, если граф связный,
# и False в противном случае.

from collections import deque

def is_connected(graph):
    if not graph:
        return False
    visited = set()
    queue = deque([list(graph.keys())[0]])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            # print(vertex)  # Обработка узла

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return len(graph) == len(visited)

# Пример использования:
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}
print(is_connected(graph))  # True