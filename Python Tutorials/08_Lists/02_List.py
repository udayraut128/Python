# Creating a list of strings
fruits = ["apple", "banana", "orange", "grape", "kiwi"]

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Slicing the list
print("Sliced fruits:", fruits[1:4])  # Slicing from index 1 to index 3

# Modifying elements
fruits[2] = "pear"
print("Modified fruits:", fruits)

# Adding elements
fruits.append("melon")
print("After appending:", fruits)

# Removing elements
removed_fruit = fruits.pop(2)
print("Removed fruit:", removed_fruit)
print("After popping:", fruits)

# Finding the index of an element
index = fruits.index("grape")
print("Index of 'grape':", index)

# Checking if an element is in the list
if "kiwi" in fruits:
    print("Yes, 'kiwi' is in the list.")
else:
    print("No, 'kiwi' is not in the list.")

# Reversing the list
fruits.reverse()
print("Reversed list:", fruits)

# Sorting the list
fruits.sort()
print("Sorted list:", fruits)


#output
# First fruit: apple
# Last fruit: kiwi
# Sliced fruits: ['banana', 'orange', 'grape']
# Modified fruits: ['apple', 'banana', 'pear', 'grape', 'kiwi']
# After appending: ['apple', 'banana', 'pear', 'grape', 'kiwi', 'melon']
# Removed fruit: pear
# After popping: ['apple', 'banana', 'grape', 'kiwi', 'melon']
# Index of 'grape': 2
# Yes, 'kiwi' is in the list.
# Reversed list: ['melon', 'kiwi', 'grape', 'banana', 'apple']
# Sorted list: ['apple', 'banana', 'grape', 'kiwi', 'melon']