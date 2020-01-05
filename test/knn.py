import numpy as np
import matplotlib.pyplot as plt
import operator

def createDataSet():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    # 数据数量
    dataSetSize = dataSet.shape[0]
    # tile 将数组复制 dataSetSize（行） 1列 这里是inX复制成 diffMat = array(inX, inX, ....(dataSetSize)次
    diffMat = np.tile(inX, ([dataSetSize,1])) - dataSet
    sqDiffMat = diffMat**2
    # print (sqDiffMat)
    # 样本 分析结果 sum(axis=1)行相加
    sqDistances = sqDiffMat.sum(axis=1)
    # print (sqDistances)
    distances = sqDistances**0.5
    # print (distances)
    # argsort()  将x中的元素从小到大排列，提取其对应的index(索引)  [1,4,3,-1,6,9] -> [3,0,2,1,4,5]
    sortedDistIndicies = distances.argsort()
    # print (sortedDistIndicies)
    classCount = {}
    #用于 统计 最近点数量
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        # print (voteIlabel)
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        # print (classCount[voteIlabel])
    # print (classCount)
    #classCount 是字典格式
    # sorted函数按value值对字典排序
    # key是一个函数，用来选取参与比较的元素，
    # reverse则是用来指定排序是倒序还是顺序
    sortedClassCount = sorted(classCount.items(), key=lambda item:item[1], reverse=True)
    return sortedClassCount[0][0]

group, labels = createDataSet()
# 判断是A 类  还是 B类
print (classify0([0.5,0.5], group, labels, 3))

n = 1024
listx = np.random.normal(0, 1, n)
listy = np.random.normal(0, 1, n)
listc = []

#上色过程
for i in range(n):
    color = classify0([listx[i], listy[i]], group, labels, 3)
    if color == "A":
        listc += 'r'
    elif color == "B":
        listc += 'k'
    else:
        listc += 'y'

plt.scatter(listx, listy, c = listc)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.show()