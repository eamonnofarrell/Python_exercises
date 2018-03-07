#Eamonn O'Farrell
# Suggested Week 4 tutorial exercise - generate random number
# Take user input to guess number

from random import randint

Target=randint(1, 100)
Guess=101

print("Guess a number between 1 and 100")
while Guess != Target:
    Guess=(int(input("Please enter your guess:")))
    if Guess == Target:
        print("You have guessed correctly!")
    elif Guess<Target:
        print("Too low!")
    else:
        print("Too high")
            
