graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()
queue = []


def bfs(visited, graph, node):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=' ')
        for adjacent_node in graph:
            if adjacent_node not in visited:
                visited.add(adjacent_node)
                queue.append(adjacent_node)


bfs(visited, graph, 'A')
