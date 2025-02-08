# 1 exmaple

# Iterate over a range of numbers
for i in range(1, 6):
    print(i)

# Output
# 1
# 2
# 3
# 4
# 5

# 2 example

# Define the number to calculate factorial for
number = 5

# Initialize factorial to 1
factorial = 1

# Calculate factorial using a for loop
for i in range(1, number + 1):
    factorial *= i

# Print the factorial
print("Factorial of", number, "is", factorial)


# output
# Factorial of 5 is 120


# 2 example of star pattern

# Define the height of the triangle
height = 5

# Outer loop for number of rows
for i in range(1, height + 1):
    # Inner loop for printing stars in each row
    for j in range(i):
        print("*", end=" ")
    print()  # Move to the next line after printing each row


# * 
# * * 
# * * * 
# * * * * 
# * * * * *
