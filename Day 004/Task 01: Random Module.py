#1. Random module in Python
import random #imports random module from python
random_integer = random.randint(1, 10)
print(random_integer)

#2. Created my own module
import my_module
print(my_module.my_favourite_colour)

#3. Random floating point between 0 and 1

#3.1 Method 1
rand_num_0_to_1 = random.random()
print(rand_num_0_to_1)

#3.2 Method 2
random_float = random.uniform(1, 10)
print(random_float)
