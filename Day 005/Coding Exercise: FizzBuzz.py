#You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game.

#MY ATTEMPT
for number in range (1, 100):
    if number % 3 == 0:
        print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        if number % 5 * 3 == 0:
            print("FizzBuzz")
    print(number)


#SOLUTION
# Create a loop with For and Range to go from 1 to 100.
for number in range(1, 101):
  # First check if the number is divisible by both 3 and 5.
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
 
  # Then check if the number is only divisible by 3
  elif number % 3 == 0:
    print("Fizz")
 
  # Finally check if the number is only divisible by 5
  elif number % 5 == 0:
    print("Buzz")
 
  # If it's not divisible by either of those numbers, just print the number
  else:
    print(number)
