import random

print("Welcome to the Dice Rolling game!")

# Simulate rolling a die with random.uniform
dice_roll = int(random.uniform(1, 7))  # Generates a float, then converts to int for dice

# User guesses if the roll is low or high
user_guess = input("Will the dice roll be Low (1-3) or High (4-6)? Enter 'Low' or 'High': ").capitalize()

if user_guess not in ["Low", "High"]:
    print("Invalid input! You lose.")
else:
    print(f"The dice rolled: {dice_roll}")
    if (user_guess == "Low" and 1 <= dice_roll <= 3) or (user_guess == "High" and 4 <= dice_roll <= 6):
        print("Correct! You win!")
    else:
        print("Wrong! You lose!")
