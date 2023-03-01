import csv
from random import shuffle

# dataSet = 'hw2 datasets/dataset1.csv'

# TODO: add functionality for multivariable functions (see dataset2.csv)

# Reads in the given csv file and creates a list of lists 
# corresponding to each row of the csv without the header row. Then shuffles 
# the list a separates the data into a train data set and a test data set. 
# parameters:
#     dataSet - string of the path to the dataset to read
# returns: returns two lists, a train data set and a test data set
def formatData(dataSet):
    with open(dataSet) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        dataRows = []
        for row in csv_reader:
            curRow = []
            if line_count != 0: # line 0 is the header
                for i in range(len(row)):
                    curRow.append(float(row[i]))
                dataRows.append(curRow)
            else:
                line_count += 1
    lenData = len(dataRows)
    listRows = list(range(lenData))
    shuffle(listRows) # shuffle to randomize data set
    trainData = []
    testData = []
    for i in range(4 * (lenData // 5)):
        trainData.append(dataRows[i])
    for i in range(lenData - (4 * (lenData // 5))):
        testData.append(dataRows[-1 - i])
    return trainData, testData 
