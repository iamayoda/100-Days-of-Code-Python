bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi)) # int Floors the number

#1. Rounding to the nearest whole number
print(round(bmi)) # Becomes 31
print(round(3.14159)) # Becomes 3

#2. Rounding to specific decimal values
print(round(bmi, 4)) # Rounds of to four decimal places
print(round(3.14159, 2)) # Rounds of to two decimal places

#3. Assignment Operators - Accumulate results of a calculation
# +=
# -=
# *=
# /=

score = 0

score += 1 #Adds score
print(score)

score -= 1 # Subtracts score
print(score)

#4. F-Strings - Used to insert a variable or an expression into a string.
score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")
