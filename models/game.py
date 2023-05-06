from .board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.players = []
        self.current_player_index = 0
        self.turn_counter = 0
        self.rounds = 0
        self.win_by_timeout = 0

    def add_player(self, player):
        self.players.append(player)

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play(self):
        while True:
            self.turn_counter += 1
            if len(self.players) == 1:
                break
            if self.turn_counter > 1000:
                # print("Maximum number of turns reached!")
                self.winner = max(self.players, key=lambda p: p.money)
                # print(f"{self.winner.name} is the Winner")
                self.win_by_timeout = 1
                break
            player = self.players[self.current_player_index % len(self.players)]
            # print(f"{player.name}'s turn")
            roll = player.roll_dice()
            # print(f"{player.name} rolled {roll}")
            player.move(roll)
            # print(f"{player.current_square} current ")
            if player.current_square >= self.board.size:
                player.current_square -= self.board.size
                player.money += 100
            
            space = self.board.get_square(player.current_square)
            if space.owner is None:
                self.buy_square(space, player)
            else:
                if player.money >= space.rent_price:
                    self.pay_rent(space, player)
                    
            if player.is_bankrupt():
                # print(f"{player.name} is bankrupt!")
                self.players.remove(player)
            if len(self.players) == 1:
                # print(f"{self.players[0].name} wins!")
                self.winner = self.players[0]
                break
            self.next_player()
            self.rounds += 1
            
    def buy_square(self, square, player):
        if player.player_type == 1:
            if player.money >= square.sell_price:
                player.money -= square.sell_price
                square.owner = player
                
        elif player.player_type == 2:
            if player.money >= square.sell_price and square.rent_price > 50:
                player.money -= square.sell_price
                square.owner = player
                
        elif player.player_type == 3:
            if player.money >= square.sell_price and (player.money - square.sell_price) >= 80:
                player.money -= square.sell_price
                square.owner = player
                
        elif player.player_type == 4:
            if player.money >= square.sell_price and player.coin_toss == True:
                player.money -= square.sell_price
                square.owner = player

    def pay_rent(self, square, player):
        rent = square.rent_price
        player.money -= rent
        square.owner.money += rent       

    def get_winner(self):
        return self.winner
    
    def get_num_rounds(self):
        return self.rounds
    
    def get_win_by_timeout(self):
        return self.win_by_timeout