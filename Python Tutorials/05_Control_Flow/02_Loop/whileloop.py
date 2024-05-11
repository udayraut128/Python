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
