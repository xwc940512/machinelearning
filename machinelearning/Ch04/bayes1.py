#!/usr/bin/env python
# coding=utf-8
from numpy import *
def loadDataSet():
    postingList = [['my','dog','has','flea','problems','help','please'],
                  ['maybe','not','take','him','to','dog','park','stupid'],
                  ['my','dalmation','is','so','cute','I','love','him'],
                  ['stop','posting','stupid','worthless','garbage'],
                   ['mr','licks','ate','my','steak','how','to','stop','him'],
                   ['quit','buying','worthless','dog','food','stupid']]
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec

def createVocabList(dataSet):
    vocaSet = set([])#用列表去初始化一个集合
    for document in dataSet:
        vocaSet = vocaSet | set(document)#对列表中的每一个列表我们都将他转化为相应的集合
    return list(vocaSet)#返回时又转化为相应的列表

def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)#初始化一个长度和词汇表等长的全0的序列
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
    return returnVec

def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p1Num = ones(numWords); p0Num = ones(numWords)
    p1Demo = 2.0; p0Demo = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Demo += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Demo += sum(trainMatrix[i])
    p1Vec = log(p1Num / p1Demo)
    p0Vec = log(p0Num / p0Demo)
    return p1Vec, p0Vec, pAbusive

def classifyNB(vec2Classfy, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classfy * p1Vec) + log(pClass1)
    p0 = sum(vec2Classfy * p0Vec) + log(1 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    postingList, classVec = loadDataSet()
    vocabSet = createVocabList(postingList)
    trainMat = []
    for postingDoc in postingList:
        trainMat.append(setOfWords2Vec(vocabSet, postingDoc))
    p1Vec, p0Vec, pAb = trainNB0(array(trainMat), array(classVec))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(vocabSet, testEntry))
    print testEntry,'classfied as:', classifyNB(thisDoc, p0Vec, p1Vec, pAb)
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(vocabSet, testEntry))
    print testEntry,'classfied as:', classifyNB(thisDoc, p0Vec, p1Vec, pAb)







    
