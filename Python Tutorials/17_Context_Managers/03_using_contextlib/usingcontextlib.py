from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entering the context")
    try:
        yield
        print("Inside the context")
    finally:
        print("Exiting the context")

with my_context_manager():
    print("Doing work inside the context")


#output
# Entering the context
# Doing work inside the context
# Inside the context
# Exiting the context