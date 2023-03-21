from Tree import Tree 
from random import randrange, choice, random

# crosses over part of one tree into another. No return. 
# parameters: 
#     curNode - Node, current node from tree two to check
#     curDepth - int, how far down the current tree
#     goalDepth - int, depth to stop
#     newNode - Node, node from tree one to crossover
# TODO: could update curTree.depth
def xoverInsert(curNode, curDepth, goalDepth, newNode):
    try:
        if (curDepth != goalDepth):
            if (randrange(2)):
                temp = curNode.right
            else:
                temp = curNode.left            
            xoverInsert(temp, curDepth + 1, goalDepth, newNode)
        else:
            try:
                if curNode.value[0] == 'x':
                    curNode = newNode
                else:
                    if (randrange(2)):
                        curNode.right = newNode
                    else:
                        curNode.left = newNode  
            except TypeError:
                curNode = newNode 
    except AttributeError:
        try:
            if curNode.value[0] == 'x':
                curNode = newNode
            else:
                if (randrange(2)):
                    curNode.right = newNode
                else:
                    curNode.left = newNode  
        except TypeError:
            curNode = newNode

# Finds a node from tree one to crossover to tree two
# parameters:
#     curNode - Node, current node being checked from tree one
#     curDepth - int, how far down the current tree
#     goalDepth - int, depth to stop
# return: Node, returns a node from tree one to crossover
def xoverFinder(curNode, curDepth, goalDepth):
    try:
        if (randrange(2)):
            temp = curNode.right
        else:
            temp = curNode.left
        if temp is None:
            return curNode
        else:
            if (curDepth != goalDepth):
                return xoverFinder(temp, curDepth + 1, goalDepth)
            else:
                return temp
    except AttributeError:
        return curNode

# TODO: Look into how to avoid bloating
def crossover(treeOne, treeTwo, MAXDEPTH):
    xDepth = randrange(0, MAXDEPTH)
    newNode = xoverFinder(treeOne.root, 0, xDepth)
    xoverInsert(treeTwo.root, 0, xDepth, newNode)
    return treeTwo

# Recursively finds a random node from the tree and changes
# its value
# parameters:
#     curTree - Tree, current tree being checked
#     curNode - Node, current node to check 
#     curDepth - int, current depth in the tree
#     goalDepth - int, max depth to go
def mutate(curTree, curNode, MUTATEPROB):
    try:
        mutate(curTree, curNode.left, MUTATEPROB)
        mutate(curTree, curNode.right, MUTATEPROB)
        if (random() < MUTATEPROB):
            temp = curNode.value
            try:
                if curNode.value[0] == 'x':
                    while curNode.value == temp:
                        curNode.value = choice([randrange(-5, 6), choice(curTree.xVals)])
                else:
                    while curNode.value == temp:
                        curNode.value = choice(['+', '-', '*', '/'])
            except TypeError:
                while curNode.value == temp:
                    curNode.value = choice([randrange(-5, 6), choice(curTree.xVals)])
    except AttributeError:
        if (random() < MUTATEPROB):
            temp = curNode.value
            try:
                if curNode.value[0] == 'x':
                    while curNode.value == temp:
                        curNode.value = choice([randrange(-5, 6), choice(curTree.xVals)])
                else:
                    while curNode.value == temp:
                        curNode.value = choice(['+', '-', '*', '/'])
            except TypeError:
                while curNode.value == temp:
                    curNode.value = choice([randrange(-5, 6), choice(curTree.xVals)])
                
                
# Implements tournament selection to determine a suitable parent
# for Genetic Algorithm. 
# parameters:
#     curGen - list of Trees, current generation of individuals
#              to pull a random sample from
#     tourneySize - int, number of individuals to select for tournament
#     fitDict - dictionary, keys are individuals in curGen and 
#               values are the corresponding fitness
# returns: Tree, returns the best fit individual from the sample
def tournament(curGen, tourneySize, fitDict):
    competitor = curGen[randrange(len(curGen))]
    champion = competitor
    bestFit = fitDict[competitor]
    for i in range(1, tourneySize):
        nextCompetitor = curGen[randrange(len(curGen))]
        if fitDict[nextCompetitor] < bestFit:
            champion = nextCompetitor
            bestFit = fitDict[nextCompetitor]
    return champion
        
    