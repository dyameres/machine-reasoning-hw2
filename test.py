from symbolic_regresson import Node, Tree, printTree

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

print('evaluated within class')
print(first.evaluate(first.root, 2))