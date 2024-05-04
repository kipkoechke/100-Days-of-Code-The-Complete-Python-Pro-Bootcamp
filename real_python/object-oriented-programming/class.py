class Dog:
    # Class Attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        """
        Initializes a new instance of the class with the given name and age.

        Parameters:
            name (str): The name of the object.
            age (int): The age of the object.
        """
        self.name = name
        self.age = age

    # Instance method
    def __str__(self):
        """
        Returns a string representation of the object.

        This method is part of the special method overloading in Python. It is called when the `str()` function is used on an instance of the class.

        Returns:
            str: A string representation of the object, showing the name and age of the dog.
        """
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        """
        A method that returns a string indicating the dog's name and the sound it makes.

        Parameters:
            self: The instance of the class.
            sound (str): The sound the dog makes.

        Returns:
            str: A string indicating the name of the dog and the sound it makes.
        """
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

    def drive(self, miles):
        self.mileage = self.mileage + miles


blue = Car("blue", 20000)
red = Car("red", 30000)
print(blue)
print(red)

blue_car = Car("blue", 0)
blue_car.drive(100)
print(blue_car)
