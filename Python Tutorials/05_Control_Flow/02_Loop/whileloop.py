# 1 example
# Initialize a counter
count = 0

# Loop until the counter reaches 5
while count < 5:
    print(count)
    count += 1

#output
# 0
# 1
# 2
# 3
# 4


# 2 example
# Ask the user to guess a number
secret_number = 7
guess = int(input("Guess the secret number (between 1 and 10): "))

# Keep asking until the correct number is guessed
while guess != secret_number:
    print("Wrong guess!")
    guess = int(input("Try again: "))

print("Congratulations! You guessed the secret number:", secret_number)


#output
# Guess the secret number (between 1 and 10): 4
# Wrong guess!
# Try again:


#3 example of star pattern

# Define the height of the triangle
height = 5

# Initialize variables
i = 1

# Outer loop for number of rows
while i <= height:
    # Inner loop for printing stars in each row
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()  # Move to the next line after printing each row
    i += 1

# * 
# * * 
# * * * 
# * * * * 
# * * * * *
