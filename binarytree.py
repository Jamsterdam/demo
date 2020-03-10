class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def printTree(self):

        if self.left:
            self.left.printTree()
        print(self.data)

        if self.right:
            self.right.printTree()

    def insert_node(self, newnode):
        if self.data:
            if newnode < self.data:
                if self.left is None:
                    self.left = Node(newnode)
                else:
                    self.left.insert_node(newnode)
            elif newnode > self.data:
                if self.right is None:
                    self.right = Node(newnode)
                else:
                    self.right.insert_node(newnode)
        else:
            self.data = newnode


root = Node(10)
root.insert_node(5)
root.insert_node(7)
root.insert_node(12)
root.insert_node(-5)

root.printTree()
