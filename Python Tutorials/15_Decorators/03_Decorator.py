# Logging Decorator

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logging_decorator
def add(a, b):
    return a + b

add(5, 3)

# output
# Calling add with arguments (5, 3) and keyword arguments {}
# add returned 8