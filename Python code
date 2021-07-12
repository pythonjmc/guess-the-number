#import random
import random

#creation and assignment of variables
secret_number = random.randint(1,5) #Here the program will randomly choose a number between 1 and 5, you can change these two numbers as you wish.
msg = "please enter a whole number"

#loop creation
while True:
    player_number = input(msg)

    if secret_number == int(player_number):
        print("correct !")
        break #If the answer entered is correct, the program stops, so as not to ask the question again when the number has been found
    elif secret_number > int(player_number):
        print("Trop small")
    else:
        print("Too big")
