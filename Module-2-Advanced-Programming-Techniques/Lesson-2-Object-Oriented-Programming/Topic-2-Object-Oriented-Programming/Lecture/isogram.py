# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)


def is_isogram(word: str) -> bool:
    # VERSION 1
    # chars = []

    # for char in word.lower():
    #     if char not in chars:
    #         chars.append(char)

    # if len(chars) == len(word):
    #     return True
    # return False

    # VERSION 2
    # word = " ".join(word.lower()).split()
    # for i in word:
    #     if word.count(i) > 1:
    #         return False
    # return True

    # VERSION 3
    # word = " ".join(word.lower()).split()
    # return False if len([i for i in word if word.count(i) > 1]) > 1 else True

    # VERSION 4
    # word = " ".join(word.lower()).split()
    # return True if [i for i in word if word.count(i) > 1] == [] else False

    # VERSION 5
    return len(word) == len(set(" ".join(word.lower()).split()))


print(is_isogram("Dermatoglyphics"))
# True

print(is_isogram("moose"))
# # False

print(is_isogram("aba"))
# # False
