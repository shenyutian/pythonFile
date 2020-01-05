from pyspark.python.pyspark.shell import sqlContext

url = "jdbc:mysql://127.0.0.1:3306/cellphone?" \
      "user=root;password=123456"
df = sqlContext.read.format("jdbc").option("url", url)\
    .option("dbtable", "soc").load()
df.printSchema()
# 计算每个类型的数量
counts = df.groupBy("soc_trademark").count()

counts.write.format("json").save("/outsql")
