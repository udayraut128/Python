# A tuple in Python is an ordered collection of elements, similar to a list but immutable. Tuples are often used for fixed data and can contain elements of different data types. They are defined using parentheses ( ) and can be accessed by index.

# Creating a tuple
my_tuple = (1, 2, 3, "apple", "banana")

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Tuple unpacking
x, y, z, fruit1, fruit2 = my_tuple
print("Unpacked variables:", x, y, z, fruit1, fruit2)

#output
# First element: 1
# Last element: banana
# Unpacked variables: 1 2 3 apple banana