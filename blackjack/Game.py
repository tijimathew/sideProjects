# Game.py
import Deck as d

rankValues = {"A": 1, "K": 10, "Q": 10, "J": 10, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

class Game:

    def __init__(self, nbrOfPlayers=1):
        self.nbrOfPlayers = nbrOfPlayers
        self.players = []
        self.dealer = Dealer()
        for i in range(0, nbrOfPlayers-1):
            print(f"Register Player #{i+1}")
            playerName = input("Enter player name : ")
            entryAmount = int(input("How much money are willing to bet ? "))
            self.players[i] = Player(playerName, entryAmount)
        
    def deal(self, gameDeck):
        # Going around the table, deal 1 card to each player (including the dealer) 
        # until everyone has 2 cards each.
        for i in range(0, 1):
            self.dealer.hand.append(gameDeck.select())
            for player in self.players:
                player.hand.append(gameDeck.select())
        


class Person:

    def __init__(self, name):
        self.name = name
    


class Player(Person):

    def __init__(self, name, balance):
        Person.__init__(self, name)
        self.balance = balance 
        self.hand = []

class Dealer(Person):

    def __init__(self):
        self.name = 'Dealer'
        self.balance = 0
        self.hand = []

class Hand:

    def __init__(self):
        self.cards = []
        self.total = 0

    