from Tree import Tree
from evolve import mutate, crossover, tournament
from csvReader import formatData
from random import randrange, random
from tqdm import tqdm

def GeneticAlgorithm(DATASET, POPSIZE, INITTREEDEPTH, MUTATEPROB, MAXGEN, TOURNEYSIZE, SURVIVALRATE):
    
        generation = 0 
        bestMSE = 1e16 # dummy value
        MSEList = []

        MSEsum = 0 # for average
        curGen = [] # list of current generation of trees
        curFitDict = {} # get fitness from tree {tree:fitness} 
        rankFitList = [] # list of fitness values
        rankFitDict = {} # get tree from fitness {fitness:tree} 

        # generates initial population
        pbarZero = tqdm(desc='INITIAL POPULATION GENERATION', total = POPSIZE)
        for i in range(POPSIZE):
            curTree = Tree(maxDepth=INITTREEDEPTH, numX=(len(DATASET[0]) - 1))
            curFit = curTree.fitness(DATASET)
            MSEsum += curFit
            if curFit < bestMSE:
                bestMSE = curFit 
            curFitDict[curTree] = curFit
            rankFitDict[curFit] = curTree    
            curGen.append(curTree)
            rankFitList.append(curFit)
            pbarZero.update(1)

        MSEList.append(bestMSE)

        # Main Genetic Algorithm execution 
        pbarOne = tqdm(desc='GENERATION', total = MAXGEN)
        pbarTwo = tqdm(desc='CURRENT POPULATION', total = POPSIZE)
        while generation < MAXGEN:
            prevMSEavg = MSEsum / POPSIZE
            bestMSE = 1e19 # dummy value
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
                child = crossover(treeOne, treeTwo, INITTREEDEPTH)
                mutate(child, child.root, MUTATEPROB)
                curFit = child.fitness(DATASET)
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
            if bestMSE < 1e-3: # we'll say it converged 
                break
            with open('BestMSE.txt', 'a') as f:
                f.write(f'[{generation}]: {bestMSE}\n')
        rankFitList.sort()
        bestFunc = []
        for i in range(5):
            bestFunc.append(rankFitDict[rankFitList[i]])
        return bestFunc
