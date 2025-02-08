class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        # Handle exceptions if necessary
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        # Return True to suppress the exception, False to propagate it
        return False

with MyContextManager() as cm:
    print("Inside the context")


#output
# Entering the context
# Inside the context
# Exiting the context