from Tree import Tree
from evolve import xoverFinder, xoverInsert, crossover
from random import randrange

#### TODO: test crossover
tree1 = Tree(3)
print(tree1)

tree2 = Tree(3)
print(tree2) 


print(crossover(tree1, tree2))
print(tree2.evaluate(tree2.root, 2))