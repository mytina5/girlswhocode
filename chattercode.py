# --- Define your functions below! ---
from random import *

def intro():
    print ("Hi! I'm chatterbot.")
    name = input("What's your name? ")
    process_name(name)

def process_input(answer):
    print ("That's my favorite number!")
    #elif answer == :
        #say_default()

def input_process(response):
    if response == "yes":
        print("Hooray!")
#from random import *
#Generates a random integer.
        aRandomNumber = randint(1, 20)
        guesses = 0
        while guesses < 3:
            guess = input("Guess a number between 1 and 20 (inclusive): ")
            if not guess.isnumeric(): # checks if a string is only digits 0 to 9
                print ("That's not a positive whole number, try again!")
            else:
                guess = int(guess) # converts a string to an integer

            if guess == aRandomNumber:
                print ("Congrats, You got it!")
                print("Thank you for playing with me!")
                break
            elif (guess > aRandomNumber):
                print ("Try again that's too high")
                guesses = guesses + 1
            else:
                print ("Try again that's too low")
                guesses = guesses + 1
        print ("Sorry the number was " + str(aRandomNumber))
        print("Maybe next time, thank you for chatting with me!")
    if response == "no":
        print("Aw, I really wanted to play a game.")

def say_greeting():
    print ("hey how are you doing?")


def process_name(name):
    print ("Nice to chat with you " + name)




# --- Put your main program below! ---


def main():
    intro()
    while True:
        answer = input("How old are you? ")
        process_input(answer)
        response = input("Do you want to play a guessing game? yes or no? ")
        input_process(response)
        break




# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
