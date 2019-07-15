#imports the ability to get a random number (we will learn more about this later!)
from random import *
#Generates a random integer.
aRandomNumber = randint(1, 20)
guesses = 0
# For Testing: print(aRandomNumber)
while guesses < 3:
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    guesses = guesses + 1
    if not guess.isnumeric(): # checks if a string is only digits 0 to 9
        print ("That's not a positive whole number, try again!")
    else:
        guess = int(guess) # converts a string to an integer
        
    if guess == aRandomNumber:
        print ("Congrats, You got it!")
        break
    elif (guess is > aRandomNumber):
        print ("Try again that's too high")
    else:
        print ("Try again that's too low")
    guesses = guesses + 1
