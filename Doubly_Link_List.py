class Node:
    def __init__(self, value):
        self.node_value = value
        self.next = None
        self.previous = None


class DoublyLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_head(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def print_values(self):
        traverse_node = self.head
        while traverse_node:
            print('Node: ', traverse_node.node_value)
            traverse_node = traverse_node.next


objDoubly_Link_List = DoublyLinkList()
objDoubly_Link_List.add_head(1)
objDoubly_Link_List.print_values()
