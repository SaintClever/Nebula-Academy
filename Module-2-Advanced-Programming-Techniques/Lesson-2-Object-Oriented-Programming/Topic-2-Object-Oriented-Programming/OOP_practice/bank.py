import random


class BankAccount:
    def __init__(self, owner, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return self.balance

    def display_account_info(self):
        return f"Account #: {self.account_number} Owner: {self.owner} Balance: ${self.balance}"


# Create an account
account1 = BankAccount(account_number=2473, owner="Alice", balance=500_000)
print(account1.display_account_info())
