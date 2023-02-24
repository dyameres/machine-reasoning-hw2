import csv
from random import shuffle

# dataSet = 'hw2 datasets/dataset1.csv'

# Reads in the given csv file and creates a list of lists 
# corresponding to each row of the csv without the header row. Then shuffles 
# the list a separates the data into a train data set and a test data set. 
# parameters:
#     dataSet - string of the path to the dataset to read
# returns: returns two lists, a train data set and a test data set
# TODO: add functionality for multivariable functions (dataset2.csv)
def formatData(dataSet):
    with open(dataSet) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        dataRows = []
        for row in csv_reader:
            if line_count != 0:
                dataRows.append([float(row[0]), float(row[1])])
            else:
                line_count += 1
    lenData = len(dataRows)
    listRows = list(range(lenData))
    shuffle(listRows)
    trainData = []
    testData = []
    for i in range(4 * (lenData // 5)):
        trainData.append(dataRows[i])
    for i in range(lenData - (4 * (lenData // 5))):
        testData.append(dataRows[-1 - i])
    return trainData, testData 
