#!/usr/bin/env python
# coding=utf-8

from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as  plt


def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    arrayline = fr.readlines()
    numberOfLines = len(arrayline)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayline:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        if cmp(listFromLine[-1],"largeDoses") == 0:
            classLabelVector.append(3)
        elif cmp(listFromLine[-1] , "smallDoses") == 0:
            classLabelVector.append(2)
        elif cmp(listFromLine[-1] , "didntLike") == 0:
            classLabelVector.append(1)
        index += 1
    return returnMat,classLabelVector

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet / tile(ranges, (m,1))
    return normDataSet, ranges, minVals

def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print "the classifier came back with: %d, the real answer is: %d" %(classifierResult, datingLabels[i])
        if(classifierResult != datingLabels[i]): errorCount += 1.0
    print "the totak error rate is: %f"  %(errorCount/float(numTestVecs))

def classifyPerson():
    resultList = ['not at all','in small doses','in large doses']
    percentTats = float(raw_input("percent of time spent palying vedio games?"))
    ffMiles = float(raw_input("frequent fliter miles earned per year?"))
    iceCream = float(raw_input("liters of ice cream cunsumed per year?"))
    datingDatamat,datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr - minVals)/ranges, normMat, datingLabels, 3)
    print "You will probably like this person: ",resultList[classifierResult - 1]

if __name__ == "__main__":
    group, labels = createDataSet()
    classify0([0, 0], group, labels, 3)
    datingDataMat,datingLabels = file2matrix("datingTestSet.txt")
    print datingLabels[0 : 20]
    print datingDataMat
    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    #ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
    #plt.show()mZ
    classifyPerson()
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.scatter(datingDataMat[:,1],datingDataMat[:,2],15 * array(datingLabels), 15 * array(datingLabels))
    plt.show()

