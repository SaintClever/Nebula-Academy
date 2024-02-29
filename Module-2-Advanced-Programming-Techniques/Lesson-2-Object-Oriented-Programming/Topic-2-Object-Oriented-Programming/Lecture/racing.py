import random

# ## Vehicle Racing Simulation

# ### Context
# Modern vehicle racing, where different types of vehicles (cars, motorcycles, and trucks) compete in a race.


# ### Problem 1: Define the Base Class
# **Task**: Define a base class `Vehicle` with attributes like `name`, `speed`, and `reliability`. Methods might include `move` (to advance in the race) and `breakdown` (chance of vehicle failure).


# #### Hint
# Start by defining your class with the `__init__` method to initialize the attributes. For the `move` method, consider how you might simulate movement based on the vehicle's speed. The `breakdown` method could randomly affect the vehicle based on its reliability.


class Weapon:
    # def __init__(self): ...

    def missile(self):
        return "Missiles launched: \U0001F680\U0001F680\U0001F680"


class Vechicle:
    def __init__(self, name, speed, reliability):
        self.name = name
        self.speed = speed
        self.reliability = reliability

    def move(self, drivers_speed: int = 0):
        if drivers_speed > 180:
            self.reliability -= 5
            return f"Your {self.name} is going too FAST!!! Your reliability rate is decreasing! It's now {self.reliability}"
        elif drivers_speed < 95:
            self.speed += 10
            return f"Pick up the pace! Now your current speed is now {self.speed}! wow!"
        elif drivers_speed <= 150 and drivers_speed > 100:
            # Using the key words "finish line" to trigger winner
            return f"Your're at the finish line! GO GO!"
        else:
            return f"Are you sleeping at the wheel?!?!"

    def breakdown(self, tune_ups: int = 0):
        if tune_ups < 5:
            self.reliability -= 1
            return f"Your {self.name}'s engine became unreliable... {self.reliability}"
        return f"No worries, your {self.name} seems reilable at {self.reliability}"

    def __repr__(self):
        return f"{self.name}: speed={self.speed}, reliability={self.reliability}"


# ### Problem 2: Create Subclasses
# **Task**: Create subclasses `Car`, `Motorcycle`, and `Truck`, inheriting from `Vehicle`, each with unique characteristics or methods (e.g., different reliability factors or speed adjustments).


# #### Hint
# Use inheritance to create each subclass. Override or add to the base class methods and attributes to reflect the unique properties of each vehicle type. Consider how each vehicle's speed and reliability might differ and implement those differences in your subclasses.


class Car(Vechicle):
    def __init__(self, name, speed, reliability):
        super().__init__(name, speed, reliability)


mazda = Car("\U0001F3CE  Mazda: RX-7", 75, 4.0)
print(mazda.name)
print(mazda.move(180))
print(mazda.breakdown(3))
print()


class Motorcycle(Vechicle):
    def __init__(self, name, speed, reliability):
        super().__init__(name, speed, reliability)

    def move(self, drivers_speed: int = 0):
        if drivers_speed > 160:
            self.reliability -= 10
            return f"Your {self.name} is going too FAST!!! Your reliability rate is decreasing! It's now {self.reliability}"
        elif drivers_speed < 60:
            return "No time to wheelie on the track!"
        else:
            return (
                f"Keep that same steady pace kido. Your current speed is {self.speed}"
            )


yamaha = Motorcycle("\U0001F3CD Yamaha: R1", 112, 4.5)
print(yamaha.name)
print(yamaha.move(6))
print(yamaha.breakdown(4))
print()


class Truck(Vechicle, Weapon):
    def __init__(self, name, speed, reliability):
        super().__init__(name, speed, reliability)
        super().missile()

    def ram(self):
        return "Breaking thru the finish line Elon!"


tesla = Truck("\U0001F6FB  Tesla: Cybertruck", 85, 5.0)
print(tesla.name)
print(tesla.move(120))
print(tesla.breakdown(4))
print(tesla.ram())
print(tesla.missile())
print()


# ### Problem 3: Implement the Race Function
# **Task**: Implement a `race` function where instances of these vehicles compete on a track of a specified distance. The race continues in a loop until one vehicle crosses the finish line, considering potential breakdowns affecting the outcome.


# #### Hint
# Your `race` function will need to keep track of each vehicle's progress. Use a loop to simulate each "tick" of the race, where vehicles have the chance to move forward or experience a breakdown. Keep track of each vehicle's distance covered and compare it to the total race distance to determine when a vehicle has won the race. Remember to factor in the possibility of a vehicle breaking down, which could affect its ability to finish.


print("\t")
print("\U0001F3C1" * 3, " RACERS 3, 2, 1... START!!! ", "\U0001F3C1" * 3, "\n")


def race(racers):
    winners = []

    for racer, status in racers.items():
        print(racer + ": " + status)
        if "finish line" in status:
            winners.append(racer)

    if len(winners) > 1:
        tie = []
        for winner in winners:
            tie.append(winner)
            print(f"\n\U0001F3C1 WINNER {winner} \U0001F3C1!!!")
        return print(f"Tie race ladies and gents! Between: {tie}")
    elif len(winners) == 1:
        return print(f"\n\U0001F3C1 WINNER {winners[0]} \U0001F3C1!!!")
    else:
        print("We have a few more laps. Take a pitstop or pick up the speed!!!\n")
        print("\U0001F3CE \U0001F4A8", (" = " * 25), "\n")
        race(
            {
                "mazda": mazda.move(random.randint(0, 200)),
                "yamaha": yamaha.move(random.randint(0, 200)),
                "tesla": tesla.move(random.randint(0, 200)),
            }
        )


race(
    {
        "mazda": mazda.move(random.randint(0, 200)),
        "yamaha": yamaha.move(random.randint(0, 200)),
        "tesla": tesla.move(random.randint(0, 200)),
    }
)
