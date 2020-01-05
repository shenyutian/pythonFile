import random

import math
from functools import reduce

from numpy.core.defchararray import capitalize


def add(x, y, f):
    return f(x) + f(y)


def fn(x, y):
    return x*10 + y


def normalize(str):
    """进行单词格式化 Aaaaa格式"""
    for i in range(len(str)):
        if 'A' < str[i] < 'Z':
            str[i] = str[i] - 'A'
    if 'a' < str[0] < 'z':
        str[0] = 'a'


def is_palindrome(n):
    """进行回数判断，"""
    n = str(n)
    l = len(n)
    print(n)
    # print(tuple((n[k], n[l-k-1]) for k in range(int((l + 1) / 2))))
    n1 = list(filter((lambda x: x[0] == x[1]), tuple((n[k], n[l-k-1]) for k in range(int((l + 1) / 2)))))
    print(n1)
    for k in range(int(l)):
        if n[k] != n[l-k-1]:
            return
    return n


def by_name(t):
    print(t)
    # 名称排序t[0], 按照成绩排序t[1]
    return t[0]



# print(add(-1, 5, abs))
# map 函数 第一个参数方法， 第二个数据类型。 返回一个iterator对象
print(tuple(map(math.sqrt, [1, 2, 4])))
# 快速转换 字符串
print(list(map(str, [1, 3, 5])))
# reduce 函数 返回 一个元素 将
print(reduce(fn, [1, 1, 4, 1]))
# 将 字符串数组 格式化为 大写开头，后面小写。 并且将其输出为一段话
print(reduce(lambda x, y: str(x) + " " + str(y), map(capitalize, ['adam', 'LISA', 'barT'])))
# 数组 求和
print("sum:", reduce(lambda x, y: x + y, [3, 5, 7, 9]))
# 字符串 -> 浮点类型
print("float:", float('123.456'))
# filter 筛选元素， 返回Iterator，也就是一个惰性序列 需要list来输出
print("filter:", list(filter(lambda x: x % 2 == 0, [1, 3, 5, 8])))
# 利用filter来求 回数
print("判断：", list(filter(is_palindrome, range(1, 2000))))
# 排序算法 sample(a, b) a是数组，b是排序条件
print(sorted(random.sample(list(range(-20, 10)), 5), key=abs))
# 学生的元组排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key=by_name))

