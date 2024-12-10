#1. MODULO OPERATOR - Gives you the remainder of a division.

6 % 2 # will be 0
6 % 5 # will be 1
6 % 4 # will be 2

#2. EXERCISE 1
print(10 % 3) # will be 1


#3. EXERCISE 2 - Check if the number in he input area is ODD or EVEN
in_value = int(input("Check if the number is ODD or EVEN."))
final_value = (in_value % 2)

if final_value == 0:
    print("This number is EVEN!")
else:
    print("This number is ODD!")
  
