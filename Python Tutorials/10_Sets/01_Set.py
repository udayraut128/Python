# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)
my_set.add(3)  # Adding a duplicate element (ignored)
print("Set:", my_set)

# Removing elements
my_set.remove(2)
print("Set after removing element 2:", my_set)

# Checking membership
if 4 in my_set:
    print("Yes, 4 is in the set.")
else:
    print("No, 4 is not in the set.")

#output
# Set: {1, 2, 3, 4, 5, 6}
# Set after removing element 2: {1, 3, 4, 5, 6}
# Yes, 4 is in the set.
