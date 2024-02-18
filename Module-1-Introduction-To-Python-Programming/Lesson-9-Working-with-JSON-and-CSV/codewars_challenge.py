"""
input: list
 - Takes in strings and non negatives:
 
output: list
- No strings / Type must be an integer
"""


def filter_list(l) -> list:
    "return a new list with the strings filtered out"

    # return [i for i in l if type(i) == int]
    return [i for i in l if type(i) == int and i >= 0]


print(filter_list([1, 4, "one", -1]))

"""
input -> string
output -> middle character

if odd: return middle characters
if even: return 2 middle characters
"""


def get_middle(s) -> str:
    midpoint = len(s) // 2

    if len(s) % 2 == 0:
        return s[midpoint - 1 : midpoint + 1]
    return s[midpoint]


print(get_middle("test"), "es")
print(get_middle("testing"), "t")
print(get_middle("middle"), "dd")
print(get_middle("A"), "A")
print(get_middle("of"), "of")
