import numpy as np

def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    else:
        return 1 / (1 + np.exp(-x))

# 数据输入集
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])
# 输出数据集
y = np.array([[0, 1, 1, 0]]).T
syn0 = 2 * np.random.random((3, 4)) - 1  # 第一个隐藏层权重值
syn1 = 2 * np.random.random((4, 1)) - 1  # 隐藏输出层权重值
print ("syn0", syn0, "\nsyn1", syn1)
for j in range(2):
    l0 = X  # 第一层  输入层
    # dot()返回的是两个数组的点积 多维为矩阵积
    l1 = nonlin(np.dot(l0, syn0))  # 第二层，和隐藏层
    l2 = nonlin(np.dot(l1, syn1))  # 第三层，输出层
    l2_error = y - l2  # 隐藏 输出层 错误
    print ("l1", l1, "\nl2", l2, "\nl2_error", l2_error)
    if (j % 10000) == 0:
        # np.mean 求取均值
        print ("Error:" + str(np.mean(l2_error)))
    l2_delta = l2_error * nonlin(l2, deriv=True)
    l1_error = l2_delta.dot(syn1.T)  # 第一个隐藏层错误
    print ("l1_error", l1_error, "\nl2_delta", l2_delta, "\nsyn1", syn1.T)
    l1_delta = l1_error * nonlin(l1, deriv=True) #误差校正系数
    print ("l2_delta", l2_delta, "\nl1_error", l1_error, "\nl1_delta", l1_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)
    print("syn0", syn0, "\nsyn1", syn1)
print ("训练结果是:")
print (l2)