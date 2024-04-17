from homepage.models import UserProfile

class Player:
    def __init__(self, user: UserProfile, side: str):
        self.user = user
        self.currency = user.currency
        self.wins = user.wins
        self.loses = user.loses
        self.side = side

    def add_money(self, amount: int):
        self.currency += amount
        self.user.currency = self.currency
        self.user.save()
    
    def subtract_money(self, amount: int):
        self.currency -= amount
        self.user.currency = self.currency
        self.user.save()