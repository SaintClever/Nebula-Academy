def is_even(x):
    # print("Current iteration:", x)
    # print("Is even:", x % 2 == 0)
    return x % 2 == 0  # returns a boolean True or False
    # if True, filter adds to new list
    # if False, filter does not add to new list


numbers = [1, 2, 3, 4, 5]
even_numbers_func = list(filter(is_even, numbers))

# or

even_numbers_lambda_func = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers_func, even_numbers_func)  # Output: [2, 4]

# map(callback_fucntion, list)
# lamda x : x * 3
