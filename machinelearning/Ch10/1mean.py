#!/usr/bin/env python
# coding=utf-8
from numpy import *

def loadDataSet(filename):
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split("\t")
        fltLine = map(flaot, curLine)
        dataMat.append(fltLine)
    return dataMat

def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))

def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = Mat(zeros((k, n)))#强行转化为矩阵
    for j in range(n):#对于每一列进行相关的操作
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j])-minJ)
        centroids[:,j] = minJ + rangeJ * random.rand(k,1)#调用了random的模块，可以调用一堆的api
    return centroids


