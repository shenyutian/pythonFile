import numpy
import matplotlib
import matplotlib.pyplot as plt

def file2matrix(filename):
    fr = open(filename)
    arrayOLine = fr.readlines()
    numberOfLines = len(arrayOLine)
    # print (numberOfLines)
    #数组 初始为零数组
    returnMat = numpy.zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    # 对所有 数据迭代
    for line in arrayOLine:
        # 前面  加  换行
        line = line.strip()
        #对 line  进行 string -> 元组化
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

dataingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
# print ((dataingDataMat[:,1]))
# datingLabels = numpy.array(datingLabels)
# print (dataingDataMat, datingLabels)
ax = plt.figure().add_subplot(111)
ax.scatter(dataingDataMat[:,1], dataingDataMat[:,2], 15.0*numpy.array(datingLabels), 15.0*numpy.array(datingLabels))
plt.show()
