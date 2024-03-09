# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into '#'.

# Examples (input --> output):


def maskify(cc) -> str:
    return (len(cc) - 4) * "#" + cc[len(cc) - 4 :] if len(cc) > 3 else cc


print(maskify("4556364607935616"))  # --> "############5616"
print(maskify("64607935616"))  # --> "#######5616"
print(maskify("1"))  # --> "1"
print(maskify(""))  # --> ""

# "What was the name of your first pet?"
print(maskify("Skippy"))  # --> "##ippy"
print(
    maskify("Nananananananananananananananana Batman!")
)  # --> "####################################man!"
