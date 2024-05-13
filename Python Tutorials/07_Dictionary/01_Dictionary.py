# A dictionary in Python is a collection of data that stores key-value pairs. Keys are unique and used to access corresponding values. Dictionaries are mutable, unordered, and support flexible data types. They offer efficient lookup using hash tables.

# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: New York

# Modifying values
my_dict["age"] = 35
print(my_dict["age"])  # Output: 35

# Adding new key-value pairs
my_dict["gender"] = "Male"
print(my_dict["gender"])  # Output: Male

# Deleting key-value pairs
del my_dict["city"]
print(my_dict)  # Output: {'name': 'John', 'age': 35, 'gender': 'Male'}

# Iterating over keys
for key in my_dict:
    print(key, my_dict[key])


#output
# John
# 30
# New York
# 35
# Male
# {'name': 'John', 'age': 35, 'gender': 'Male'}
# name John
# age 35
# gender Male