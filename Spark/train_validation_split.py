"""线性回归算法，来生成用户标签"""
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.regression import LinearRegression
from pyspark.ml.tuning import ParamGridBuilder, TrainValidationSplit
from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .appName("TrainValidationSplit")\
    .getOrCreate()

# 准备数据集
data = spark.read.format("libsvm").load("F:\\上传路径\\sample_linear_regression_data.txt")
# train 训练数据 test 测试数据
train, test = data.randomSplit([0.95, 0.05], seed=12345)
print("train:\n", train.collect(), "\ntest:\n", test.collect())

lr = LinearRegression(maxIter=10)
# 我们使用ParamGridBuilder构造要搜索的参数网格
# TrainValidationSplit将尝试所有值的组合并使用以下方法确定最佳模型评估者。
paramGrid = ParamGridBuilder()\
    .addGrid(lr.regParam, [0.1, 0.01])\
    .addGrid(lr.fitIntercept, [False, True])\
    .addGrid(lr.elasticNetParam, [0.0, 0.5, 1.0])\
    .build()
print("paramGrid:\n", paramGrid)
# 在这种情况下，估计量只是线性回归
# TrainValidationSplit需要一个Estimator，一组Estimator ParamMaps和一个Evaluator。
# 80％的数据将用于训练，20％的数据将用于验证
tvs = TrainValidationSplit(estimator=lr,
                           estimatorParamMaps=paramGrid,
                           evaluator=RegressionEvaluator(),
                           trainRatio=0.8)
# 运行TrainValidationSplit，然后选择最佳的参数集
model = tvs.fit(train)
# print(model.transform(test).show())
model.transform(test)\
        .select("features", "label", "prediction")\
        .show()

