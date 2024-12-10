print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    # Nesting -  Putting if/else or elif statements inside other if/else statements
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay R5")
    elif age <= 18: # Older than 12 but younger than 189
        print("Please pay R7")
    else:
        print("Please pay R12")
else:
    print("Sorry you have to grow taller before you can ride.")
  
