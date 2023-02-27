from Tree import Tree
from evolve import mutate, crossover
from random import randrange

#### TODO: test mutate
tree1 = Tree(1)
print(tree1)

tree2 = Tree(realTree=tree1)
print(tree2)
mutate(tree2.root, 0, randrange(tree1.depth + 1))
print(tree2)

tree2.root.value = 0

print(tree2)
print(tree1)

