from lib.items_repository import ItemRepository
from lib.items import Item
from lib.database_connection import DatabaseConnection


def test_get_all_records_for_items(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/shop_manager.sql") # Seed our database with some test data
    repository = ItemRepository(db_connection) # Create a new ArtistRepository

    items = repository.all_items() # Get all artists

    # Assert on the results
    assert items == [
        Item(1, "Pink Top", 10, 100),
        Item(2, "Blue Top", 15, 200)
    ]
    print(items)

def test_create_record_for_items(db_connection):
    # db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    repository.create_item(Item(None, "Red Top", 20, 250))

    result = repository.all_items()
    assert result == [
        Item(1, "Pink Top", 10, 100),
        Item(2, "Blue Top", 15, 200),
        Item(3, "Red Top", 20, 250)
    ]

