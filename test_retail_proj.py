import pytest
from lib.DataReader import read_customers,read_orders
from lib.DataManipulation import *
from lib.ConfigReader import get_app_config




# Using Unit test cases we will check below conditions:
# 1. read_customers_df == 20
# 2. read_orders_df == 20
# 3. filter_closed_orders == 10
# 4. read_app_config (Using read_app_config we will verify all the configurations.)
# 5. check if the count_orders_state function works correctly

@pytest.mark.skip()
def test_read_customers_df(spark):
    customers_count = read_customers(spark, "LOCAL").count()
    assert customers_count == 20

@pytest.mark.skip()    
def test_read_orders_df(spark):
    orders_count = read_orders(spark, "LOCAL").count()
    assert orders_count == 20


@pytest.mark.skip()
def test_filter_closed_orders(spark):
    orders_df = read_orders(spark, "LOCAL")
    filtered_orders_count = filter_closed_orders(orders_df).count()
    assert filtered_orders_count == 4

@pytest.mark.skip()
def test_read_app_config():
    configs = get_app_config("LOCAL")
    assert configs["customers.file.path"] == "data/customers.csv"
    

@pytest.mark.skip()
def test_count_orders_state(spark, expected_results):
    customers_df = read_customers(spark, "LOCAL")
    aggegate_states = count_orders_state(customers_df)
    assert aggegate_states.collect() == expected_results.collect()
    
    
@pytest.mark.parametrize("status, count",
                          [
                            ("CLOSED", 4),
                            ("PENDING_PAYMENT", 6),
                            ("COMPLETE", 6)
                          ]
                          )
def test_count_orders_generic_by_status(spark, status, count):
    orders_df = read_orders(spark, "LOCAL")
    orders_count = count_orders_generic_by_status(orders_df, status)
    assert orders_count == count 
    