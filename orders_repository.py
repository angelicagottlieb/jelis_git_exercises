from lib.orders import *
from datetime import datetime, date

class OrderRepository:

    def __init__(self, connection):
        self._connection = connection

    # Retrieve all items
    def all(self):
        rows = self._connection.execute('SELECT * from orders')
        orders = []
        for row in rows:
            item = Order(row["id"], row["customer_name"], row["date_of_order"])
            orders.append(item)
        return orders


    # Create a new item
    def create(self, order):
        self._connection.execute('INSERT INTO orders (customer_name, date_of_order) VALUES (%s, %s)', [
                                order.customer_name, order.date_of_order])
        # return "New order has been added!"
        return "New order has been created" 
