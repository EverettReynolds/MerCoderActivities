import random

def play():
    global playerWin
    global computerWin
    global ties
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It\'s a tie'
        

    # rock beats scissors, scissors beats paper, paper beats rock
    if is_win(user, computer):
        playerWin = playerWin + 1
        return 'You Won!'

    
    if is_win(computer, user):
      computerWin = computerWin + 1
      return 'You Lost!'

def is_win(player, opponent):
    # return true if player (you) win
    # rock beats scissors, scissors beats paper, paper beats rock
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

def scoreBoard(playerWin,computerWin):
  print("You Have Won", playerWin, "Times.")
  print("Your Opponent Has Won", computerWin, "Times.")
  print("You and Your Opponent have Tied", ties, "Times.")


continueChoice = 0
playerWin = 0
computerWin = 0
ties = 0
while continueChoice == 0:
  print(play())
  print(scoreBoard(playerWin,computerWin))
  user = input("Would You Like to Play Again? (Type 'no' to stop the game): ")
  if user == "no":
    print("Thank You for Playing Rock, Paper, Scissors!")
    continueChoice = 1
    
  
