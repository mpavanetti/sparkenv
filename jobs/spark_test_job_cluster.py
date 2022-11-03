from pyspark.sql.session import SparkSession
import os
import logging

if __name__ == "__main__":

    spark = (SparkSession
            .builder
            .appName("TestApplicationCluster")
            .master("spark://spark:7077")
            .getOrCreate())


    logging.warning(f"Spark Session Created Object --> {spark}")
    logging.warning(f"Spark Default CPU Cores --> {spark.sparkContext.defaultParallelism}")
    
    df = spark.read.csv("/home/jovyan/work/data/input/test.csv",header=True)
    logging.warning(f"Dataframe partitions --> {df.rdd.getNumPartitions()}")
    
    df.printSchema()

    df.show(20,False)
    
    df.write.mode("overwrite").csv("/home/jovyan/work/data/output/test_output_cluster")
    