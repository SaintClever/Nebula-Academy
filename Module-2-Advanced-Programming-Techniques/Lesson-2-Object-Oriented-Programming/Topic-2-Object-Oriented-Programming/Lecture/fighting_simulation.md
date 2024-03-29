## Character Fighting Loop Problems 🥊

### Problem 1: Defining the Character Class 🛠️
**Task**: Define a base class `Character` with attributes for `name`, `hp` (health points), and `atk` (attack damage). Include methods for `attack(other)` where `other` is another character, and `is_alive()` to check if the character's `hp` is above 0.

#### Hint
Consider how you can use the `__init__` method to initialize each character's attributes. The `attack` method should reduce the `hp` of the `other` character by the attacker's `atk` value. `is_alive` should return a boolean value.

### Problem 2: Extending the Character Class 🌱
**Task**: Create two subclasses of `Character`: `Hero` and `Villain`. Each subclass should have a unique attribute or method that reflects their role. For example, a `Hero` might have a higher chance to dodge an attack, while a `Villain` could have a counterattack ability.

#### Hint
Use inheritance to define the subclasses. Override or add methods in these subclasses to incorporate their unique abilities. Think about how these abilities will affect the flow of a fight.

### Problem 3: Simulating a Battle ⚔️
**Task**: Implement a `battle` function that takes two instances of `Character` (they could be a `Hero`, a `Villain`, or any `Character`) and simulates a fight between them. The fight occurs in turns, and ends when one of the characters no longer `is_alive()`. Print the outcome of each attack and the winner at the end.

#### Hint
You'll need a loop that continues until one of the characters dies. On each iteration, one character attacks the other, then you check if the defender is still alive. If they are, the roles reverse. Use the methods you've defined on the characters to handle the logic of attacking and checking health.

## Challenge Problems 🚀

### Challenge 1: Implement Special Abilities 🔮
**Task**: Enhance the `Hero` and `Villain` classes with special abilities that have a cooldown or a condition to trigger. For example, a `Hero` might have a "Heal" ability that they can use once every three turns, while a `Villain` might have a "Poison" attack that does additional damage over time.

#### Hint
Think about adding attributes to track the state of these abilities (e.g., whether they are on cooldown). You might need to override the `attack` method to incorporate the logic for these abilities, and possibly update the `battle` function to apply effects like poison over time.

### Challenge 2: Battle Royale 🎯
**Task**: Create a function `battle_royale(participants)` where `participants` is a list of `Character` instances. This function should simulate a free-for-all battle where each character randomly chooses another to attack each turn. The battle continues until only one character is left standing.

#### Hint
You'll need a way to randomly select targets for each character's attack, ensuring that a character cannot target themselves and only targets alive opponents. After each turn, check if only one character remains alive, and declare them the winner. Consider how the dynamics of multiple participants might affect the implementation of special abilities and strategies.

---