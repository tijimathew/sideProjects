# Game.py
rankValues = {"A": 1, "K": 10, "Q": 10, "J": 10, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

class Game:

    def __init__(self, nbrOfPlayers=1):
        self.nbrOfPlayers = nbrOfPlayers


class Player:

    def __init__(self, name, fundAmount):
        self.name = name
        self.fundAmount = fundAmount
