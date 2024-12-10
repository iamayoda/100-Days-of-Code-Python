print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0 # Initial bill value

#1. Add bill to change to this value
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5 # Change 1
        print("Child tickets are R5.")
    elif age <= 18:
        bill = 7 # Change 2
        print("Youth tickets are R7.")
    else:
        bill = 12 # Change 3
        print("Adult tickets are R12.")

    #2. Add New If statement to offer photo as part of the ride
    wants_photo = input("Do you want a photo taken? Type Y for Yes and N for NO.")
    if wants_photo == "Y":
        #Add $3 to bill
        print()
        bill = bill + 3 # Or bill += 3

    print(f"Your bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
