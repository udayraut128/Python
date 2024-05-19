# A generator function is defined like a normal function, but instead of using the return statement to return a value, it uses yield to yield a value and suspend its state. When the generator is called, it returns a generator object which can be iterated over.

def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = simple_generator()

# Iterate over the generator
for value in gen:
    print(value)


#output
# 1
# 2
# 3