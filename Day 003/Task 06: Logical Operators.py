You can combine different conditions using logical operators.

A and B #Both conditions need to be true
C or D #Only one condition needs to be true
not E #The condition must be false


#EXAMPLE 1 - Less/more than
a = 12

a > 15
False

a > 10
True


#EXAMPLE 2 - AND operation
#True and True = True
#True and False = False
#False and True = False
#Fasle and False = False

a > 10 and a < 13 # Both condtions are true
True

a > 15 and a < 13 # The first condition is true and the second one is false.
False


#EXAMPLE 3 - OR operation
#True or True = True
#True or False = True
#False or True = True
#Fasle or False = False

a > 10 and a < 13 # Both condtions are true
True

a > 15 and a < 13 # The first condition is true and the second one is false.
True


#EXAMPLE 4 - NOT operation
#Not True = False
#Not False = True
