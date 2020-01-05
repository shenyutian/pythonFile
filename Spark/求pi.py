from pyspark import *
import random,sys


def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1


NUM_SAMPLES = 999999999
print("大数为：", NUM_SAMPLES)
sc = SparkContext("local", "求pi")
# range 生成器，生成一个数组。 与 range 完全相同
pi = sc.parallelize(range(0, NUM_SAMPLES))\
    .filter(inside).count()
print("pi大约为:" + str(4.0 * pi / NUM_SAMPLES))
