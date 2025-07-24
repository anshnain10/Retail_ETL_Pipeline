from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp, to_date, date_format, col, round

# Step 1: Spark session
spark = SparkSession.builder \
    .appName("Retail_ETL") \
    .getOrCreate()

# Step 2: Load data (from mounted volume)
df = spark.read.options(header=True, inferSchema=True).csv("/Users/ansh/etl-pipeline/data/retail_data.csv")

# Step 3: Clean and transform
df = df.withColumn("InvoiceTimeStamp", to_timestamp("InvoiceDate")) \
       .withColumn("InvoiceDateOnly", to_date("InvoiceTimeStamp")) \
       .withColumn("InvoiceTimeOnly", date_format("InvoiceTimeStamp", "HH:mm")) \
       .drop("InvoiceTimeStamp") \
       .dropna(subset=["CustomerID", "InvoiceNo"]) \
       .filter(~col("InvoiceNo").startswith("C")) \
       .filter((col("UnitPrice") > 0) & (col("Quantity") > 0)) \
       .withColumn("TotalPrice", round(col("Quantity") * col("UnitPrice"), 2))

df.show(5)

# Step 4: Write to HDFS
df.write.mode("overwrite").option("header", True).csv("/Users/ansh/etl-pipeline/output/cleaned_data")  # or use "parquet"

