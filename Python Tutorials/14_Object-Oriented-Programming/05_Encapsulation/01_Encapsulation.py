# Encapsulation: The bundling of data with the methods that operate on that data. It restricts direct access to some of the object's components.

class Person:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self.__age = age   # Private attribute

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive!")

person = Person("Alice", 30)
print(person.get_age()) 
# Output: 30
person.set_age(35)
print(person.get_age())  
# Output: 35



#output
# 30
# 35