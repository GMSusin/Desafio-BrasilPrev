class Square:
    def __init__(self, name, rent_price, sell_price, owner=None):
        self.name = name
        self.rent_price = rent_price
        self.sell_price = sell_price
        self.owner = owner

    def is_owned(self):
        return self.owner is not None
    
        