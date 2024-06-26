# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# For example (Input --> Output):

# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)


def persistence(num):
    # Initialize persistence count
    persistence_count = 0

    # Loop until num becomes a single digit
    while num >= 10:
        # Calculate the product of digits
        product = 1
        for digit in str(num):
            product *= int(digit)

        # Update num with the product and increment persistence count
        num = product
        persistence_count += 1

    return persistence_count
