import random

# ## Character Fighting Loop Problems 🥊


# ### Problem 1: Defining the Character Class 🛠️
# **Task**: Define a base class `Character` with attributes for `name`, `hp` (health points), and `atk` (attack damage). Include methods for `attack(other)` where `other` is another character, and `is_alive()` to check if the character's `hp` is above 0.


# #### Hint
# Consider how you can use the `__init__` method to initialize each character's attributes. The `attack` method should reduce the `hp` of the `other` character by the attacker's `atk` value. `is_alive` should return a boolean value.


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


# ### Problem 2: Extending the Character Class 🌱
# **Task**: Create two subclasses of `Character`: `Hero` and `Villain`. Each subclass should have a unique attribute or method that reflects their role. For example, a `Hero` might have a higher chance to dodge an attack, while a `Villain` could have a counterattack ability.

# #### Hint
# Use inheritance to define the subclasses. Override or add methods in these subclasses to incorporate their unique abilities. Think about how these abilities will affect the flow of a fight.


class Hero(Character):
    def attack(self, other):
        super().attack(other)
        print(f"{self.name} bravely strikes!")

    def heal(self):
        self.hp += 5
        print(f"{self.name} HP+ went UP!")


class Villain(Character):
    def attack(self, other):
        super().attack(other)
        print(f"{self.name} ferociously assaults!")

    def poison_attack(self, other):
        other.hp -= 2
        print(f"{self.name} strikes and {other.name} loses additional HEALTH!")


# ### Problem 3: Simulating a Battle ⚔️
# **Task**: Implement a `battle` function that takes two instances of `Character` (they could be a `Hero`, a `Villain`, or any `Character`) and simulates a fight between them. The fight occurs in turns, and ends when one of the characters no longer `is_alive()`. Print the outcome of each attack and the winner at the end.


# #### Hint
# You'll need a loop that continues until one of the characters dies. On each iteration, one character attacks the other, then you check if the defender is still alive. If they are, the roles reverse. Use the methods you've defined on the characters to handle the logic of attacking and checking health.
def battle(char1, char2):
    turn = 0

    while char1.is_alive() and char2.is_alive():
        print(char1, "|", char2)

        if turn % 2 == 0:
            char1.attack(char2)
        else:
            char2.attack(char1)
        turn += 1

        if turn % 3 == 0:
            char1.heal()
            char2.poison_attack(char1)

    if char1.is_alive():
        print(f"{char1.name} is victorious")
    else:
        print(f"{char2.name} is victorious")


spiderman = Hero("Spiderman", 100, 7)
batman = Hero("Batman", 85, 8)
onepunch_man = Hero("One Punch Man", 100, 10)
erin_brockovich = Hero("Erin Brockovich", 75, 8)
wicked_witch_of_the_west = Hero("Wicked Witch of the West", 85, 5)

venom = Villain("Venom", 90, 8)
agent_smith = Villain("Agent Smith", 95, 8)
voldemort = Villain("voldemort", 105, 5)
pennywise = Villain("Pennywise", 115, 8)
loki = Villain("Loki", 85, 7)

print(spiderman, "__self__")
print(venom, "__self__")

battle(spiderman, venom)
print()

# ## Challenge Problems 🚀

# ### Challenge 1: Implement Special Abilities 🔮
# **Task**: Enhance the `Hero` and `Villain` classes with special abilities that have a cooldown or a condition to trigger. For example, a `Hero` might have a "Heal" ability that they can use once every three turns, while a `Villain` might have a "Poison" attack that does additional damage over time.


# #### Hint
# Think about adding attributes to track the state of these abilities (e.g., whether they are on cooldown). You might need to override the `attack` method to incorporate the logic for these abilities, and possibly update the `battle` function to apply effects like poison over time.

# ### Challenge 2: Battle Royale 🎯
# **Task**: Create a function `battle_royale(participants)` where `participants` is a list of `Character` instances. This function should simulate a free-for-all battle where each character randomly chooses another to attack each turn. The battle continues until only one character is left standing.

# #### Hint
# You'll need a way to randomly select targets for each character's attack, ensuring that a character cannot target themselves and only targets alive opponents. After each turn, check if only one character remains alive, and declare them the winner. Consider how the dynamics of multiple participants might affect the implementation of special abilities and strategies.

# ---

print(f"\n {10 * " * "} BATTLE ROYALE {10 * " * "}")


def battle_royale(participants):

    turn = random.randint(0, 100)

    heros = []
    villains = []

    for char in list(random.sample(participants, 8)):
        if type(char) == Hero:
            heros.append(char)
        else:
            villains.append(char)

    char1, char2, char3, char4, char5, char6, char7, char8 = heros + villains

    while (
        char1.is_alive()
        and char2.is_alive()
        and char3.is_alive()
        and char4.is_alive()
        and char5.is_alive()
        and char6.is_alive()
        and char7.is_alive()
        and char8.is_alive()
    ):
        print(
            f"\n{char1}\n{char2}\n{char3}\n{char4}\n{char5}\n{char6}\n{char7}\n{char8}\n"
        )

        if turn % 2 == 0:
            char1.attack(char5)
            char2.attack(char6)
            char3.attack(char7)
            char4.attack(char8)
        else:
            char5.attack(char1)
            char6.attack(char2)
            char7.attack(char3)
            char8.attack(char4)
        turn += 1

        if turn % 3 == 0:
            char5.attack(char1)
            char6.attack(char2)
            char7.attack(char3)
            char8.attack(char4)
        else:
            char1.attack(char5)
            char2.attack(char6)
            char3.attack(char7)
            char4.attack(char8)
        turn += 1

        if turn % 2 == 0:
            char1.heal()
            char2.heal()
            char3.heal()
            char4.heal()

        if turn % 3 == 0:
            char5.poison_attack(char1)
            char6.poison_attack(char2)
            char7.poison_attack(char3)
            char8.poison_attack(char4)

    if char1.is_alive() and char2.is_alive() and char3.is_alive() and char4.is_alive():
        print(
            f"\n🥊 {char1.name}, {char2.name}, {char3.name} and {char4.name} are victorious! 🥊"
        )
    elif (
        char5.is_alive() and char6.is_alive() and char7.is_alive() and char8.is_alive()
    ):
        print(
            f"\n🥊 {char5.name}, {char6.name}, {char7.name} and {char8.name} are victorious! 🥊"
        )


battle_royale(
    [
        batman,
        onepunch_man,
        erin_brockovich,
        wicked_witch_of_the_west,
        agent_smith,
        voldemort,
        pennywise,
        loki,
    ]
)
