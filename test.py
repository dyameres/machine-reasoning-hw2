from Tree import Tree
from evolve import mutate
from random import randrange

#### TODO: test mutate
tree1 = Tree(2)
print(tree1)

mutate(tree1.root, 0, randrange(tree1.depth + 1))
print(tree1)

