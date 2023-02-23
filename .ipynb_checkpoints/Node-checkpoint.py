# Node class for tree building 
class Node():
    def __init__(self, value, left=None, right=None): #left and right are children
        self.left = left
        self.right = right
        self.value = value

    def insert(self, value):
        if self.left is None:
            self.left = Node(value)
        else:
            self.left.insert(value)
        if self.right is None:
            self.right = Node(value)
        else:
            self.right.insert(value)

    # prints the value of the current node if Node object is printed
    def __str__(self):
        return self.value
