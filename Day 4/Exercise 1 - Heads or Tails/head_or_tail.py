# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇
import random

random_choosen_int = random.randint(0, 1)
if random_choosen_int == 1:
    print("Heads")
else:
    print("Tails")
