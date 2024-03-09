# This time no story, no theory. The examples below show you how to write function accum:


def accum(string: str) -> str:
    return "-".join((char * (i + 1)) for i, char in enumerate(string)).title()


print(accum("abcd"))  # "A-Bb-Ccc-Dddd"
print(accum("RqaEzty"))  # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
print(accum("cwAt"))  # "C-Ww-Aaa-Tttt"


abc = ("a", "b", "c")
alpha = list(enumerate(abc))
print(alpha)
