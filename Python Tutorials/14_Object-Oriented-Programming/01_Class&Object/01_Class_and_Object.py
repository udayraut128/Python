# Class: A blueprint for creating objects. A class defines a set of attributes and methods that the created objects will have.

# Object: An instance of a class. It is a concrete entity based on the class blueprint.



class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}."

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

# Accessing class attributes
print(dog1.species) 
# Output: Canis familiaris

# Accessing instance attributes
print(dog1.name) 
# Output: Buddy
print(dog2.name) 
# Output: Lucy

# Calling instance methods
print(dog1.description())  
# Output: Buddy is 3 years old.
print(dog2.speak("Woof Woof"))  
# Output: Lucy says Woof Woof.

#output
# Canis familiaris
# Buddy
# Lucy
# Buddy is 3 years old.
# Lucy says Woof Woof