from pyspark import *
import Spark.emp as emp
import sys
import os, shutil


def file_move(out):
    """对输入目录清空处理"""
    filelist = os.listdir(out)
    # 删除目录下所有文件
    for file in filelist:
        os.remove(out + "/" + file)
    # 删除文件夹
    os.rmdir(out)


def syt_map1(x):
    """处理map的函数,输出部门，工资+补贴"""
    x = x.split(",")
    if x[6] != '':
        return x[2], int(x[5])+int(x[6])
    else :
        return x[2], int(x[5])

def syt_map2(x):
    """处理map"""
    x = x.split(",")
    date = x[4].split("-")
    # 判断月份长度，不够就  +0
    if len(date[1]) < 3:
        date[1] = "0" + date[1]
    # 取年 月 日 累加成字符串
    date = date[2] + date[1].replace("月", "") + date[0]
    for d in date:
        if d == '':
            d = 0
    y = emp.Emp(int(x[0]), x[1], x[2], x[3], int(date), int(x[5]))
    return x[2], y


def syt_reduce1(a, b):
    """排序筛选出日期最小的"""
    return b if a._date > b._date else a


def my_abs(x):
    """函数来校验数据是否为int， float"""
    if not isinstance(x, (int, float)):
        return 0
    else:
        return x


sc = SparkContext("local", "工资统计")
file = "F:\\input\\emp.txt"
file = "F:\\input\\dept.txt"
out = "/output"
text_file = sc.textFile(file)

"""求各个部门的总工资
counts1 = text_file.map(syt_map1).reduceByKey(lambda a, b: int(a) + int(b))
counts1.foreach(print)
print(counts1)
if os.path.exists(out):
    file_move(out)
counts1.saveAsTextFile(out)"""

"""求每个部门最早进入公司的员工姓名
# mapValues 对value 的Emp类处理，将类换成name
counts2 = text_file.map(syt_map2)\
    .reduceByKey(syt_reduce1)\
    .mapValues(lambda a: a._name)
if os.path.exists(out):
    file_move(out)
counts2.saveAsTextFile(out)"""

"""求各个城市的员工的总工资"""

