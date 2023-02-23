from symbolic_regresson import Node, Tree, buildTree, printTree
from evaluate import evaluate

# root = Node('*')

# root.left = Node('+')
# root.right = Node('-')

# root.left.left = Node(4)
# root.left.right = Node('x')

# root.right.left = Node('x')
# root.right.right = Node(2)


# print(evaluate(root, 1))

first = Tree(2)
printTree(first.root)


print('evaluated outside class')
print(evaluate(first.root, 2))
print('evaluated within class')
print(first.evaluate(first.root, 2))