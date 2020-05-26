# test_Deck.py
import pytest
import Deck as d


class TestDeck:
    gameDeck = d.Deck()

    def test_CanInstantiateSingleDeckOf52Cards(self):
        assert self.gameDeck.nbrOfCards == 52

    def test_CanReturnACardFromTheDeck(self):
        assert len(self.gameDeck.select()) == 1

    def test_FaceCardsHaveValueOf10(self):
        for key in ['K', 'Q', 'J']:
            assert self.gameDeck.ranks[key] == 10

    def test_PipValueCardsHaveValueMatchingNumberOfPips(self):
        # check the values for cards 2 through 10.
        for i in range(2, 11):
            assert self.gameDeck.ranks[str(i)] == i

    def test_AceHasValueOf1(self):
        assert self.gameDeck.ranks['A'] == 1