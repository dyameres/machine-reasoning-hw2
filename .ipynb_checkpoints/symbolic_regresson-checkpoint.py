#
#
# By Dylan Ameres and Tristan Allen

import random
from Node import Node
from evaluate import evaluate
from treeBuilder import buildTree

class Tree():
    
    def __init__(self, maxDepth):
        self.root = Node(random.choice(['+', '-', '/', '*']))
        buildTree(self, maxDepth)
        
    def createNode(self, value):
        """
        Utility function to create a node.
        """
        return Node(value)
        
    def fitness(self, x):
        # determine fitness of current tree
        # maybe mean square error
        value = evaluate(self.getRoot, x)
        return value

    def crossover(self, otherTree):
        # function for crossover
        return self.root
        
    def mutate(self,):
        # function for mutation
        return self.root

def printTree(root, level=0):
        children = []
        if root.left != None and root.right != None:
            children = [root.left, root.right]
        print("  " * level, root.value)
        # prints left branch above right branch
        for child in children:
            printTree(child, level + 1)

def main():
    choices = ["+", "-", "*", "/", 1, 2]
    rand_children = [2]
    for i in range(9):
        rand_children.append(random.randrange(0, 3, 2))
    
    tree1 = Node(random.choice(choices))
    tree1.insert(10)
    #buildTree(tree1)

    printTree(tree1)

if __name__ == "__main__":
    main()

# CITATIONS:
# https://www.researchgate.net/publication/10684490_Using_genetic_programming_to_discover_nonlinear_variable_interactions
