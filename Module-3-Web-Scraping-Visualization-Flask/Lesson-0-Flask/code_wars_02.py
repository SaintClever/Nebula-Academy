# DESCRIPTION:
# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples


def duplicate_encode(word) -> str:
    # output = ""
    # word = word.casefold()

    # for i in word:
    #     if word.casefold().count(i) > 1:
    #         output += ")"
    #     else:
    #         output += "("

    # return output

    # return "".join(
    #     [")" if word.casefold().count(i) > 1 else "(" for i in word.casefold()]
    # )

    word = word.casefold()
    return "".join([")" if word.count(i) > 1 else "(" for i in word])


print(duplicate_encode("din"), "(((")
print(duplicate_encode("recede"), "()()()")
print(duplicate_encode("Success"), ")())())", "should ignore case")
print(duplicate_encode("(( @"), "))((")
