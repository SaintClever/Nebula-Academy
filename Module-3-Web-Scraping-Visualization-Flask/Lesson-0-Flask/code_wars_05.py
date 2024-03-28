# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# For example, the score of abad is 8 (1 + 2 + 1 + 4).

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.
import string


def high(x):
    alpha = {}
    total = 0
    word = ""

    for i, char in enumerate(string.ascii_lowercase):
        alpha[char] = i + 1

    for i, char in enumerate(x.split()):
        if sum([alpha[i] for i in char]) > total:
            total = sum([alpha[i] for i in char])
            word = "".join(i for i in char)

    return [word, total]


print(high("man i need a taxi up to ubud"), "taxi")
print(high("what time are we climbing up the volcano"), "volcano")
print(high("take me to semynak"), "semynak")
print(high("aa b"), "aa")
print(high("b aa"), "b")
