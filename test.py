from Tree import Tree, printTree
from csvReader import formatData

#### TODO: test fitness
tree = Tree()
printTree(tree.root)

dataSet = 'hw2 datasets/dataset1.csv'
train, test = formatData(dataSet)

print(len(train))
print(len(test))

print(tree.fitness(train))
print(tree.fitness(train) / 4)
print(tree.fitness(test))