from lib.items import *
from lib.database_connection import *

class ItemRepository:

    def __init__(self, connection):
        self._connection = connection

    # Retrieve all items
    def all_items(self):
        rows = self._connection.execute('SELECT * from items')
        items = []
        for row in rows:
            item = Item(row["id"], row["name"], row["price"],row["quantity_available"])
            items.append(item)
        return items


    # Create a new item
    def create_item(self, item):
        self._connection.execute('INSERT INTO items (name, price, quantity_available) VALUES (%s, %s, %s)', [
                                item.name, item.price, item.quantity_available])
        # return "New item has been added!"
        return "New item has been created"  
    