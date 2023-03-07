import random

def guess(x):
    range =  input("What is The Top of Your Range for Guessing:")
    x = (int)(range)
    global guessCount
    global winCount
    global lossCount
    guessCount = 0
    winCount = 0
    lossCount = 0
    rand = random.randint(1, x)
    guess = 0
    print("You Have Won", winCount,"Times and You Have Lost", lossCount, "Times.")
    while guess != rand:
        print("You have" , (10-guessCount),"Guesses Left." )
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < rand:
            guessCount = guessCount + 1
            print('Sorry, guess again. Too low.')
        if guess > rand:
            guessCount = guessCount + 1
            print('Sorry, guess again. Too high.')
        if guessCount >= 10:
            lossCount = lossCount + 1
            break;
        if guess == rand:
          winCount = winCount + 1
          print("You have guessed the number", rand , "correctly.")

def computer_guess(x): 
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print("Yay! The computer guessed your number", guess, "correctly!")



continueChoice = 0
playerWin = 0
computerWin = 0

while continueChoice == 0:
  guess(1)
  user = input("Would You Like to Play Again? (Type 'no' to stop the game): ")
  if user == "no":
    print("Thank You for Playing The Number Guessing Game!")
    continueChoice = 1
