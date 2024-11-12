# Кратчайший путь: BFS-версия

# Напишите функцию для поиска кратчайшего пути от начальной вершины до целевой
# в неориентированном графе с использованием BFS.
# Функция должна возвращать список вершин, составляющих кратчайший путь.

from collections import deque

def find_shortest_path(graph, start, goal):
    # Queue to keep track of paths
    queue = deque([[start]])
    # Set to keep track of visited nodes
    visited = set()

    # Begin BFS
    while queue:
        # Get the first path from the queue
        path = queue.popleft()
        # Get the last node from the path
        node = path[-1]

        # Check if we've reached the target
        if node == goal:
            return path

        # Mark the node as visited
        if node not in visited:
            visited.add(node)
            # Explore neighbors
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    # Create a new path with the neighbor and add it to the queue
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

    # If there's no path from start to target
    return []


# Пример использования:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
goal = 'F'
print(find_shortest_path(graph, start, goal))