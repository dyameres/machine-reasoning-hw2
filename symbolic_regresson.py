#
#
# By Dylan Ameres and Tristan Allen

import random

class Node():
    def __init__(self, value, left=None, right=None): #left and right are children
        self.left = left
        self.right = right
        self.value = value

    # prints the value of the current node if Node object is printed
    def __str__(self):
        return self.value

class Tree():
    def __init__(self, value):
        root = Node(value)
        self.buildTree(root)

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

    def buildTree(self, root):
        # array = [2, 0, 2, 0, 0, 0, 2, 2, 2, 2, 2]
        #Recursive solution, flip a coin between choices
        #base case: when the node is an integer or x
        print("TYPE:", type(root))

        choices = ["+", "-", "*", "/", 1, 2]
        #self.root = random.choice(choices)
        if root.left == None:
            self.buildTree(root.left)
        if root.right == None:
            self.buildTree(root.right)


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
    
    tree1 = Tree(10)

    printTree(tree1)

if __name__ == "__main__":
    main()

# CITATIONS:
# https://www.researchgate.net/publication/10684490_Using_genetic_programming_to_discover_nonlinear_variable_interactions
