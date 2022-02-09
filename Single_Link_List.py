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
        self.head = node

    def print_node_values(self):
        node = self.head
        while node:
            print('Node', node.node_value)
            node = node.next


objSingleLinkList = SingleLinkList()
objSingleLinkList.add_head(1)
objSingleLinkList.print_node_values()
