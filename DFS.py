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

# class Node:
#     def __init__(self, name):
#         self.children = []
#         self.name = name
#
#     def addChild(self, name):
#         self.children.append(Node(name))
#         return self
#
#     def depthFirstSearch(self, array):
#         # Write your code here.
# 		array.append(self.name)
# 		for child_node in self.children:
# 			child_node.depthFirstSearch(array)
# 		return array
