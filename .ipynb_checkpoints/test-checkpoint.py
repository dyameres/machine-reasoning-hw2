from Tree import Tree
from csvReader import formatData

#### TODO: test fitness
tree = Tree()
print(tree)

dataSet = 'hw2 datasets/dataset1.csv'
train, test = formatData(dataSet)

print(len(train))
print(len(test))

print(tree.fitness(train))
print(tree.fitness(train) / 4)
print(tree.fitness(test))