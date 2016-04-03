import random

def game():
	# Generate a random number between 1 and 10
	secret_num = random.randint(1, 100)
	guesses = []

	while len(guesses) < 5:
		
		try:
			# Get a number guess from the player
			guess = int(input("Guess a number between 1 and 10: "))
			
		except ValueError:
			print("{} isn't a number!".format(guess))
		
		else:
			# Compare guess to secret number
			if guess == secret_num:
				print("You got it! My number was {}".format(secret_num))
				break
			elif guess < secret_num:
				guesses.append(guess)
				print("My number is higher than {}".format(guess))
				print("{} guesses remaining".format((5 - len(guesses))))
			else:	
				guesses.append(guess)
				print("My number is lower than {}".format(guess))
				print("{} guesses remaining".format((5 - len(guesses))))
	else:
		print("You didn't get it, my number was {}. Thanks for playing!".format(secret_num))
		
		play_again = input("Do you want to play again? Y/n ")
		
		if play_again.lower() != "n":
			game()
		else:
			print("Bye!")
		
game()