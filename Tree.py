#
#
# By Dylan Ameres and Tristan Allen

import random
from Node import Node

class Tree():
    
    def __init__(self, maxDepth=2, realTree=None): # defaults to tree of depth 2 if no parameter given
        if realTree == None:
            self.root = Node(random.choice(['+', '-', '/', '*']))
            self.buildTree(self.root, 1, maxDepth) # constructs the tree
            self.depth = maxDepth
        else:
            self.root = self.copyTree(realTree.root)
            self.depth = realTree.depth
        
    # Recursively builds the tree to the specified max depth
    # parameters: 
    #     curNode - Node object of the current node to create children for
    #     curDepth - int of what layer the current node is at 
    #     maxDepth - int of how many layers to build the tree out
    def buildTree(self, curNode, curDepth, maxDepth):
        ops = ['+', '-', '*', '/']
        if curDepth < maxDepth:
            curNode.left = Node(random.choice(ops))
            self.buildTree(curNode.left, curDepth+1, maxDepth)
            curNode.right = Node(random.choice(ops))
            self.buildTree(curNode.right, curDepth+1, maxDepth)
        else:
            # using 2:1 for integers to x's to avoid too many x's but could change in future
            curNode.left = Node(random.choice([random.randrange(-2, 3), random.randrange(-2, 3), 'x']))
            curNode.right = Node(random.choice([random.randrange(-2, 3), random.randrange(-2, 3), 'x']))
            
    # Recursively creates a copy of the original tree for manipulation
    # parameters:
    #     curNode - Node of the current node to copy
    # returns: Node, returns the copied node
    def copyTree(self, curNode):
        copyNode = Node(curNode.value)
        try:
            copyNode.left = self.copyTree(curNode.left)
        except AttributeError:
            pass
        try:
            copyNode.right = self.copyTree(curNode.right)
        except AttributeError:
            pass
        return copyNode
    
    # Finds the fitness of the current tree with a given data set 
    # using the mean squared error to determine fitness 
    # parameters: 
    #     dataSet - list of pairs of floats/int representing [[x1, f(x1)], [x2, f(x2)], ...]
    # returns: float, returns the mean square error of the data set and current tree 
    def fitness(self, dataSet):
        MSE = 0 
        for i in range(len(dataSet)):
            MSE += (self.evaluate(self.root, dataSet[i][0]) - dataSet[i][1])**2 # calculate mse for each data point
        return MSE
    
    # Evaluates a symbolic regression tree recursively through tree 
    # traversal using Node objects and their children
    # parameters:
    #     curNode - a Node object to evaluate the current value
    #     x - int/float which is the current 'x' to evaluate the function at
    # returns: float, returns the value after evaluating the tree at 
    #          the current 'x' value 
    def evaluate(self, curNode, x):
        if curNode.value == '+':
            return self.evaluate(curNode.left, x) + self.evaluate(curNode.right, x)
        elif curNode.value == '-':
            return self.evaluate(curNode.left, x) - self.evaluate(curNode.right, x)
        elif curNode.value == '*':
            return self.evaluate(curNode.left, x) * self.evaluate(curNode.right, x)
        elif curNode.value == '/':
            right = self.evaluate(curNode.right, x)
            if right != 0:
                return self.evaluate(curNode.left, x) / right
            else:
                return 1
        elif curNode.value == 'x':
            return x
        else: 
            return curNode.value

    # TODO (not critical): make this return the tree instead of print
    def printTree(self, root, level=0):
        children = []
        if root.left != None and root.right != None:
            children = [root.left, root.right]
        print("  " * level, root.value)
        # prints left branch above right branch
        for child in children:
            self.printTree(child, level + 1)
            
    def __str__(self):
        self.printTree(self.root)
        return 'current tree'

# CITATIONS:
# https://www.researchgate.net/publication/10684490_Using_genetic_programming_to_discover_nonlinear_variable_interactions
