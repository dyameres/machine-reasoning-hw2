from Tree import Tree
from evolve import mutate, crossover, tournament

def x():
    return 0, 1

y = x()
print(y[0])

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