class Car:
    # Initializer / Constructor
    def __init__(self, make, model, year):
        self.make = make    # Attribute 1
        self.model = model  # Attribute 2
        self.year = year    # Attribute 3

    # Method 1: Display car details
    def display_details(self):
        return f"{self.year} {self.make} {self.model}"

    # Method 2: Start the car
    def start(self):
        return f"The {self.model} is starting."

    # Method 3: Accelerate the car
    def accelerate(self):
        return f"The {self.model} is accelerating."

    # Method 4: Stop the car
    def stop(self):
        return f"The {self.model} is stopping."

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing attributes
print(f"Make: {my_car.make}")     # Output: Make: Toyota
print(f"Model: {my_car.model}")   # Output: Model: Corolla
print(f"Year: {my_car.year}")     # Output: Year: 2020

# Calling methods
print(my_car.display_details())  # Output: 2020 Toyota Corolla
print(my_car.start())            # Output: The Corolla is starting.
print(my_car.accelerate())       # Output: The Corolla is accelerating.
print(my_car.stop())             # Output: The Corolla is stopping.




# Attributes:

# make: The make (manufacturer) of the car.
# model: The model of the car.
# year: The manufacturing year of the car.


# Methods:

# display_details(): Returns a string displaying the car's details.
# start(): Returns a string indicating the car is starting.
# accelerate(): Returns a string indicating the car is accelerating.
# stop(): Returns a string indicating the car is stopping.