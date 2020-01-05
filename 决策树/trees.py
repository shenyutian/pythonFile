import math

# 计算 香农熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        # print (currentLabel)
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
        # print (labelCounts)
    shannonEnt = 0.0
    for key in labelCounts:
        # print (key)
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob*math.log(prob, 2)
        # print (prob)
        print (shannonEnt)
    return shannonEnt

# 划分数据集
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

# 选择数据集的 划分方式
def chooseBestFeatureToSplit(dataSet):
    # 3个数据
    numFeatures = len(dataSet[0]) - 1
    # 香农熵
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        print (featList)
        uniqueVals = set(featList)
        print (uniqueVals)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=lambda count: classCount[1], reverse=True)
    print (sortedClassCount)

dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'],[0, 1, 'no']]
labels = ['no surfacing', 'flippers']
myDat = dataSet
# calcShannonEnt(myDat)
# myDat[0][-1] = 'myybe'
# print (myDat)
calcShannonEnt(myDat)
print (myDat)
print (splitDataSet(myDat, 0, 1))
print (splitDataSet(myDat, 0, 0))
print (chooseBestFeatureToSplit(myDat))
print (majorityCnt(myDat))