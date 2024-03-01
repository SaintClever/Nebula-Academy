class Animal:
    def __init__(self, species):
        self.species = species


# VERSION 00
class Cat(Animal):
    def __init__(self, name, species):
        super().__init__(species)
        self.name = name


my_cat = Cat("Whiskers", "Feline")
print(my_cat.species, my_cat.name)


# VERSION 01
class Cat(Animal):
    def __init__(self, name):
        super().__init__("Feline")
        self.name = name


my_cat = Cat("Whiskers")
print(my_cat.species, my_cat.name)


class Bank:
    def __init__(self, account):
        self.account = account

    def display(self):
        return self.account

    def deposit(self, amount):
        return self.account + amount

    def withdrawal(self, amount):
        return self.account - amount


def show_all(account):
    return account.display()


saint = Bank(100)
print(saint.account, saint.deposit(40), saint.withdrawal(20))
print(show_all(saint))
