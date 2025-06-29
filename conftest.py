import pytest
from lib.Utils import get_spark_session
from lib.DataReader import read_customers
from lib.DataManipulation import count_orders_state


@pytest.fixture
def spark():
    "Creates a Spark session"
    spark_session = get_spark_session("LOCAL")
    yield spark_session
    spark_session.stop()
    
@pytest.fixture
def expected_results(spark):
    "returns state aggregate csv datafarme"
    return spark.read \
        .format("csv") \
            .schema("state string, count int") \
                .load("data/test_result/state_aggregate.csv")
