class Node:
    def __init__(self, value):
        self.left_node = None
        self.right_node = None
        self.node_value = value

    def add_new_node(self, value):
        if self.node_value == value:
            print('Node already exist, node:', value)
            return
        if value < self.node_value:
            if self.left_node is None:
                self.left_node = Node(value)
            else:
                self.left_node.add_new_node(value)
        elif value > self.node_value:
            if self.right_node is None:
                self.right_node = Node(value)
            else:
                self.right_node.add_new_node(value)
        return self

    def search_node(self, value):
        if value == self.node_value:
            print('Node found, Node: ', value)
            return
        elif value < self.node_value:
            if self.left_node is None:
                print('Node not found, Node: ', value)
                return
            self.left_node.search_node(value)
        elif value > self.node_value:
            if self.right_node is None:
                print('Node not found, Node: ', value)
                return
            self.right_node.search_node(value)

    def print_tree(self):
        if self.left_node:
            self.left_node.print_tree()
        print(self.node_value)
        if self.right_node:
            self.right_node.print_tree()


root = Node(3)
root.add_new_node(2)
root.add_new_node(4)
root.add_new_node(1)
root.add_new_node(5)
root.add_new_node(4)
root.print_tree()
root.search_node(1)
root.search_node(10)
