import numpy as np
import matplotlib.pyplot as plt
max = 0 #最大值点  数量
inX1 = [0, 0] #最大值坐标

def classify0(inX, dataSet, k):
    dataSet = np.array(dataSet)
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, ([dataSetSize,1])) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    index = 0
    global max
    global inX1
    for line in distances:
        if line < 0.1:
            index += 1
    if index > max:
        max = index
        inX1 = inX

def huayuan(inX, dataSet):
    print(inX)
    dataSet = np.array(dataSet)
    r = 0.5
    a = inX[0]
    b = inX[1]
    theta = np.arange(0, 2 * np.pi, 0.01)
    x = a + r * np.cos(theta)
    y = b + r * np.sin(theta)
    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(x, y)
    # axes.plot(dataSet[:,0], dataSet[:,1])
    axes.axis('equal')
    plt.xlim((-1.5, 1.5))
    plt.ylim((-1.5, 1.5))
    plt.show()

n = 1024
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
dataSet = list(zip(x, y))
dataSet = np.array(dataSet)
plt.scatter(dataSet[:,0], dataSet[:,1])
for line in dataSet:
    classify0(line, dataSet, 50)
huayuan(inX1, dataSet)
