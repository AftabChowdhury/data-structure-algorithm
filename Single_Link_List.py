class Node:
    def __init__(self, value):
        self.node_value = value
        self.next = None


class SingleLinkList:
    def __init__(self):
        self.head = None

    def add_head(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node.node_value
