from pyspark.sql.functions import *

# filter orders with status 'CLOSED'
def filter_closed_orders(orders_df):
    return orders_df.filter("order_status = 'CLOSED'")


# join filtered orders df with customers dataframes on customer_id
def join_orders_customers(orders_df, customers_df):
    return orders_df.join(customers_df, "customer_id")


# count joined dataframe by state
def count_orders_state(joined_df):
    return joined_df.groupBy('state').count()


# returns count of orders by status
def count_orders_generic_by_status(df, order_status):
    return df.filter("order_status == '{}'".format(order_status)).count()
