def sum_two_smallest_numbers(numbers: list) -> int:
    # num1, num2 = sorted(numbers)[:2]
    # return num1 + num2

    return sum(sorted(numbers)[:2])


print(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
print(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)


def friend(x) -> list:
    return [name for name in x if len(name) == 4]


print(
    friend(
        [
            "Ryan",
            "Kieran",
            "Mark",
        ]
    ),
    ["Ryan", "Mark"],
)
print(friend(["Ryan", "Jimmy", "abc", "d", "Cool Man"]), ["Ryan"])
print(
    friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]),
    ["Jimm", "Cari", "aret"],
)
