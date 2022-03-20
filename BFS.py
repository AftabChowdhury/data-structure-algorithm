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
        current_node = queue.pop(0)
        print(current_node, end=' ')
        for adjacent_node in graph:
            if adjacent_node not in visited:
                visited.add(adjacent_node)
                queue.append(adjacent_node)


bfs(visited, graph, 'A')

# class Node:
#   def __init__(self, name):
#     self.children = []
#     self.name = name
#
#   def addChild(self, name):
#     self.children.append(Node(name))
#     return self
#
#   def breadthFirstSearch(self, array):
#     # Write your code here.
#     queue = [self]
#     while queue:
#       current_node = queue.pop(0)
#       array.append(current_node)
#       for adjacent_node in current_node:
#         queue.append(adjacent_node)
#
#     return array
