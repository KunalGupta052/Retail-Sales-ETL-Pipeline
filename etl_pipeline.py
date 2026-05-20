from pyspark.sql import SparkSession
from pyspark.sql.functions import col, month, year, sum as spark_sum, round as spark_round
import os

# ─── Initialize Spark ───────────────────────────────────────────────
spark = SparkSession.builder \
    .appName("Retail Sales ETL Pipeline") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# ─── 1. EXTRACT ──────────────────────────────────────────────────────
print("\n>>> [EXTRACT] Reading sales data...")
df = spark.read.csv("data/sales_data.csv", header=True, inferSchema=True)
print(f"    Total records loaded: {df.count()}")

# ─── 2. TRANSFORM (Clean) ────────────────────────────────────────────
print("\n>>> [TRANSFORM] Cleaning data...")

# Drop duplicate rows
df = df.dropDuplicates()

# Drop rows with null values in critical columns
df = df.dropna(subset=["product", "quantity", "price"])

# Add revenue column
df = df.withColumn("revenue", spark_round(col("quantity") * col("price"), 2))

print(f"    Records after cleaning: {df.count()}")

# ─── 3. ANALYZE ──────────────────────────────────────────────────────
print("\n>>> [ANALYZE] Running sales analysis...")

# Total Revenue
total_revenue = df.agg(spark_sum("revenue").alias("total_revenue")).collect()[0]["total_revenue"]
print(f"\n    Total Revenue: ₹{total_revenue:,.2f}")

# Top-Selling Products (by revenue)
print("\n    Top-Selling Products:")
top_products = df.groupBy("product") \
    .agg(spark_sum("revenue").alias("total_revenue")) \
    .orderBy(col("total_revenue").desc())
top_products.show(5, truncate=False)

# Monthly Sales
print("    Monthly Sales:")
monthly_sales = df.withColumn("month", month("order_date")) \
    .withColumn("year", year("order_date")) \
    .groupBy("year", "month") \
    .agg(spark_sum("revenue").alias("monthly_revenue")) \
    .orderBy("year", "month")
monthly_sales.show(truncate=False)

# ─── 4. LOAD (Save Output) ───────────────────────────────────────────
print("\n>>> [LOAD] Saving cleaned data and reports...")

os.makedirs("output", exist_ok=True)

# Save cleaned data as single CSV using pandas
df.toPandas().to_csv("output/cleaned_sales.csv", index=False)
top_products.toPandas().to_csv("output/top_products.csv", index=False)
monthly_sales.toPandas().to_csv("output/monthly_sales.csv", index=False)

print("    Saved: output/cleaned_sales.csv")
print("    Saved: output/top_products.csv")
print("    Saved: output/monthly_sales.csv")
print("\n>>> ETL Pipeline completed successfully!\n")

spark.stop()
