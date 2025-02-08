# Define a list of numbers
#even number
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iterate over the list
for number in numbers:
    # Check if the number is divisible by 2
    if number % 2 != 0:
        # If it's not divisible by 2, skip to the next iteration
        continue
    # If it's divisible by 2, print the number
    print("Found an even number:", number)


#output
# Found an even number: 2
# Found an even number: 4
# Found an even number: 6
# Found an even number: 8
# Found an even number: 10

#second example
# Odd number

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iterate over the list
for number in numbers:
    # Check if the number is divisible by 2
    if number % 2 == 0:
        # If it's not divisible by 2, skip to the next iteration
        continue
    # If it's divisible by 2, print the number
    print("Found an even number:", number)


#output
# Found an even number: 1
# Found an even number: 3
# Found an even number: 5
# Found an even number: 7
# Found an even number: 9