#MY  ATTEMPT
print("World Rock Paper Scissors Championships")

hands = [rock, paper, scissors]
my_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(hands[my_hand])

comp_hand = random.randint(0,2)
print(hands[comp_hand])

my_win_1 = (my_hand == 0 and comp_hand == 2)
comp_win_1 = (my_hand == 2 and comp_hand == 0)
my_win_2 = (my_hand == 1 and comp_hand == 0)
comp_win_2 = (my_hand == 0 and comp_hand == 1)
my_win_3 = (my_hand == 2 and comp_hand == 1)
comp_win_3 = (my_hand == 1 and comp_hand == 2)

if my_win_1:
    print("You win!")
    if comp_win_1:
        print("You lose!")
    elif my_win_2:
        print("You win!")
    elif comp_win_2:
        print("You lose!")
    elif my_win_3:
        print("You win!")
    elif comp_win_3:
        print("You lose!")
else:
    print("It's a draw")


# SOLUTION
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
