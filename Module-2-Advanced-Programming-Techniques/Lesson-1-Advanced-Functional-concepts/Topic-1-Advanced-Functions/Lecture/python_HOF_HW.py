import functools

# ### Homework:
# 1. **Enhanced Temperature Converter:** Write a program that uses `map` to convert a list of temperatures in Fahrenheit to Celsius.
fahrenheit: list[int] = [85, 45, 65, 90, 32, 75, 40, 65, 55, 70, 50, 95, 80]


def fahrenheit_to_celsius(f: list[int]) -> list:
    return float(f"{(f - 32) * 5 / 9:.2f}")


print(list(map(fahrenheit_to_celsius, fahrenheit)))
print(list(map(lambda f: float(f"{(f - 32) * 5 / 9:.2f}"), fahrenheit)))


# 2. **Summation Function:** Implement a function using `reduce` to calculate the sum of a list `[3, 5, 2, 4, 6, 8]`.
numbers: list[int] = [3, 5, 2, 4, 6, 8]


def summation(x: int, y: int) -> list:
    return x + y


print(functools.reduce(summation, numbers))
print(functools.reduce(lambda x, y: x + y, numbers))


# 3. **String Processing Enhanced:** **CHALLENGE:** Use `filter` and a custom function to keep only consonants from a given string, effectively removing vowels and spaces.
vowels = "aeiou "
sentence = "Hello World!"


def constants(char: str) -> list:
    # if string not in vowels:
    #     return string

    return char if char not in vowels else False


print("".join(list(filter(constants, sentence))))
print(
    "".join(list(filter(lambda char: char if char not in vowels else False, sentence)))
)
