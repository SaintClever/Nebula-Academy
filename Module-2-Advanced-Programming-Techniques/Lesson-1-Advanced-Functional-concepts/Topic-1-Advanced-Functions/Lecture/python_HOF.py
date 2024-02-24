import functools

### Class Exercises:


# 1. **Transforming Data: MAP**
#    - Convert this list of temperatures from Celsius to Fahrenheit: `32, -17, 40, 5, -7, 20, -1, 16, -16, 4` Celsius.

celsius = [32, -17, 40, 5, -7, 20, -1, 16, -16, 4]


def celsius_to_fahrenheit(c):
    fahrenheit = (c * 9 / 5) + 32
    return float(f"{fahrenheit:.2f}")


fahrenheit_func = print(list(map(celsius_to_fahrenheit, celsius)))
fahrenheit_lambda = print(list(map(lambda c: (c * 9 // 5) + 32, celsius)))


# 2. **Filtering Data: FILTER**
#    - Extract names starting with the letter "E" from this updated list: `Emma, Evan, Ella, Alice, Bob, Charlie, Diana, Fiona, George, Hannah`.

names = [
    "Emma",
    "Evan",
    "Ella",
    "Alice",
    "Bob",
    "Charlie",
    "Diana",
    "Fiona",
    "George",
    "Hannah",
]


def start_with_e(name):
    # if name[0].lower() == "e":
    #     return name

    return name if name[0].lower() == "e" else False


print(list(filter(start_with_e, names)))
print(list(filter(lambda name: name[0].lower() == "e", names)))


# 3. **Aggregating Data: REDUCE**
#    - Calculate the total of this list of numbers: `33, 87, 58, 46, 31, 29, 21, 40, 86, 47`.

numbers = [33, 87, 58, 46, 31, 29, 21, 40, 86, 47]


def total_of_numbers(x, y):
    return x + y


print(functools.reduce(total_of_numbers, numbers))
print(functools.reduce(lambda x, y: x + y, numbers))


# ### Practice Exercises:

# 1. **List Transformation:** Use `map` to create a list of the lengths of each word in the list `["Python", "Programming", "Is", "Fun"]`.

words = ["Python", "Programming", "Is", "Fun"]


def word_length(words):
    return len(words)


print(list(map(word_length, words)))
print(list(map(lambda words: len(words), words)))


# 2. **Filtering Values:** Use `filter` to get all the prime numbers from a list `[2, 3, 4, 5, 6, 7, 8, 9, 10]`.
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]


def prime_numbers(num):
    # if num < 2:
    #     return False
    # for i in range(2, int(num**0.5) + 1):
    #     if num % i == 0:
    #         return False
    # return True

    return all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and num > 1


print(list(filter(prime_numbers, numbers)))
print(
    list(
        filter(
            lambda num: all(num % i != 0 for i in range(2, int(num**0.5) + 1))
            and num > 1,
            numbers,
        )
    )
)


# 3. **Data Aggregation:** Use `reduce` to concatenate a list of strings into a single sentence: `["Functional", "programming", "in", "Python"]`.
words = ["Functional", "programming", "in", "Python"]


def single_sentence(x, y):
    return x + " " + y


print(functools.reduce(single_sentence, words))
print(functools.reduce(lambda x, y: x + " " + y, words))
