from .square import Square

class Board:
    def __init__(self):
        self.squares = []
        self.create_spaces()
        self.size = len(self.squares)
        self.populate_board()

    def create_spaces(self):
        for i in range(20):
            name = f"Square {i+1}"
            rent_price = i * 10
            sell_price = i * 20
            square = Square(name, rent_price, sell_price)
            self.squares.append(square)
    
    def get_square(self, index):
        return self.squares[index]
    
    def populate_board(self):
        building_names = ["Hotel", "Apartment", "Office", "Mall", "Restaurant", "Cinema", "Gym", "Park", "Hospital", "School"]
        for i, square in enumerate(self.squares):
            building_name = building_names[i % len(building_names)]
            sell_price = (i + 1) * 50
            rent_price = sell_price // 2
            square.name = f"{building_name} Square"
            square.sell_price = sell_price
            square.rent_price = rent_price