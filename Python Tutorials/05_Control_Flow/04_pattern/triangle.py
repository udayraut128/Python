# Define the height of the triangle
height=int(input("Enter your height of traingle:"))

# Outer loop for number of rows
for i in range(1, height + 1):
    # Inner loop for printing stars in each row
    for j in range(i):
        print("*", end=" ")
    print()  # Move to the next line after printing each row


#output
# Enter your height of traingle:4
# *
# * *
# * * *
# * * * *