#1. len does not work with number data types
len(12345)

#2. Add "" to turn integer to string
print(len("12345"))

#3. Check the data type of any value or variable in python.
print(type(12345)) #int
print(type(True)) #bool
print(type(123.45)) #float
print(type("12345")) #str

#4. Data type conversion
int("12345") #Converting string to integer

#5. Make this line of code run without errors
print("Number of letters in your name: " + len(input(int("Enter your name"))))

username = input("Enter your name")
namelength = len(username)
print("Number of letters in your name: " + str(namelength)) #Solution
