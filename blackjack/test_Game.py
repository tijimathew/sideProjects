# test_Game.py
import pytest 
import Game as g


class TestGame:

    def test_CanInstantiateGameForOnePlayer(self):
        assert g.Game() is not None

    def test_CanInstantiatePlayer(self):
        assert g.Player("Tiji", 1000) is not None
