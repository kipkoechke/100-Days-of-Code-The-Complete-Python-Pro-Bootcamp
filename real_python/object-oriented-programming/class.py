class Dog:
    # Class Attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


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
