import csv
from random import shuffle

# dataSet = 'hw2 datasets/dataset1.csv'

def readCsv(dataSet):
    with open(dataSet) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        dataRows = []
        for row in csv_reader:
            if line_count != 0:
                dataRows.append([float(row[0]), float(row[1])])
            else:
                line_count += 1

        return dataRows
    
def separateData(dataSet):
    lenData = len(dataSet)
    listRows = list(range(lenData))
    shuffle(listRows)
    trainData = []
    testData = []
    for i in range(4 * (lenData // 5)):
        trainData.append(dataSet[i])
    for i in range(len(x) - (4 * (len(x) // 5))):
        testData.append(dataSet[-1 - i])
    return trainData, testData
