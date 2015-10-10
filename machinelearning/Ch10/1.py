#!/usr/bin/env python
# coding=utf-8
from numpy import *

def loadDataSet(filename):
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float, curLine)
        dataMat.append(fltLine)
    return dataMat

def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))

def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k, n)))#强行转化为矩阵
    for j in range(n):#对于每一列进行相关的操作
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j])-minJ)
        centroids[:,j] = minJ + rangeJ * random.rand(k,1)#调用了random的模块，可以调用一堆的api
    return centroids

def kMeans(dataSet, k, distMeans=distEclud, createCent=randCent):
    m = shape(dataSet)[0]#取一共有多少个点
    clusterAssment = mat(zeros((m,2)))#一共m个点。两列，第一列是点的序号，第二列是点距离簇中心的距离平方和
    centroids = createCent(dataSet, k)#选取k个点，作为初始的簇中心
    clusterChanged = True#簇默认是改变果的
    while clusterChanged:
        clusterChanged = False#初始认为簇为未改变的
        for i in range(m):#对于图中的每一个点
            minDist = inf; minIndex = -1#初始的最小距离设为一个极大的值，最小的索引也是极小的值
            for j in range(k):#对于每一个点对于每一个簇中心时
                distJI = distMeans(centroids[j,:],dataSet[i,:])#算出设定的距离量度的距离
                if distJI < minDist:
                    minDist = distJI; minIndex = j#进行相关的替换
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex, minDist ** 2#对于每个点，给出对应的簇中心，以及相关的距离和
        print centroids
        for cent in range(k):#对于每一个簇中心
            ptsInclust = dataSet[nonzero(clusterAssment[:,0].A == cent)[0]]#
            centroids[cent,:] = mean(ptsInclust, axis=0)#更新每一个相关的簇中心，axis=0是取列的平均值
    return centroids, clusterAssment#返回相关的质心和各个点的簇中心以及距离和
    
def biKmean(dataSet, k, distMeans= distEclud):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))
    centroid0 = mean(dataSet, axis=0).tolist()[0]
    centList = [centroid0]
    for j in range(m):
        clusterAssment[j,1] = distMeans(dataMat[j,:], mat(centroid0)) ** 2
    while len(centList) < k:
        lowestSSE = inf
        for i in range(centList):




if __name__ == "__main__":
    dataMat = mat(loadDataSet('testSet.txt'))
    myCentroids, clustAssing = kMeans(dataMat, 4)
    print myCentroids
    print clustAssing
    
