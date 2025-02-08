# Function with Variable Number of Arguments (Arbitrary Arguments):

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

product = multiply(2, 3, 4)
print("Product:", product) 

# Output: Product: 24
