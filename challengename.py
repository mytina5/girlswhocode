#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
List1 = ["Burger", "Swift", "Clean", "TableTop", "Timeless", "Yummy", "Delicious", "Tasty", "Raritan",]
List2 = ["Eatery", "Dining", "Eats", "House", "Shack", "Diner", "Hub", "Brewery", "Express"]
#Generates a random integer.
randomfirst = randint(0, len(List1)-1)
randomsecond = randint(0, len(List2)-1)

print (List1[randomfirst] +" "+ List2[randomsecond])
