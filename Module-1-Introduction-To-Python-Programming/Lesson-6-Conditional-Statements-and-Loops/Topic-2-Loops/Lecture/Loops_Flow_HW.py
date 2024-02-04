import random, string

# Question 1: Sum of Positive Numbers
# Write a Python program using a while loop that asks the user to enter numbers repeatedly. The loop should accumulate the sum of positive numbers entered and stop when the user enters a negative number. At the end, print out the sum of all positive numbers entered.

accumulate = 0

while True:
    user_input = float(input("feed me Seymour: "))

    if user_input > -1:
        accumulate += user_input
    else:
        break
print(f"body count accumulated: {accumulate}")


# Question 2: Find the Largest Number
# Using a for loop, write a program that iterates through a list of numbers (you can define the list with some sample numbers) and finds the largest number in the list. Print the largest number at the end.

my_list = random.sample(range(0, 100), 5)

largest_int = 0

for i in my_list:
    if i > largest_int:
        largest_int = i
print(f"Largest int: {largest_int}")

# or


def largest_num(nums):
    return nums, sorted(nums)[-1]


print(largest_num(my_list))


# Question 3: Password Attempt
# Create a program with a while loop that simulates a password entry system. Define a password string at the start of your program. Then, repeatedly ask the user to enter the password. If the user enters the correct password, print a success message and break out of the loop. If the user enters the wrong password, allow them to try again.

while True:
    generated_passowrd = "".join(random.choices(string.ascii_letters, k=3))
    password_attempt = input(f"Remember your NEW password: {generated_passowrd}\n")

    if password_attempt == generated_passowrd:
        print("Access Granted!\n")
        break

    print("Access Denied!\n")


# Question 4: Skip Multiples of Three
# Write a program using a for loop and the continue statement that iterates through numbers 1 to 30 (inclusive). Use the continue statement to skip any number that is a multiple of 3. Print out all numbers that are not multiples of 3.

for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i)


# Question 5: Multiplication Table
# Using nested loops, write a program that prints out the multiplication table for numbers from 1 to 5. The outer loop should iterate through the multiplier, and the inner loop should iterate through the multiplicand. Format the output so that it's easy to read the multiplication table.


for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()
