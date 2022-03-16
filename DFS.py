graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print('Node: ', node)
        visited.add(node)
        for next_node in graph[node]:
            dfs(visited, graph, next_node)


dfs(visited, graph, 'A')
