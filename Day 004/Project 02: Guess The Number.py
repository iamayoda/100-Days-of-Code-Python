import random

print("Welcome to the Guess the Number game!")

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Loop until the user guesses the correct number
while True:
    user_guess = int(input("Guess a number between 1 and 100: "))

    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number!")
        break
