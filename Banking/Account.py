# Account.py

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    
    def __str__(self):
        return f"Owner: {self.owner}, Balance: ${self.balance}"

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return True
        else:
            return False


    def deposit(self, amount):
        self.balance += amount