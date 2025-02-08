# 

# List comprehension
squares = [x * x for x in range(10)]

# Generator expression
squares_gen = (x * x for x in range(10))

# Iterate over the generator
for square in squares_gen:
    print(square)

#output
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81