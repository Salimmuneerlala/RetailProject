from pyspark.sql import *
from lib.Utils import get_spark_session
from lib.DataReader import read_customers, read_orders


def get_normal_agg_spark_session():
    spark = get_spark_session("LOCAL")
    customers_df = read_customers(spark, "LOCAL")
    orders_df = read_orders(spark, "LOCAL")
    customers_df.createOrReplaceTempView("customers_df")
    orders_df.createOrReplaceTempView("orders_df")
    agg_states = spark.sql("""
              select state,count(state) from customers_df
              group by state
              """)
    agg_states.write \
        .mode("overwrite") \
            .format("csv") \
        .save("data/test_result/")


get_normal_agg_spark_session()