
# Writing data to a file
with open('example.txt', 'w') as file:
    file.write('Line 1: This is the first line.\n')
    file.write('Line 2: This is the second line.\n')
    file.write('Line 3: This is the third line.\n')

# Appending data to the same file
with open('example.txt', 'a') as file:
    file.write('Line 4: This is the fourth line.\n')

# Reading data from the file
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # Strip newline character and print each line


#output
# Line 1: This is the first line.
# Line 2: This is the second line.
# Line 3: This is the third line.
# Line 4: This is the fourth line.