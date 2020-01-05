"""管道调优，利用交叉验证的方式，将其普通管道的模型调优为 概率更高的概率和标签"""

from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.feature import Tokenizer
from pyspark.ml.feature import HashingTF
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.sql import SparkSession

# 建立spark
spark = SparkSession.builder.appName("CrossValidatorExample").getOrCreate()
# 训练文件
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
# 我们现在将管道视为估算器，将其包装在CrossValidator实例中
# 这将使我们能够共同选择所有管道阶段的参数。
# CrossValidator需要一个Estimator，一组Estimator ParamMaps和一个Evaluator。
# 我们使用ParamGridBuilder构造要搜索的参数网格。
# 对于hashingTF.numFeatures具有3个值，对于lr.regParam具有2个值，
# 该网格将具有3 x 2 = 6个参数设置，供CrossValidator选择
paramGrid = ParamGridBuilder()\
    .addGrid(hashingTF.numFeatures, [10, 100, 1000])\
    .addGrid(lr.regPara/m, [0.1, 0.01])\
    .build()

crossval = CrossValidator(estimator=pipeline,
                          estimatorParamMaps=paramGrid,
                          evaluator=BinaryClassificationEvaluator(),
                          numFolds=4)
# 运行交叉验证，然后选择最佳的参数集
cvModel = crossval.fit(training)
# 测试数据
test = spark.createDataFrame([
        (4, "spark i j k"),
        (5, "l m n"),
        (6, "mapreduce spark"),
        (7, "apache hadoop")
    ], ["id", "text"])
print("show:\n", cvModel.transform(test).show())
