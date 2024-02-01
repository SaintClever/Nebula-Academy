# Python Lists Practice Assignment
# 1. Create a List
# Task: Create a list named fruits containing the following items: "apple", "banana", "cherry".
fruits = ["apple", "banana", "cherry"]


# Objective: Understand how to create and initialize a list.
# 2. Access List Items
# Task: Print the second item in the fruits list.
print(fruits[1])


# Objective: Learn to access elements in a list using indices.
# 3. Change List Items
# Task: Change the value of the first item in fruits to "orange".
fruits[0] = "orange"
print(fruits)


# Objective: Practice modifying the contents of a list.
# >OPTIONAL, SKIP 4. Loop Through a List
# Task: Write a loop that prints every item in the fruits list.
for i in fruits:
    print(i)


# Objective: Understand how to iterate over list items.
# 5. Check if Item Exists
# Task: Check if "banana" is present in the fruits list and print a message based on the result.
print("banana" in fruits)


# Objective: Learn to check for the existence of an item in a list.
# 6. List Length
# Task: Print the number of items in the fruits list.
print(len(fruits))


# Objective: Use the len() function to determine the size of a list.
# 7. Add Items to a List
# Task: Add "mango" to the end of the fruits list.
fruits.append("mango")
print(fruits)


# Objective: Practice using list methods like append().
# 8. Remove Items from a List
# Task: Remove "banana" from the fruits list.
fruits.remove("banana")
print(fruits)


# Objective: Learn to remove items from a list.
# 9. Copy a List
# Task: Create a new list named more_fruits that is a copy of the fruits list.
solo_fruit = fruits.pop(1)
print(solo_fruit)
print(fruits)


# Objective: Understand different ways to copy a list.
# 10. Join Two Lists
# Task: Create another list named vegetables containing "carrot", "potato", "cucumber". Combine it with the fruits list to create a mixed list.
veggies = ["carrot", "potato", "cucumber"]
print(fruits)
print(fruits + veggies)
fruits.extend(veggies)


# Objective: Learn to join or concatenate two lists.
# 11. Find the Index of an Item
# Task: Find and print the index of "cherry" in the fruits list.
fruits.insert(len(fruits), "cherry")
print(fruits)


# Objective: Use the index() method to find the position of an item in a list.
# 12. Sorting a List
# Task: Sort the fruits list in alphabetical order.
print(fruits.index("carrot"))


# Objective: Practice sorting lists using the sort() method.
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)
