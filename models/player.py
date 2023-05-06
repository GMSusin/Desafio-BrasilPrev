import random

class Player:
    def __init__(self, name, money, player_type):
        self.name = name
        self.current_square = 0
        self.money = money
        self.player_type = player_type
        
    def roll_dice(self):
        return random.randint(1, 6)

    def move(self, num_squares):
        self.current_square = (self.current_square + num_squares) % 20
        return self.current_square

    def is_bankrupt(self):
        return self.money <= 0
    
    def coin_toss():
        return random.choice([True, False])