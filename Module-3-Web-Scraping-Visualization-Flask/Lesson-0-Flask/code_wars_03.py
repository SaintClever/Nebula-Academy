# DESCRIPTION:
# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:


def unique_in_order(sequence):
    if sequence:
        output = [sequence[0]]

        for i in sequence:
            if output[len(output) - 1] != i:
                output.append(i)

        return output
    return []

    # if sequence:
    #     output = [None]
    #     for i in sequence:
    #         if output[len(output) - 1] != i:
    #             output.append(i)

    #     return output[1:]
    # return []

    # output = []

    # for i in range(len(sequence)):
    #     if i == 0 or sequence[i] != sequence[i - 1]:
    #         output.append(sequence[i])

    # return output


print(unique_in_order("AAAABBBCCDAABBB"))
print(["A", "B", "C", "D", "A", "B"])
print()

print(unique_in_order("ABBCcAD"))
print(["A", "B", "C", "c", "A", "D"])
print()

print(unique_in_order([1, 2, 2, 3, 3]))
print([1, 2, 3])
print()

print(unique_in_order((1, 2, 2, 3, 3)))
print([1, 2, 3])
print()

print(unique_in_order(""), [])
print(unique_in_order([]), [])
print(unique_in_order(()), [])
print()

print(unique_in_order("A"), ["A"])
print(unique_in_order(["A"]), ["A"])
print(unique_in_order(("A",)), ["A"])
print()

print(unique_in_order("AA"), ["A"])
print(unique_in_order("AAAABBBCCDAABBB"), ["A", "B", "C", "D", "A", "B"])
print()

print(unique_in_order("ABBCcA"), ["A", "B", "C", "c", "A"])
print()

print(unique_in_order([1, 2, 3, 3, -1]), [1, 2, 3, -1])
print(unique_in_order(["a", "b", "b", "a"]), ["a", "b", "a"])
