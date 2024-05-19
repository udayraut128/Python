# Genterator function for genterating Fibonacci numbers:

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Create a generator object
fib_gen = fibonacci(10)

# Iterate over the generator
for num in fib_gen:
    print(num)

#output
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34