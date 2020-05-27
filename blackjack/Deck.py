# Deck.py
import random


rankNames = {"A": "Ace", "K": "King", "Q": "Queen", "J": "Jack", "10": "Ten", "9": "Nine", "8": "Eight", "7": "Seven", "6": "Six", "5": "Five", "4": "Four", "3": "Three", "2": "Two"}
suits = {"S": "Spade", "C": "Club", "D": "Diamond", "H": "Heart"}

class Card:
    
    def __init__(self, rank, suit):
        self.id = str(rank) + suit
        self.rank = rank
        self.rankName = rankNames[rank]
        self.suit = suit
        self.suitName = suits[suit]
        self.longName = self.rankName + " of " + self.suitName

class Deck:

    def __init__(self):
        self.cards = []
        for suitKey in suits.keys():
            for rankKey in rankNames.keys():
                self.cards.append(Card(rankKey, suitKey))
        
        self.nbrOfCards = len(self.cards)
        
    def select(self):
        selectedIndex = random.choice(range(0, len(self.cards)))
        self.nbrOfCards -= 1
        return self.cards.pop(selectedIndex)

    def reset(self):
        self.__init__()

