#  a decorator is a powerful tool that allows you to modify the behavior of a function or a method without changing its code. Decorators are a form of metaprogramming because they work with functions as arguments to other functions. They are commonly used for logging, enforcing access control and authentication, instrumentation and timing, and caching.




def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# output

# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.