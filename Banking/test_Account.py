# test_Account.py
import pytest
import Account as a 

class TestAccount:
    def test_CanInstantiateAccountObject(self):
        result = a.Account("Tiji", 1000)
        assert result.owner == "Tiji" and result.balance == 1000     

    def test_CanWithdraw(self):
        result = a.Account("Tiji", 1000)
        result.withdraw(10)
        assert result.balance == 990

    def test_CanPreventOverWithdraw(self):
        act = a.Account("Tiji", 10)
        result = act.withdraw(100)
        assert act.balance == 10 and result == False

    def test_CanDeposit(self):
        result = a.Account("Tiji", 1000)
        result.deposit(100)
        assert result.balance == 1100

    def test_HasStringOutputForPrintingValueOfAnInstance(self):
        result = str(a.Account("Tiji", 1000))
        assert result == "Owner: Tiji, Balance: $1000"
        
