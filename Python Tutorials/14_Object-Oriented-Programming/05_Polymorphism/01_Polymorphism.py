# Polymorphism: The ability to present the same interface for different underlying forms (data types).



class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

# Polymorphism example
def animal_sound(animal):
    print(animal.speak())

cat = Cat()
dog = Dog()

animal_sound(cat)  
# Output: Meow
animal_sound(dog)  
# Output: Woof


#output
# Meow
# Woof