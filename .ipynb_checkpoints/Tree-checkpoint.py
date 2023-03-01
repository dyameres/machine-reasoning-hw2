#
#
# By Dylan Ameres and Tristan Allen

import random
from Node import Node

class Tree():
    
    def __init__(self, maxDepth=2, copyTree=None): # defaults to tree of depth 2 if no parameter given
        if copyTree == None:
            self.root = Node(random.choice(['+', '-', '/', '*']))
            self.buildTree(self.root, 1, maxDepth) # constructs the tree
            self.depth = maxDepth
        else:
            self.root = self.copyTree(copyTree.root)
            self.depth = copyTree.depth
        
    # Recursively builds the tree to the specified max depth
    # parameters: 
    #     curNode - Node object of the current node to create children for
    #     curDepth - int of what layer the current node is at 
    #     maxDepth - int of how many layers to build the tree out
    # TODO: add x1, x2, ...
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
        print(dataSet)
        MSE = 0 
        for i in range(len(dataSet)):
            xValues = {}
            for j in range(len(dataSet[i]) - 1):
                xValue['x' + str(j)] = dataSet[i][j]
            MSE += (self.evaluate(self.root, xValues) - dataSet[i][-1])**2 # calculate mse for each data point
        return MSE / len(dataSet)
    
    # Evaluates a symbolic regression tree recursively through tree 
    # traversal using Node objects and their children. Helper function
    # for the fitness method.
    # parameters:
    #     curNode - a Node object to evaluate the current value
    #     x - int/float which is the current 'x' to evaluate the function at
    # returns: float, returns the value after evaluating the tree at 
    #          the current 'x' value 
    # TODO: change line 89 to x1, x2, ...
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
    
    # TODO: same change as line 89 on 104 for x1, x2, ...
    def fancyPrint(self, curNode):
        if curNode.value == '+':
            return f'({self.fancyPrint(curNode.left)} + {self.fancyPrint(curNode.right)})'
        elif curNode.value == '-':
            return f'({self.fancyPrint(curNode.left)} - {self.fancyPrint(curNode.right)})'
        elif curNode.value == '*':
            return f'({self.fancyPrint(curNode.left)} * {self.fancyPrint(curNode.right)})'
        elif curNode.value == '/':
            return f'({self.fancyPrint(curNode.left)} / {self.fancyPrint(curNode.right)})'
        elif curNode.value == 'x':
            return 'x'
        else: 
            if str(curNode.value)[0] == '-':
                return f'({str(curNode.value)})'
            else:
                return str(curNode.value)

    # TODO: make this return the tree instead of print
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
        return ''

# CITATIONS:
# https://www.researchgate.net/publication/10684490_Using_genetic_programming_to_discover_nonlinear_variable_interactions
