from GeneticAlgorithm import GeneticAlgorithm
from csvReader import formatData

#### TODO: test in main file

# These are Constants that the user can change
DATASET = 'hw2 datasets/dataset1.csv' # dataset as a string
POPSIZE = 100 # size of each new population
INITTREEDEPTH = 2 # depth of first tree generation (root is 0)
MUTATEPROB = 0.3 # probability of a mutation
MAXGEN = 20 # number of generations until stopping algorithm (if fit enough individual not found)
TOURNEYSIZE = 25 # number of trees for tournament selection to choose a parent 
SURVIVALRATE = 0.3 # percent of population that survives to next generation
TOTALRUNS = 5 # number of times to run the Genetic Algorithm 
OUTPUTFILE = 'GAOutputFile.txt'


trainData, testData = formatData(DATASET)

with open(OUTPUTFILE, 'a') as f:
    f.write('CURRENT PARAMETERS: \n')
    f.write(f"""\tDATASET = '{DATASET}' 
\tPOPSIZE = {POPSIZE}
\tINITTREEDEPTH = {INITTREEDEPTH} 
\tMUTATEPROB = {MUTATEPROB} 
\tMAXGEN = {MAXGEN} 
\tTOURNEYSIZE = {TOURNEYSIZE} 
\tSURVIVALRATE = {SURVIVALRATE}\n\n""")
        
    for i in range(TOTALRUNS):
        GAFunc, GAFit = GeneticAlgorithm(trainData, POPSIZE, INITTREEDEPTH, MUTATEPROB, MAXGEN, TOURNEYSIZE, SURVIVALRATE, OUTPUTFILE)
        f.write(f'\tTOP Five for POPULATION {i}\n\n')
        for j in range(5):
            f.write(f"""[{j+1}] FUNCTION: {GAFunc[j]} 
    MSE: {GAFit[j]}\n\n""")
    f.write('###########################')