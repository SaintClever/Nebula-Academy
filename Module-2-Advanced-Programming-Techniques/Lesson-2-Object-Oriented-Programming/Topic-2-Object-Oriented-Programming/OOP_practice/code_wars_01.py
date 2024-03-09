# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.


def spin_words(sentence) -> str:
    # new_sentence = ""

    # for word in sentence.split():
    #     if len(word) >= 5:
    #         new_sentence += word[::-1] + " "
    #     else:
    #         new_sentence += word + " "

    # return new_sentence.strip()

    return " ".join(word[::-1] if len(word) >= 5 else word for word in sentence.split())


print(spin_words("Hey fellow warriors"))  # --> "Hey wollef sroirraw"
print(spin_words("This is a test"))  # --> "This is a test"
print(spin_words("This is another test"))  # --> "This is rehtona test"
