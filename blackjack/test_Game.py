# test_Game.py
import pytest 
import Game as g


class TestGame:

    def test_CanInstantiateGameForOnePlayer(self):
        assert g.Game() is not None

    def test_CanInstantiatePlayer(self):
        assert g.Player("Tiji", 1000) is not None

    def test_FaceCardsHaveValueOf10(self):
        for key in ['K', 'Q', 'J']:
            assert g.rankValues[key] == 10

    def test_PipValueCardsHaveValueMatchingNumberOfPips(self):
        # check the values for cards 2 through 10.
        for i in range(2, 11):
            assert g.rankValues[str(i)] == i

    def test_AceHasValueOf1(self):
        assert g.rankValues['A'] == 1
