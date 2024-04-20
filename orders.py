from datetime import datetime, date 

class Order:
    def __init__(self, id, customer_name, date_of_order):
        self.id = id
        self.customer_name = customer_name
        self.date_of_order = date_of_order

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    

    def __repr__(self):
        return f"Order({self.id}, {self.customer_name}, {self.date_of_order})"