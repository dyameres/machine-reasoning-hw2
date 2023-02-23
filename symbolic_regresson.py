#
#
# By Dylan Ameres and Tristan Allen

import random

class Node():
    def __init__(self, value, left=None, right=None): #left and right are children
        self.left = left
        self.right = right
        self.value = value

    def insert(self, value):
        if self.value:
            if self.left is None:
                self.left = Node(value)
            elif self.right is None:
                self.right = Node(value)
        else:
            self.value = value

    # prints the value of the current node if Node object is printed
    def __str__(self):
        return self.value

class Tree():

    def createNode(self, value):
        """
        Utility function to create a node.
        """
        return Node(value)
        
    def getRoot(self):
        # return self.root
        return self
        
    def fitness(self,):
        # determine fitness of current tree
        # maybe mean square error
        return self

    def crossover(self, otherTree):
        # function for crossover
        return self
        
    def mutate(self,):
        # function for mutation
        return self


def buildTree(tree):
    # array = [2, 0, 2, 0, 0, 0, 2, 2, 2, 2, 2]
    choices = ["+", "-", "*", "/", 1, 2]
    random_node = random.choice(choices)

def printTree(root, level=0):
        children = []
        if root.left != None and root.right != None:
            children = [root.left, root.right]
        if root.left != None and root.right == None:
            children = [root.left]
        if root.left == None and root.right != None:
            children = [root.right]
        print("  " * level, root.value)
        for child in children:
            printTree(child, level + 1)

def main():
    choices = ["+", "-", "*", "/", 1, 2]
    rand_children = [2]
    for i in range(9):
        rand_children.append(random.randrange(0, 3, 2))
    
    tree1 = Node(random.choice(choices))
    tree1.insert(10)
    tree1.insert(20)
    tree1.insert(30)
    #buildTree(tree1)

    printTree(tree1)

if __name__ == "__main__":
    main()

# CITATIONS:
# https://www.researchgate.net/publication/10684490_Using_genetic_programming_to_discover_nonlinear_variable_interactions
