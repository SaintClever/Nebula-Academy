# ## Vehicle Racing Simulation

# ### Context
# Modern vehicle racing, where different types of vehicles (cars, motorcycles, and trucks) compete in a race.


# ### Problem 1: Define the Base Class
# **Task**: Define a base class `Vehicle` with attributes like `name`, `speed`, and `reliability`. Methods might include `move` (to advance in the race) and `breakdown` (chance of vehicle failure).


# #### Hint
# Start by defining your class with the `__init__` method to initialize the attributes. For the `move` method, consider how you might simulate movement based on the vehicle's speed. The `breakdown` method could randomly affect the vehicle based on its reliability.


class Vechicle:
    def __init__(self, name: str, speed: int = 0, reliability: int = 0):
        self.name = name
        self.speed = speed
        self.reliability = reliability

    def move(self):
        return self.speed

    def breakdown(self):
        return self.reliability

    def __str__(self):
        return f"{self.name}: speed={self.speed}, reliability={self.reliability}"


# ### Problem 2: Create Subclasses
# **Task**: Create subclasses `Car`, `Motorcycle`, and `Truck`, inheriting from `Vehicle`, each with unique characteristics or methods (e.g., different reliability factors or speed adjustments).


# #### Hint
# Use inheritance to create each subclass. Override or add to the base class methods and attributes to reflect the unique properties of each vehicle type. Consider how each vehicle's speed and reliability might differ and implement those differences in your subclasses.


class Car(Vechicle):
    def __init__(self):
        super().__init__("Mazda: RX-7", 120, 4.0)


class Motorcycle(Vechicle):
    def __init__(self):
        super().__init__("Yamaha: R1", 182, 4.5)


class Truck(Vechicle):
    def __init__(self):
        super().__init__("Tesla: Cybertruck", 130, 5.0)


# ### Problem 3: Implement the Race Function
# **Task**: Implement a `race` function where instances of these vehicles compete on a track of a specified distance. The race continues in a loop until one vehicle crosses the finish line, considering potential breakdowns affecting the outcome.

# #### Hint
# Your `race` function will need to keep track of each vehicle's progress. Use a loop to simulate each "tick" of the race, where vehicles have the chance to move forward or experience a breakdown. Keep track of each vehicle's distance covered and compare it to the total race distance to determine when a vehicle has won the race. Remember to factor in the possibility of a vehicle breaking down, which could affect its ability to finish.
