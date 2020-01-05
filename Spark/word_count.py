from pyspark import SparkContext, SparkConf
"""单词统计Scark第一次"""

conf = SparkConf().setAppName("单词统计").setMaster("local")
sc = SparkContext('local', "单词统计")
# 获取数据
# textFile = sc.textFile('hdfs://192.168.64.140:9000/input/wa.txt')
textFile = sc.textFile('file://上传路径/wa.txt')
wordcount = textFile.flatMap(lambda line: line.split(""))\
    .map(lambda word: (word, 1))\
    .reduceByKey(lambda a, b: a + b)
print(wordcount.name())
# print(wordcount.min())
# print(wordcount.take(5))
