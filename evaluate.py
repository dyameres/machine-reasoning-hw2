# Evaluates a symbolic regression tree recursively through tree 
# traversal using Node objects and their children
# parameters:
#     curNode - a Node object to evaluate the current value
#     x - the current 'x' to evaluate the function at
# returns: returns the value after evaluating the tree at 
#          the current 'x' value 
def evaluate(curNode, x): # recursive
    if curNode.value == '+':
        return evaluate(curNode.left, x) + evaluate(curNode.right, x)
    elif curNode.value == '-':
        return evaluate(curNode.left, x) - evaluate(curNode.right, x)
    elif curNode.value == '*':
        return evaluate(curNode.left, x) * evaluate(curNode.right, x)
    elif curNode.value == '/':
        right = evaluate(curNode.right, x)
        if right != 0:
            return evaluate(curNode.left, x) / right
        else:
            return 1
    elif curNode.value == 'x':
        return x
    else: 
        return curNode.value
    