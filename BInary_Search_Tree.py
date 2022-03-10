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

    def print_tree(self):
        if self.left_node:
            self.left_node.print_tree()
        print(self.node_value)
        if self.right_node:
            self.right_node.print_tree()

root = Node(1)
root.add_new_node(2)
root.add_new_node(3)
root.add_new_node(1)
root.print_tree()

