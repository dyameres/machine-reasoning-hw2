from Tree import Tree 
from random import randrange, choice

# TODO: update the depth of the current tree
def xoverInsert(curNode, curDepth, goalDepth, newNode):
    try:
        if (curDepth != goalDepth):
            if (randrange(2)):
                temp = curNode.right
            else:
                temp = curNode.left            
            xoverInsert(temp, curDepth + 1, goalDepth, newNode)
        else:
            if (randrange(2)):
                curNode.right = newNode
            else:
                curNode.left = newNode  
    except AttributeError:
        if (randrange(2)):
            curNode.right = newNode
        else:
            curNode.left = newNode

# done just needs comments
def xoverFinder(curNode, curDepth, goalDepth):
    try:
        if (randrange(2)):
            temp = curNode.right
        else:
            temp = curNode.left
        if (curDepth != goalDepth):
            return xoverFinder(temp, curDepth + 1, goalDepth)
        else:
            return temp
    except AttributeError:
        return curNode

# TODO: Look into how to avoid bloating
def crossover(treeOne, treeTwo):
    newNode = xoverFinder(treeOne.root, 0, randrange(treeOne.depth))
    xoverInsert(treeTwo.root, 0, randrange(treeTwo.depth), newNode)
    return treeTwo

# done just needs comments
def mutate(curNode, curDepth, goalDepth):
    try:
        if (randrange(2)):
            temp = curNode.right
        else:
            temp = curNode.left
        if (curDepth != goalDepth):
            mutate(temp, curDepth + 1, goalDepth)
        else:
            temp = curNode.value
            if curNode.value == 'x' or type(curNode.value) == int:
                while curNode.value == temp:
                    curNode.value = choice([randrange(-2, 3), randrange(-2, 3), 'x'])
            else:
                while curNode.value == temp:
                    curNode.value = choice(['+', '-', '*', '/'])
    except AttributeError:
        if curNode.value == 'x' or type(curNode.value) == int:
            while curNode.value == temp:
                curNode.value = choice([randrange(-2, 3), randrange(-2, 3), 'x'])
        else:
            while curNode.value == temp:
                curNode.value = choice(['+', '-', '*', '/'])
                
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
        
    