# Define the height of the triangle
height=int(input("Enter your height of traingle:"))

# Outer loop for number of rows
for i in range(1, height + 1):
    # Inner loop for printing  number  in each row
    for j in range(i):
        print(j+1, end=" ")
    print()  # Move to the next line after printing each row

#output
# 1
# 1 2
# 1 2 3
# 1 2 3 4