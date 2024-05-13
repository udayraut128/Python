# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)
my_set.add(3)  # Adding a duplicate element (ignored)
print("After adding elements:", my_set)

# Removing elements
my_set.remove(2)
print("After removing element 2:", my_set)

# Checking membership
if 4 in my_set:
    print("Yes, 4 is in the set.")
else:
    print("No, 4 is not in the set.")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# Symmetric difference
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)


#output
# After adding elements: {1, 2, 3, 4, 5, 6}
# After removing element 2: {1, 3, 4, 5, 6}        
# Yes, 4 is in the set.
# Union: {1, 2, 3, 4, 5, 6}
# Intersection: {3, 4}
# Difference (set1 - set2): {1, 2}
# Symmetric Difference: {1, 2, 5, 6}