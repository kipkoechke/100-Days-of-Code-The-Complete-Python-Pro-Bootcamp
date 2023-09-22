print("Welcome to the rollercoaster!")
height = int(input("What is your height: "))
bill = 0

if height > 120:
    print("Wow! You can ride.")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age < 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        print("Everything is going to be OK! Have a free ride with us.")
    else:
        bill = 12
        print("Adult tickets are $12")

    want_photo = input("Want to take a photo? Y or N.")
    if want_photo == "Y":
        bill += 3
    print(f"Total bill is ${bill}")
else:
    print("Sorry! You can't ride.")
