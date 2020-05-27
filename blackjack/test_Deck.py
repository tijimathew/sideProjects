# test_Deck.py
import Deck as d


class TestDeck:

    gameDeck = d.Deck()

    def test_CanInstantiateSingleDeckOf52Cards(self):
        assert self.gameDeck.nbrOfCards == 52

    def test_CanReturnACardFromTheDeck(self):
        assert self.gameDeck.select() is not None

    def test_WhenACardIsSelectedDeckReducesByOneCard(self):
        beforeCount = len(self.gameDeck.cards)
        self.gameDeck.select()
        afterCount = len(self.gameDeck.cards)
        assert beforeCount - afterCount == 1

    def test_WhenACardIsSelectedDeckWillHaveCurrentNumberOfCardsInDeck(self):
        self.gameDeck.select()
        assert self.gameDeck.nbrOfCards == len(self.gameDeck.cards)

    def test_whenRoundIsResetThenDeckIsRestored(self):
        self.gameDeck.select()
        self.gameDeck.reset()
        assert len(self.gameDeck.cards) == 52
