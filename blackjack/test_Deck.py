# test_Deck.py
import pytest
import Deck as d


class TestDeck:
    gameDeck = d.Deck()

    def test_CanInstantiateSingleDeckOf52Cards(self):
        assert self.gameDeck.nbrOfCards == 52

    def test_CanReturnACardFromTheDeck(self):
        assert self.gameDeck.select() is not None 

