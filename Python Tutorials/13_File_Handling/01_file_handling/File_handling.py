# File handling in Python refers to the manipulation of files on the filesystem using Python programming language. It allows you to read data from files, write data to files, and perform various operations such as creating, deleting, and modifying files.

# Opening a file in write mode ('w')
file = open('example.txt', 'w')

# Writing data to the file
file.write('Hello, World!\n')
file.write('This is a sample file.\n')

# Closing the file
file.close()

# Opening the file in read mode ('r')
file = open('example.txt', 'r')

# Reading data from the file
content = file.read()
print(content)

# Closing the file
file.close()
