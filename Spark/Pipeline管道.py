"""管道Pipline example 用于对text分析，产生训练集，并且预测概率和标签"""
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import Tokenizer
from pyspark.ml.feature import HashingTF
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("管道例子").getOrCreate()
# 从（id，文本，标签）元组列表准备培训文档
training = spark.createDataFrame([
        (0, "a b c d e spark", 1.0),
        (1, "b d", 0.0),
        (2, "spark f g h", 1.0),
        (3, "hadoop mapreduce", 0.0),
        (4, "b spark who", 1.0),
        (5, "g d a y", 0.0),
        (6, "spark fly", 1.0),
        (7, "was mapreduce", 0.0),
        (8, "e spark program", 1.0),
        (9, "a e c l", 0.0),
        (10, "spark compile", 1.0),
        (11, "hadoop software", 0.0)
    ], ["id", "text", "label"])

# 配置一个ML管道，该管道包括三个阶段
# tokenizer(分词器), hashingTF(切割), and lr(逻辑回归)
tokenizer = Tokenizer(inputCol="text", outputCol="words")
hashingTF = HashingTF(inputCol=tokenizer.getOutputCol(), outputCol="features")
lr = LogisticRegression(maxIter=10, regParam=0.001)
pipeline = Pipeline(stages=[tokenizer, hashingTF, lr])
# 训练文件的管道
model = pipeline.fit(training)
# print("mode\n", model.extend())
# 准备没有label的（id，text）元组的测试文档
test = spark.createDataFrame([
        (4, "spark i j k"),
        (5, "l m n"),
        (6, "mapreduce spark"),
        (7, "apache hadoop")
    ], ["id", "text"])
# 对测试文档进行预测并打印结果的列
prediction = model.transform(test)
print("show\n", prediction.show())
selected = prediction.select("id", "text", "probability", "prediction")
print("预测结果：")
for row in selected.collect():
    rid, text, prob, prediction = row
    print("(%d, %s) --> prob=%s, prediction=%f" % (rid, text, str(prob), prediction))



