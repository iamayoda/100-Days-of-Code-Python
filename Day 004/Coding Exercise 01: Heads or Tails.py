import random

#Create a heads or tales games
#MY CODE
random_integer = random.randint(1, 20)
coin_side = (random_integer % 2)
print(random_integer)
print(coin_side)

if coin_side == 0:
    print("Heads!")
else:
    print("Tales!")

#ALTERNATIVE
random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
