# Define the height of the inverted triangle
height=int(input("Enter your height of traingle:"))

# Outer loop for number of rows
for i in range(height, 0, -1):
    # Inner loop for printing stars in each row
    for j in range(i):
        print("*", end=" ")
    print()  # Move to the next line after printing each row




#output
# Enter your height of traingle:5
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
