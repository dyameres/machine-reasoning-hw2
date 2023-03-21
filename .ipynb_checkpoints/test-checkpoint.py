from Tree import Tree
from evolve import mutate, crossover, tournament
from Node import Node
from csvReader import formatData

data, td = formatData('hw2 datasets/dataset1.csv')

t1 = Tree()
t1.root.left = None
t1.root.right = None

t1.root.value = '+'
t1.root.right = Node(5)
t1.root.left = Node('*')
t1.root.left.left = Node('-')
t1.root.left.left.left = Node('x1')
t1.root.left.left.right = Node(3)
t1.root.left.right = Node('-')
t1.root.left.right.left = Node('x1')
t1.root.left.right.right = Node(3)
print(t1)
print(t1.fitness(data))
print(t1.fitness(td))

# x = {'x1':1}
# tree = Tree(6, numX=3)
# print(tree)
# print(tree.fancyPrint(tree.root))
# tree.simplifyEvaluate(tree.root, x)
# print()
# print(tree.fancyPrint(tree.root))

# for i in range(5):
#     print(f'RUN {i}')
#     tree1 = Tree(3)
#     print(f'initial tree1 = {tree1}')
#     tree2 = Tree(3)
#     print(f'initial tree2 = {tree2}')
#     child = crossover(Tree(copyTree=tree1), Tree(copyTree=tree2))
#     print(f'child after crossover = {child}')
#     mutate(child, child.root, 1)
#     print(f'child after mutate = {child}')
#     print()