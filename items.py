class Item:
    def __init__(self, id, name, price, quantity_available):
        self.id = id
        self.name = name
        self.price = price
        self.quantity_available = quantity_available

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    

    def __repr__(self):
        return f"Item({self.id}, {self.name}, {self.price}, {self.quantity_available})"