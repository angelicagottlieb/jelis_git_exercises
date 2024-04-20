from lib.orders import *
from datetime import datetime, date


def test_order_constructs():
    order = Order(1, 'Angelica', date(2023, 5, 3))
    assert order.id == 1
    assert order.customer_name == 'Angelica'
    assert order.date_of_order == date(2023, 5, 3)


def test_construct_formats_nicely_orders():
    order = Order(1, 'Angelica', date(2023, 5, 3))
    assert str(order) == "Order(1, Angelica, 2023-05-03)"

def test_is_equal_for_items():
    order1 = Order(1, 'Angelica', date(2023, 5, 3))
    order2 = Order(1, 'Angelica', date(2023, 5, 3))
    assert order1 == order2

