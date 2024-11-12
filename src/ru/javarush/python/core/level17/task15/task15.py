# Топологическя сортировка
# У вас есть список задач и их зависимости. Напишите функцию для определения порядка выполнения задач
# с использованием топологической сортировки через поиск в глубину (DFS).
# Функция должна возвращать список задач в правильном порядке.

# Helper function for DFS
from collections import defaultdict, deque

# Create adjacency list
graph = defaultdict(list)

# Visited nodes tracker
visited = set()
temp_marks = set()
stack = list()


def dfs(node):
    if node in temp_marks:
        raise ValueError("Graph is not a Directed Acyclic Graph (DAG)")

    if node not in visited:
        temp_marks.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)
        temp_marks.remove(node)
        visited.add(node)
        stack.append(node)


def topological_sort(tasks):
    for dest, src in tasks:
        graph[src].append(dest)

    # Perform DFS on each node
    all_nodes = {node for edge in tasks for node in edge}
    for node in all_nodes:
        if node not in visited:
            dfs(node)

    return stack[::-1]  # Результат в обратном порядке

# Example usage:
tasks = [('a', 'b'), ('b', 'c'), ('c', 'd')]
print(topological_sort(tasks))  # Output: ['d', 'c', 'b', 'a']