from lib.orders_repository import *
from lib.orders import *
from datetime import datetime, date


def test_get_all_records_for_orders(db_connection): # See conftest.py to learn what `db_connection` is.
    # db_connection.seed("seeds/shop_manager.sql") # Seed our database with some test data
    repository = OrderRepository(db_connection) # Create a new ArtistRepository

    orders = repository.all() # Get all artists

    # Assert on the results
    assert orders == [
        Order(1, 'Jeli', date(2023, 5, 1)),
        Order(2, 'Elior', date(2023, 5, 2))
    ]

def test_create_record_for_orders(db_connection):
    # db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

    repository.create(Order(None, "Jake", date(2023, 5, 5)))

    result = repository.all()
    assert result == [
        Order(1, 'Jeli', date(2023, 5, 1)),
        Order(2, 'Elior', date(2023, 5, 2)),
        Order(3, 'Jake', date(2023, 5, 5))
    ]