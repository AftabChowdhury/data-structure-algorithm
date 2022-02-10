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

    def add_last_node(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            last = self.head
            while last.next:
                last = last.next

            last.next = node

    def add_node_after_specific_node(self, value, specific_node):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = specific_node.next
            specific_node.next = node

    def delete_node(self, value):
        if self.head is None:
            return
        else:
            node = self.head
            if node.node_value == value:
                self.head = node.next
                return
            while node:
                if node.node_value == value:
                    break
                previous = node
                node = node.next

            previous.next = node.next

    def print_node_values(self):
        node = self.head
        while node:
            print('Node', node.node_value)
            node = node.next


objSingleLinkList = SingleLinkList()
objSingleLinkList.add_head(1)
objSingleLinkList.add_last_node(2)
objSingleLinkList.add_node_after_specific_node(3, objSingleLinkList.head)
objSingleLinkList.delete_node(3)
objSingleLinkList.print_node_values()
