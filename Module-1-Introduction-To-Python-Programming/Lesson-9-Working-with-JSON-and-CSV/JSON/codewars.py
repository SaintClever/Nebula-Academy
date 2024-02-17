"""
input -> str
output -> int
consider "a, e, i, o, u", lowercase and /or spaces
"""

# def get_count(sentence: str) -> int:
#     vowels: list = ["a", "e", "i", "o", "u"]
#     count = 0

#     for letter in sentence:
#         if letter in vowels:
#             count += 1

#     return count


# print(get_count("abracadabra"))


def get_count(sentence: str) -> int:
    vowels: str = "aeiou"
    return len("".join(letter for letter in sentence if letter in vowels))


print(get_count("abracadabra"))

"""
input -> str
output -> str
remove vowels
"""


# def disemvowel(string_: str) -> str:
#     vowels: list = ["a", "e", "i", "o", "u"]
#     vowels_upper_case: list = " ".join(vowels).upper().split()
#     sentence: str = ""

#     for letter in string_:
#         if letter in vowels + vowels_upper_case:
#             list(string_).remove(letter)
#         else:
#             sentence += letter

#     return sentence


# print(disemvowel("This website is for losers LOL!"))
# # "Ths wbst s fr lsrs LL!"


def disemvowel(string_: str) -> str:
    vowels: str = "aeiouAEIOU"
    return "".join(letter for letter in string_ if letter not in vowels)


print(disemvowel("This website is for losers LOL!"))
# "Ths wbst s fr lsrs LL!"
