from Node import Node
import random

# Helper function to recursively create multiple layers of the tree
# parameters: 
#     curNode - the current node to create children for
#     curDepth - what layer the current node is at 
#     maxDepth - how many layers to build the tree out
def buildHelper(curNode, curDepth, maxDepth):
    ops = ['+', '-', '*', '/']
    if curDepth < maxDepth:
        curNode.left = Node(random.choice(ops))
        buildHelper(curNode.left, curDepth+1, maxDepth)
        curNode.right = Node(random.choice(ops))
        buildHelper(curNode.right, curDepth+1, maxDepth)
    else:
        # using 2:1 for integers to x's to avoid too many x's but could change in future
        curNode.left = Node(random.choice([random.randrange(-2, 3), random.randrange(-2, 3), 'x']))
        curNode.right = Node(random.choice([random.randrange(-2, 3), random.randrange(-2, 3), 'x']))
    
# Initializes the tree building process by calling the recursive helper
# parameters:
#     tree - the initial tree object 
#     maxDepth - the total number of levels to build the tree (first layer is 0)
def buildTree(tree, maxDepth):
    ops = ['+', '-', '*', '/']
    tree.left = buildHelper(tree.root, 1, maxDepth)
    tree.right = buildHelper(tree.root, 1, maxDepth)