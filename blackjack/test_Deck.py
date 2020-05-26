# test_Deck.py
import pytest
import Deck as d


class TestDeck:

    def test_CanInstantiateDeck(self):
        assert d.Deck() is not None
        