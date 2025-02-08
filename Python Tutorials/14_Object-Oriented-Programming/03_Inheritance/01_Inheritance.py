# Inheritance: A mechanism to create a new class using details of an existing class without modifying it. The new class is called the derived class, and the one from which it is derived is the base class.


# Parent class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old."

# Child class (inherits from Animal)
class Dog(Animal):
    def speak(self, sound):
        return f"{self.name} says {sound}."

# Creating an object of the derived class
dog = Dog("Buddy", 3)
print(dog.description()) 
# Output: Buddy is 3 years old.
print(dog.speak("Woof Woof")) 
# Output: Buddy says Woof Woof.



#output
# Buddy is 3 years old.
# Buddy says Woof Woof.