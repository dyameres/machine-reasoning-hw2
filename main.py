from GeneticAlgorithm import GeneticAlgorithm
from csvReader import formatData

# These are Constants that the user can change
DATASET = 'hw2 datasets/dataset2.csv' # dataset as a string
POPSIZE = 2000 # size of each new population
INITTREEDEPTH = 3 # depth of first tree generation (root is 0)
MUTATEPROB = 0.1 # probability of a mutation
MAXGEN = 10 # number of generations until stopping algorithm (if fit enough individual not found)
TOURNEYSIZE = 50 # number of trees for tournament selection to choose a parent 
SURVIVALRATE = 0.4 # percent of population that survives to next generation
TOTALRUNS = 5 # number of times to run the Genetic Algorithm 
OUTPUTFILE = f'{DATASET[-5]}GAOutputFile.txt'


trainData, testData = formatData(DATASET)

with open(OUTPUTFILE, 'a') as f:
    f.write('\nCURRENT PARAMETERS: \n')
    f.write(f"""\tDATASET = '{DATASET}' 
\tPOPSIZE = {POPSIZE}
\tINITTREEDEPTH = {INITTREEDEPTH} 
\tMUTATEPROB = {MUTATEPROB} 
\tMAXGEN = {MAXGEN} 
\tTOURNEYSIZE = {TOURNEYSIZE} 
\tSURVIVALRATE = {SURVIVALRATE}\n\n""")
        
    for i in range(TOTALRUNS):
        GAFuncList = GeneticAlgorithm(trainData, POPSIZE, INITTREEDEPTH, MUTATEPROB, MAXGEN, TOURNEYSIZE, SURVIVALRATE)
        f.write(f'\tTOP Five for POPULATION {i + 1}\n\n')
        for j in range(5):
            f.write(f"""[{j+1}] FUNCTION: {GAFuncList[j].fancyPrint(GAFuncList[j].root)} 
    TEST DATA MSE: {GAFuncList[j].fitness(testData)}\n\n""")
    f.write('###########################\n')
