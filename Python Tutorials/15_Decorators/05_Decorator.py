# Changing Decorators

def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1")
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2")
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()


#output
# Decorator 1
# Decorator 2
# Hello!
