# test_Game.py
import Game as g
import Deck as d


class TestGame:
    game = g.Game()
    gameDeck = d.Deck()

    def test_CanInstantiateGame(self):
        assert self.game is not None

    def test_CanInstantiateHandToDealer(self):
        assert self.game.dealer is not None

    def test_CanInstantiateHand(self):
        assert g.Hand() is not None

    def test_dealerMuststartwith2CardsinHand(self):
        self.game.deal(self.gameDeck)
        assert len(self.game.dealer.hand) == 2

    def test_PlayerMuststartwith2CardsinHand(self):
        self.game.deal(self.gameDeck)
        assert len(self.game.players[0].hand) == 2

    def test_Has13RanksForTheGame(self):
        assert len(g.rankValues) == 13

    def test_HasNoZeroValueCards(self):
        assert list(g.rankValues.values()).count(0) == 0

    def test_FaceCardsHaveValueOf10(self):
        for key in ['K', 'Q', 'J']:
            assert g.rankValues[key] == 10

    def test_PipValueCardsHaveValueMatchingNumberOfPips(self):
        # check the values for cards 2 through 10.
        for i in range(2, 11):
            assert g.rankValues[str(i)] == i

    def test_AceHasValueOf1(self):
        assert g.rankValues['A'] == 1


class TestPerson:

    def test_CanInstantiatePerson(self):
        assert g.Person("Tiji") is not None


class TestPlayer:

    def test_CanInstantiatePlayer(self):
        assert g.Player("Tiji", 1000) is not None


class TestDealer:

    def test_CanInstantiateDealer(self):
        assert g.Dealer() is not None


class TestHand:

    def test_CanInstantiateHand(self):
        assert g.Hand() is not None
