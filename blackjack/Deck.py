# Deck.py
import random


class Deck:

    def __init__(self):
        self.ranks = {"A": 1, "K": 10, "Q": 10, "J": 10, "10": 10, "9": 9,
                      "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
        self.suits = {"S": "Spade", "C": "Club", "D": "Diamond", "H": "Heart"}
        self.cards = {}
        self.nbrOfCards = len(self.ranks) * len(self.suits)
        for suitKey in self.suits.keys():
            for rankKey in self.ranks.keys():
                self.cards[f"{rankKey}{suitKey}"] = self.ranks[rankKey]

    def select(self):
        key = random.choice(list(self.cards))
        result = {key: self.cards[key]}
        return result
