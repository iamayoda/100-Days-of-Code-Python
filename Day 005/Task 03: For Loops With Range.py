#1. Range Function with For Loops
for number in range(1, 10): #Does not include the last number "10"
    print(number)

#2. Specify step of the range
for number in range(1, 11, 2): #Does not include the last number "11" and step is 2
    print(number)

#3. Add numbers from 1 to 100
total = 0
for number in range(1, 101): #Does not include the last number "101"
    total += number
print(total)
