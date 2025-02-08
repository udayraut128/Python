# A list in Python is an ordered and mutable collection of elements. It can contain elements of different data types, and you can add, remove, and modify elements as needed. Lists are a versatile and commonly used data structure in Python programming.

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print("First element:", my_list[0])

# Modifying elements
my_list[1] = 10
print("Modified list:", my_list)

# Adding elements
my_list.append(6)
print("After appending:", my_list)

# Removing elements
my_list.remove(3)
print("After removing:", my_list)

#output
# First element: 1
# Modified list: [1, 10, 3, 4, 5]
# After appending: [1, 10, 3, 4, 5, 6]
# After removing: [1, 10, 4, 5, 6]