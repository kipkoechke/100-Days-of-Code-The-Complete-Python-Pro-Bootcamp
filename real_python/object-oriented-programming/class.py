class Dog:
    # Class Attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

print(buddy.name)
print(buddy.age)
print("********************************")
print(miles.name)
print(miles.age)
print("********************************")
print(f"Class Attribute is: {buddy.species}")
print("********************************")
buddy.age = 10
miles.species = "Felis silvestris"
print(buddy.age)
print(miles.species)
print("********************************")
print(miles.speak("Woof Woof"))
print(miles.speak("Bow Bow"))
print(miles)


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage:,} miles"


blue = Car("blue", 20000)
red = Car("red", 30000)
print(blue)
print(red)
