# Databricks notebook source
dbutils.fs.ls ("/tmp/test-folder")

# COMMAND ----------

f = "/tmp/test-folder/test2.json"
df = spark.read.json(f)
df.show()

# COMMAND ----------


