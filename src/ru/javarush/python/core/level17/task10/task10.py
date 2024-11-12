# Связный граф

# Напишите функцию для проверки, является ли граф связным, с использованием DFS.
# Функция должна принимать граф в виде списков смежности и возвращать True, если граф связный,
# и False в противном случае.


def dfs(graph, visited, node):
    # if visited is None:
    #     visited = set()
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, visited, neighbor)



def is_connected(graph):
    if not graph:
        return False
    # Initialize a set to keep track of visited nodes
    visited = set()
    start_node = list(graph.keys())[0]


    # Call the DFS function
    dfs(graph, visited, start_node)

    # Check if all nodes were visited
    return len(visited) == len(graph)


# Пример использования:
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}
print(is_connected(graph))  # Output: True
