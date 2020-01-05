"""用于 回归预测 作用是根据标签，判断预测是否正确"""
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.linalg import Vectors
from pyspark.shell import sqlContext

# 此数据列表的每个记录都包含标签和向量表示的特征
data = [(0, Vectors.dense(51, 159, 253)),
        (1, Vectors.dense(0.0, 1.0, 1)),
        (1, Vectors.dense(0.0, 1.3, 1)),
        (1, Vectors.dense(2.0, 1.2, 1))]
df = sqlContext.createDataFrame(data, ["label", "features"])
# 设置算法参数 在这里我们将迭代次数限制为10
lr = LogisticRegression(maxIter=10)
print("lr:\n", lr.explainParams())
# fit（dataset，params = None ）
# 使用可选参数将模型拟合到输入数据集
model = lr.fit(df)
# 给定数据集，预测每个点的标签，并显示结果。
print("mode,show:\n", model.transform(df).show())
