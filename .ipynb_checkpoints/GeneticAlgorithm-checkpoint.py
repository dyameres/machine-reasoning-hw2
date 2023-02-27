from Tree import Tree
from evolve import mutate, crossover 
from csvReader import formatData
from random import randrange, random
from tqdm import tqdm


DATASET = 'hw2 datasets/dataset1.csv'
POPSIZE = 5
INITTREEDEPTH = 2
MUTATEPROB = 0.25
MAXGEN = 4

trainData, testData = formatData(DATASET)

generation = 0 
bestMSE = 1e10 # dummy value
MSEList = []

MSEsum = 0
curGen = []
for i in range(POPSIZE):
    curTree = Tree(INITTREEDEPTH)
    curFit = curTree.fitness(testData)
    MSEsum += curFit
    if curFit < bestMSE:
        bestMSE = curFit
    curGen.append(curTree)

MSEList.append(bestMSE)
prevMSE = bestMSE

pbarOne = tqdm(desc='GENERATION: ' + str(generation), total = MAXGEN)
while generation < MAXGEN:
    prevMSEavg = MSEsum / POPSIZE
    bestMSE = 1e10 # dummy value
    nextGen = []
    pbarTwo = tqdm(desc='CUR GEN SIZE: ' + str(len(nextGen)), total = POPSIZE)
    while len(nextGen) < POPSIZE:
        # TODO: implement a method for parent selection
        treeOne = Tree(realTree=curGen[randrange(len(curGen))])
        treeTwo = Tree(realTree=curGen[randrange(len(curGen))])
        child = crossover(treeOne, treeTwo)
        if random() < MUTATEPROB:
            mutate(child.root, 0, randrange(child.depth + 1))
        curFit = curTree.fitness(testData)
        if curFit < prevMSEavg:
            if curFit < bestMSE:
                bestMSE = curFit
            nextGen.append(curTree)
            pbarTwo.update(1)
    generation += 1
    MSEList.append(bestMSE)
    pbarOne.update(1)
    prevMSE = bestMSE
    curGen = nextGen
    
print(MSEList)