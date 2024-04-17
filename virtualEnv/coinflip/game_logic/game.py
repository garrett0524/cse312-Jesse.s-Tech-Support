from game_logic import Player
from random import random

class Game:
    def __init__(self, player1: Player):
        self.player1 = player1
        self.player2 = None

    def play(self, bet: int):
        winningSide = random.choice(['heads', 'tails'])
        if winningSide == self.player2.side:
            self.player2.add_money(bet)
            self.player1.subtract_money(bet)
            self.player2.wins += 1
            self.player1.loses += 1
        else:
            self.player1.add_money(bet)
            self.player2.subtract_money(bet)
            self.player1.wins += 1
            self.player2.loses += 1
        
