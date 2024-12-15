print(r'''
*******************************************************************************
                                     /\  /\  /\  /\                                    
                                  //\\/  \/  \/\\//\\                                  
                               /\ ||                || /\                               
                            //\\\\||                ||////\\                           
                         ///\\\\\\||                ||////\\\\\                        
                      ////      \\\\||                ||////      \\\\                 
                   ////          \\\\||                ||////          \\\\            
                 ////              \\\||                ||///             \\\\         
  ,@@@@@@@,                       ||                    ||                       ,@@@@@@@,
 ,,,.   ,@@@@@@/@@,               ||                    ||                .oo8888o.   ,@@,
,&%%&%&&%,@@@@@/@@@@@@,            ||                  ||              ,8888\88/8o ,%&%%&%&&,
,%&\%&&%&&%,@@@\@@@/@@@88          ||                  ||             88888\88888',%&&%&&%%&&,
%&&%&%&/%&&%@@\@@/ /@@@88888       ||                  ||            88888\88888'%&&%/%&&%&%&%
%&&%/ %&%%&&@@\ V /@@' `88\8       ||                  ||             `/88' `88\ %&&%  %&%%&&%
`&%\ ` /%&'    |.|        \ '|8'   ||                  ||    |.|        '|8' ` /%&'    ` /%&
    |o|        | |         | |     ||                  ||    | |         | |        |o|    
    |.|        | |         | |     ||                  ||    | |         | |        |.|    
\/ ._\//_/__/  ,\_//__\\/.  \_//__/_                  __\\_//  ._\//_/__/  ,\_//__/_/  \/  
*******************************************************************************
''')

print("Welcome to Jungle Quest!")
print("Your mission is to find the hidden relic.")

path = input("You stand at the edge of the jungle. Do you take the 'left' or 'right' path?\n").lower()

if path == "right":
    print("You find a river blocking your path.")
    decision = input("Do you 'build' a raft or 'search' for a bridge?\n").lower()

    if decision == "search":
        print("You find a bridge that leads to an ancient temple.")
        relic_room = input("Inside the temple, you find two relic rooms: 'gold' or 'stone'. Which one do you enter?\n").lower()

        if relic_room == "gold":
            print("The room is filled with traps. Game Over.")
        elif relic_room == "stone":
            print("You find the hidden relic. You Win!")
        else:
            print("You wander aimlessly. Game Over.")
    else:
        print("The raft sinks and you get swept away. Game Over.")
else:
    print("You walk into a dense thicket and get lost. Game Over.")
