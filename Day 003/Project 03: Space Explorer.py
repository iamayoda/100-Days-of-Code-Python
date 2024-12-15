print(r'''
*******************************************************************************
                                      .        .                                       
                   .          .      .       .       .       .                        
        .                 .           *       .    .      .      *                   
                     .   .    '       .    .        .        .   .                   
    .      .   .      *      .    *         .   '     .      *    .                  
                    *     .      .       .     .    .   *                             
       .     *    .    .       .   *      .        .       *     .                   
                     .   .  *    .      .       .      *   .                          
       .      *        .   .     .         '       .      *     .       *            
             .    *        .  *    .         *     .       .      .                  
           _________     .      *         *    .         *     .                     
       .  /         \         .        .       *         .      .                    
         /   _   _    \    .         *       .    *      .   .     .                 
        /    | |_| |    \      .         *         .        *         .              
       |    _|     |_    |   .      *       *       .    *      .                    
       |   |         |   |   ________   *      .           *       .                 
        \  |    _    |  /   |        |   *    _______  *        .                    
         \ |___|_|___| /    |        |   .   |       |    .     *                    
          \___________/     |________|       |_______|      *                        
             /     \   .        *           .       *                                
            /       \       *         *          .         .                         
           /_________\  .      .         *           .         *                     
*******************************************************************************
''')

print("Welcome, Space Explorer!")
print("Your mission is to retrieve the lost artifact from Planet X.")

choice1 = input("You arrive at Planet X. Do you land on the 'east' or 'west' side of the planet?\n").lower()

if choice1 == "west":
    print("You encounter a dense alien forest.")
    choice2 = input("Do you 'enter' the forest or 'fly' to a new location?\n").lower()

    if choice2 == "enter":
        print("You find a mysterious bunker with two doors.")
        door = input("Do you open the 'metal' door or the 'glass' door?\n").lower()

        if door == "glass":
            print("You find the artifact behind the door. You Win!")
        else:
            print("The bunker collapses. Game Over.")
    else:
        print("A meteor hits your spacecraft. Game Over.")
else:
    print("You land on a volcano and your ship is destroyed. Game Over.")
