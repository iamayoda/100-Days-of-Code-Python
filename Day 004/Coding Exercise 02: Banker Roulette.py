friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random

#1. Figure out how to pick a random name from the list of friends.

#1.1 MY SOLUTION
person_to_pay = random.randint(0,4)
print(friends[person_to_pay])

#1.2 ALTERNATIVE
person_to_pay = random.choice(friends)
print(person_to_pay)
