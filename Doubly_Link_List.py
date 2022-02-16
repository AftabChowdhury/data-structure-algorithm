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
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            node.next = self.head
            self.head = node
            self.size += 1

    def add_last_node(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
            self.size += 1

    def print_values(self):
        traverse_node = self.head
        while traverse_node:
            print('Node: ', traverse_node.node_value)
            traverse_node = traverse_node.next

    def print_reverse_values(self):
        traverse_node = self.tail
        while traverse_node:
            print('Node: ', traverse_node.node_value)
            traverse_node = traverse_node.previous


objDoubly_Link_List = DoublyLinkList()
objDoubly_Link_List.add_head(1)
objDoubly_Link_List.add_last_node(2)
objDoubly_Link_List.add_last_node(3)
objDoubly_Link_List.add_last_node(4)
print('Forward List')
objDoubly_Link_List.print_values()
print('Reverse List')
objDoubly_Link_List.print_reverse_values()
