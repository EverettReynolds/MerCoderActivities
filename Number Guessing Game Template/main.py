import random

def guess(x):
    
    #range =  input()
   #x = (int)(range)
    
    rand = random.randint(1, x)
    guess = 0
    print("Put Code Here")
    #while guess != rand:
        # Set your guess variable equal to a user input and fill in the blank of what you want the guess prompt to say
        #guess = int(input())
        #Use the Conditions if the guess is too low, too high, or right to prompt the user on their correctness


def computer_guess(x): 
    low = 1
    high = x
    feedback = ''
    while feedback != 'c': # Use characters 'c', 'h', and 'l' to denote if the guess is correct, high, or low
        if low != high: # Condition which should set the computers guess using random.randint(), print is a placeholder
            print()
        # Conditions should be if too high, if too low, correct. Allow The Computer to give accurate guess feedback

    print("Yay! The computer guessed your number", guess, "correctly!")



# At first x, is defined when being placed into the guess method. Change this to allow x to be equal to a top range of your selection within the guess method
guess(1)
 
