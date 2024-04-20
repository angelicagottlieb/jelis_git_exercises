from lib.items import *


def test_item_constructs():
    item = Item(1, 'Pink Top', 10, 100)
    assert item.id == 1
    assert item.name == 'Pink Top'
    assert item.price == 10
    assert item.quantity_available == 100


def test_construct_formats_nicely_items():
    item = Item(1, 'Pink Top', 10, 100)
    assert str(item) == "Item(1, Pink Top, 10, 100)"

def test_is_equal_for_items():
    item1 = Item(1, 'Pink Top', 10, 100)
    item2 = Item(1, 'Pink Top', 10, 100)
    assert item1 == item2