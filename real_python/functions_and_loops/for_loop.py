for letter in "Python":
    print(letter)

print("")
print("================")
print("")

for n in range(10, 20):
    print(n * n)

print("")
print("================")
print("")

amount = float(input("Enter an amount: "))

for num_people in range(2, 6):
    print(f"{num_people} people: ${amount / num_people:.2f} each")
