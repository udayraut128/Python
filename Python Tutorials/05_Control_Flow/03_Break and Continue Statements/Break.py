# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iterate over the list
for number in numbers:
    # Check if the number is greater than 5
    if number > 5:
        # If it is, print the number and exit the loop
        print("Found a number greater than 5:", number)
        break


#output
# Found a number greater than 5: 6

# another example

# Define a list of numbers
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Iterate over the list
for number in numbers:
    # Check if the number is divisible by 30
    if number % 30 == 0:
        # If it is, print the number and exit the loop
        print("Found a number divisible by 30:", number)
        break


#output
# Found a number divisible by 30: 30