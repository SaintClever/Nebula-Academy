class Character:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack(self, other):
        other.hp -= self.atk
        print(f"{self.name} attacks {other.name} for {self.atk} damage.")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: HP={self.hp}, ATK={self.atk}"


class Human(Character):
    def attack(self, other):
        super().attack(other)
        print(f"{self.name} (Human) bravely strikes!")


class Orc(Character):
    def attack(self, other):
        super().attack(other)
        print(f"{self.name} (Orc) ferociously assaults!")


def fight(char1, char2):
    turn = 0
    while char1.is_alive() and char2.is_alive():
        print(char1, "|", char2)
        if turn % 2 == 0:
            char1.attack(char2)
        else:
            char2.attack(char1)
        turn += 1
    if char1.is_alive():
        print(f"{char1.name} is victorious")
    else:
        print(f"{char2.name} is victorious")


human = Human("Arthur", 100, 20)
orc = Orc("Grok", 120, 15)

print(human, "__self__")
print(orc, "__self__")

fight(human, orc)
