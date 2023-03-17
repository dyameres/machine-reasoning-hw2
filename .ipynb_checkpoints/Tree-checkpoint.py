#
#
# By Dylan Ameres and Tristan Allen

import random
from Node import Node

class Tree():
    
    def __init__(self, maxDepth=2, numX=1, copyTree=None): # defaults to tree of depth 2 if no parameter given
        if copyTree == None:
            self.root = Node(random.choice(['+', '-', '/', '*']))
            xValues = []
            for i in range(numX):
                xValues.append('x' + str(i + 1))
            self.buildTree(self.root, 1, maxDepth, xValues) # constructs the tree
            self.depth = maxDepth
            self.xVals = xValues
        else:
            self.root = self.copyTree(copyTree.root)
            self.depth = copyTree.depth
            self.xVals = copyTree.xVals
        
    # Recursively builds the tree to the specified max depth
    # parameters: 
    #     curNode - Node object of the current node to create children for
    #     curDepth - int of what layer the current node is at 
    #     maxDepth - int of how many layers to build the tree out
    def buildTree(self, curNode, curDepth, maxDepth, xList):
        ops = ['+', '-', '*', '/']
        if curDepth < maxDepth:
            curNode.left = Node(random.choice(ops))
            self.buildTree(curNode.left, curDepth+1, maxDepth, xList)
            curNode.right = Node(random.choice(ops))
            self.buildTree(curNode.right, curDepth+1, maxDepth, xList)
        else:
            curNode.left = Node(random.choice([random.randrange(-5, 6), random.choice(xList)]))
            curNode.right = Node(random.choice([random.randrange(-5, 6), random.choice(xList)]))
            
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
            xValues = {}
            for j in range(len(dataSet[i]) - 1):
                xValues['x' + str(j + 1)] = dataSet[i][j]
            MSE += (self.evaluate(self.root, xValues) - dataSet[i][-1])**2 # calculate mse for each data point
        return MSE / len(dataSet) # taking mean of the squared error 
    
    # Evaluates a symbolic regression tree recursively through tree 
    # traversal using Node objects and their children. Helper function
    # for the fitness method.
    # parameters:
    #     curNode - a Node object to evaluate the current value
    #     xValues - Dict, {x1:value, x2:value, ...}
    # returns: float, returns the value after evaluating the tree at 
    #          the current 'x' value 
    def evaluate(self, curNode, xValues):
        if curNode.value == '+':
            return self.evaluate(curNode.left, xValues) + self.evaluate(curNode.right, xValues)
        elif curNode.value == '-':
            return self.evaluate(curNode.left, xValues) - self.evaluate(curNode.right, xValues)
        elif curNode.value == '*':
            return self.evaluate(curNode.left, xValues) * self.evaluate(curNode.right, xValues)
        elif curNode.value == '/':
            right = self.evaluate(curNode.right, xValues)
            if right != 0:
                return self.evaluate(curNode.left, xValues) / right
            else:
                return 1
        # try to add flag here to reduce tree
        elif type(curNode.value) == int:
            return curNode.value
        else:
            return xValues[curNode.value]
        
    # COPY OF EVALUATE TO TEST REDUCTION  
    def reduceEvaluate(self, curNode, xValues):
        tempSimplify = 0
        if curNode.value == '+':
            left, Lsimplify = self.evaluate(curNode.left, xValues)
            right, Rsimplify = self.evaluate(curNode.right, xValues)
            if Lsimplify == 1 and Rsimplify == 1:
                curNode.left = None
                curNode.right = None 
                curNode.value = left + right
                tempSimplify = 1
            return left + right, tempSimplify
        elif curNode.value == '-':
            left, Lsimplify = self.evaluate(curNode.left, xValues)
            right, Rsimplify = self.evaluate(curNode.right, xValues)
            if Lsimplify == 1 and Rsimplify == 1:
                curNode.left = None
                curNode.right = None 
                curNode.value = left - right
                tempSimplify = 1
            return left - right, tempSimplify
        elif curNode.value == '*':
            left, Lsimplify = self.evaluate(curNode.left, xValues)
            right, Rsimplify = self.evaluate(curNode.right, xValues)
            if Lsimplify == 1 and Rsimplify == 1:
                curNode.left = None
                curNode.right = None 
                curNode.value = left * right
                tempSimplify = 1
            return left * right, tempSimplify
        # try to simplify for division as well 
        elif curNode.value == '/':
            right = self.evaluate(curNode.right, xValues)
            if right != 0:
                return self.evaluate(curNode.left, xValues) / right
            else:
                return 1
        # try to add flag here to reduce tree
        elif type(curNode.value) == int:
            return curNode.value, 1
        else:
            return xValues[curNode.value]
    
    def fancyPrint(self, curNode):
        if curNode.value == '+':
            return f'({self.fancyPrint(curNode.left)} + {self.fancyPrint(curNode.right)})'
        elif curNode.value == '-':
            return f'({self.fancyPrint(curNode.left)} - {self.fancyPrint(curNode.right)})'
        elif curNode.value == '*':
            return f'({self.fancyPrint(curNode.left)} * {self.fancyPrint(curNode.right)})'
        elif curNode.value == '/':
            return f'({self.fancyPrint(curNode.left)} / {self.fancyPrint(curNode.right)})'
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
