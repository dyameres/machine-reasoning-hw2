from Tree import Tree
from evolve import mutate, crossover, tournament
from csvReader import formatData
from random import randrange, random
from tqdm import tqdm

# These are Constants that the user can change
DATASET = 'hw2 datasets/dataset1.csv' # dataset as a string
POPSIZE = 5 # size of each new population
INITTREEDEPTH = 2 # depth of first tree generation (root is 0)
MUTATEPROB = 0.25 # probability of a mutation
MAXGEN = 4 # number of generations until stopping algorithm (if fit enough individual not found)
TOURNEYSIZE = 5 # size tree for tournament selection to choose a parent 

trainData, testData = formatData(DATASET)

generation = 0 
bestMSE = 1e10 # dummy value
MSEList = []

MSEsum = 0 # for average
curGen = []
curFitDict = {} # get fitness from tree
for i in range(POPSIZE):
    curTree = Tree(INITTREEDEPTH)
    curFit = curTree.fitness(testData)
    curFitDict[curTree] = curFit
    MSEsum += curFit
    if curFit < bestMSE:
        bestMSE = curFit
    curGen.append(curTree)

MSEList.append(bestMSE)
prevMSE = bestMSE

while generation < MAXGEN:
    pbarOne = tqdm(desc='GENERATION: ' + str(generation), total = MAXGEN)
    prevMSEavg = MSEsum / POPSIZE
    bestMSE = 1e10 # dummy value
    nextGen = []
    nextFitDict = {}
    pbarTwo = tqdm(desc='CUR GEN SIZE: ' + str(len(nextGen)), total = POPSIZE)
    while len(nextGen) < POPSIZE:
        # TODO: implement a method for parent selection
        treeOne = Tree(copyTree=tournament(curGen, TOURNEYSIZE, curFitDict))
        treeTwo = Tree(copyTree=tournament(curGen, TOURNEYSIZE, curFitDict))
        child = crossover(treeOne, treeTwo)
        if random() < MUTATEPROB:
            mutate(child.root, 0, randrange(child.depth + 1))
        curFit = child.fitness(testData)
        nextFitDict[child] = curFit
        # if curFit < prevMSEavg:
        # tab
        if curFit < bestMSE:
            bestMSE = curFit
        print(bestMSE)
        nextGen.append(child)
        pbarTwo.update(1)
        #
    generation += 1
    MSEList.append(bestMSE)
    pbarOne.update(1)
    prevMSE = bestMSE
    curGen = nextGen
    curFitDict = nextFitDict
    
print(MSEList)