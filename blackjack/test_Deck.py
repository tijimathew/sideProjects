# test_Deck.py
import pytest
import Deck as d


class TestDeck:

    def test_CanInstantiateDeck(self):
        assert d.Deck() is not None

#    def test_hasCardObject(self):
#        assert d.Deck().card is not None