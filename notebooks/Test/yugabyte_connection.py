# Databricks notebook source
df = spark.read \
   .format("jdbc") \
   .option("url", "jdbc:postgresql://us-east-1.1e7bb9df-f861-4305-85e1-d3c03984cbf7.aws.ybdb.io:5433/yugabyte") \
   .option("dbtable", "public.t1") \
   .option("user", "admin") \
   .option("driver", "org.postgresql.Driver") \
   .option("password", "Admin@123") \
   .option("useSSL", "true") \
   .option("ssl", "true") \
   .option("sslmode", "require") \
   .option("sslrootcert", "dbfs:/FileStore/root__2_.crt") \
   .load()