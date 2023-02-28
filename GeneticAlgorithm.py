from Tree import Tree
from evolve import mutate, crossover, tournament
from csvReader import formatData
from random import randrange, random
from tqdm import tqdm

# These are Constants that the user can change
DATASET = 'hw2 datasets/dataset1.csv' # dataset as a string
POPSIZE = 100 # size of each new population
INITTREEDEPTH = 4 # depth of first tree generation (root is 0)
MUTATEPROB = 0.25 # probability of a mutation
MAXGEN = 200 # number of generations until stopping algorithm (if fit enough individual not found)
TOURNEYSIZE = 40 # size tree for tournament selection to choose a parent 
SURVIVALRATE = 0.5 # percent of population that survives to next generation
OUTPUTFILE = 'newFile.txt'

trainData, testData = formatData(DATASET)

generation = 0 
bestMSE = 1e10 # dummy value
MSEList = []

MSEsum = 0 # for average
curGen = [] # list of current generation of trees
curFitDict = {} # get fitness from tree {tree:fitness} 
rankFitList = [] # list of fitness values
rankFitDict = {} # get tree from fitness {fitness:tree} 
# generates initial population
for i in range(POPSIZE):
    curTree = Tree(INITTREEDEPTH)
    curFit = curTree.fitness(testData)
    MSEsum += curFit
    if curFit < bestMSE:
        bestMSE = curFit 
    curFitDict[curTree] = curFit
    rankFitDict[curFit] = curTree    
    curGen.append(curTree)
    rankFitList.append(curFit)

MSEList.append(bestMSE)

# Main Genetic Algorithm execution 
pbarOne = tqdm(desc='GENERATION', total = MAXGEN)
pbarTwo = tqdm(desc='CURRENT POPULATION', total = POPSIZE)
while generation < MAXGEN:
    prevMSEavg = MSEsum / POPSIZE
    bestMSE = 1e10 # dummy value
    nextGen = [] 
    nextFitDict = {} # next gen {tree:fitness}
    nextRank = []
    nextRankDict = {} # next gen {fitness:tree}
    rankFitList.sort()
    for i in range(int(POPSIZE * SURVIVALRATE)):
        nextFitDict[rankFitDict[rankFitList[i]]] = rankFitList[i]
        nextRankDict[rankFitList[i]] = rankFitDict[rankFitList[i]]
        nextGen.append(rankFitDict[rankFitList[i]])
        nextRank.append(rankFitList[i])
        pbarTwo.update(1)
    while len(nextGen) < POPSIZE:
        treeOne = Tree(copyTree=tournament(curGen, TOURNEYSIZE, curFitDict)) 
        treeTwo = Tree(copyTree=tournament(curGen, TOURNEYSIZE, curFitDict)) 
        child = crossover(treeOne, treeTwo)
        if random() < MUTATEPROB:
            mutate(child.root, 0, randrange(child.depth + 1))
        curFit = child.fitness(testData)
        if curFit < bestMSE:
            bestMSE = curFit       
        nextFitDict[child] = curFit
        nextRankDict[curFit] = child
        nextGen.append(child)
        nextRank.append(curFit)
        pbarTwo.update(1)
    generation += 1
    MSEList.append(bestMSE)
    pbarOne.update(1)
    pbarTwo.reset()
    curGen = nextGen
    rankFitList = nextRank
    curFitDict = nextFitDict
    rankFitDict = nextRankDict 
    
print(MSEList)