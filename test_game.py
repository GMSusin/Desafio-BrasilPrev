from collections import Counter
from models.game import Game
from models.player import Player
import unittest

class TestGame(unittest.TestCase):
       
    def test_win(self):
        rounds = 0
        win_by_timeout = 0
        number_of_games = 0
        winners = []
        for i in range(300):
            game = Game()
            for i in range(4):
                player = Player(f"Player {i+1}", 300, i+1)
                game.add_player(player)
            
            game.play()
            winner = game.get_winner()
            winners.append(winner.name) 
            rounds += game.get_num_rounds()
            win_by_timeout += game.get_win_by_timeout()
            number_of_games += 1

        print(number_of_games)
        counted = Counter(winners)
        sorted_list = sorted(winners, key=lambda x: -counted[x])
        
        count_player1 = winners.count('Player 1')
        count_player2 = winners.count('Player 2')
        count_player3 = winners.count('Player 3')
        count_player4 = winners.count('Player 4')
        
        player1_average_win_rate = (count_player1/number_of_games) * 100
        player2_average_win_rate = (count_player2/number_of_games) * 100
        player3_average_win_rate = (count_player3/number_of_games) * 100
        player4_average_win_rate = (count_player4/number_of_games) * 100
        
        print(f"Quantas partidas terminam por timeout: {win_by_timeout}")
        print("Quantos turnos em média demora uma partida: {:.2f}".format(rounds/number_of_games))
        print("Player 1 venceu em média {:.2f} %".format(player1_average_win_rate))
        print("Player 2 venceu em média {:.2f} %".format(player2_average_win_rate))
        print("Player 3 venceu em média {:.2f} %".format(player3_average_win_rate))
        print("Player 4 venceu em média {:.2f} %".format(player4_average_win_rate))      
        print(f"Qual o comportamento que mais vence: {sorted_list[0]}")


