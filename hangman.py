import random

# A list of words that
potential_words = ["picture", "clouds", "computer", "milk", "north", "dwarves", "twelfth", "yacht","swivel"]

word = random.choice(potential_words)

# Use to test your code:
#print(word)
length = len(word)

# Converts the word to lowercase
word = word.lower()
current_word = ["__"] * length
#for letter in range (len(word)):
	#print(word[letter])
	#current_word[let] = guess

# Make it a list of letters for someone to guess
 # TIP: the number of letters should match the word

# Some useful variables
guesses = []
maxfails = length + 1
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")
	if guess == word:
		print ("Congrats you won!")
		break
		word = word.lower()
	elif guess in word:
		print ("Correct!")
		for letter in range (len(word)):
			if word[letter] == guess:
				print(word[letter])
				current_word[letter] = guess
	else:
		print ("Incorrect!")
		fails = fails+1
		print("You have " + str(maxfails - fails) + " tries left!")
	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!
	print(current_word)

	if not "__" in current_word:
		print("You won!")
		break

	#fails = fails+1
	#print("You have " + str(maxfails - fails) + " tries left!")

	#print (current_word)
	#if guess in word:
		#repeat = False
		#current_word.replace(word.find(guess),guess)
		#current_word.insert(word.find(guess), guess)
