# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
number_items = len(names) - 1
random_choice = random.randint(0, number_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today!")
