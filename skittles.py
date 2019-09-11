"""
Code Written By Kolton
In this code we generate a pseudorandom number, and make the user guess it.
If the user guess is higher or lower there will be different outputs to help the user,
the porgram will end only when the user guess the correct number. 
"""
import random
randomNum = random.randint(0,1023)
print("O hai! I'm thinking of a number between 0 and 1023. What is it?")
userNum = 1024
while userNum != randomNum:
    userNum = int(input(""))
    if userNum < 0:
        print("Nope! Don't be difficult. Guess again.")
    if userNum > randomNum:
        print("Nope! There are fewer Skittles than that. Guess again.")
    if userNum < randomNum:
        print("Nope! There are way more Skittles than that. Guess again.")
print ("That's right! Nom nom nom.")
