from numpy import *
import operator


def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', "A", "B", "B"]
    return group, labels

if __name__ == '__main__':
    group,labels = createDataSet()
    print(group)
    print(labels)
