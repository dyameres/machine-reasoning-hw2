from Tree import Tree
from evolve import mutate, crossover, tournament
from random import randrange
from csvReader import formatData
import matplotlib.pyplot as plt

#### TODO: graphing data points

DATASET = 'hw2 datasets/dataset1.csv'

trainData, testData = formatData(DATASET)

fullData = trainData + testData
xData = []
yData = []
for i in range(len(fullData)):
    xData.append(fullData[i][0])
    yData.append(fullData[i][1])
    
plt.plot(xData, yData)