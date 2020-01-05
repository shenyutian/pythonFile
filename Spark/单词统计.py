from pyspark import *
import os
import sys


sc = SparkContext('local', '单词统计')
# File = 'hdfs://sytnode01:9000/input/per'
File = 'F:\\上传路径\\china.txt'
Data = sc.TextFiles(File, 1)
# print(Data.take(2))
counts = Data.flatMap(lambda line: line.split(" "))
counts = counts.map(lambda word: (word, 1))
counts = counts.reduceByKey(lambda a, b: a + b)
# # 输出路径处理
url = "/output"
if os.path.exists(url) :
    os.remove(url)
counts.saveAsTextFile(url)
counts = iter(counts)
# for count in counts:
    # print(count)
# counts.foreach(print)
# print(type(counts))
