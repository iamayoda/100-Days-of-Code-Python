#1. [] is used to create lists

#1.1 Fruit List
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[1]) #Prints "Apple"

#1.2 American States in the order they joined the Union
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[37]) #Prints "Colorado"

#2. Negative indices
print(states_of_america[-1]) #Prints "Hawaii"
print(fruits[-2])

#3. Modifying items on the list
states_of_america[1] = "Pencilvania"
print(states_of_america)

fruits[0] = "Orange"
print(fruits)

#4. Adding Items
states_of_america.append("Duduland")
print(states_of_america)

fruits.append("kiwi")
print(fruits)
