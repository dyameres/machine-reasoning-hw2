from Tree import Tree 
from random import randrange

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
# TODO: Need to make new tree not change original tree
def crossover(treeOne, treeTwo):
    newNode = xoverFinder(treeOne.root, 0, randrange(treeOne.depth))
    xoverInsert(treeTwo.root, 0, randrange(treeTwo.depth), newNode)
    return treeTwo

# TODO: write mutate, similar logic to xoverFinder 
def mutate(curTree):
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