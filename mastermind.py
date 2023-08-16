import random

def playGame():
  correctFruits = []
  for i in range(4):
    correctFruits.append(fruits[random.randint(0, 3)]) # Randomly selects four fruits to be guessed
  print("\nAnswer =", correctFruits, "\n") # For testing purposes only, add/remove '#' to front of line to disable/enable testing mode
  guessAttempts = 1
  takeGuesses()
  while guessedFruits != correctFruits:
    compareGuesses(guessedFruits, correctFruits)
    guessAttempts += 1
  if guessAttempts > 7:
    print("Congratulations! It took you", guessAttempts, "attempts to get the four fruits right.")
  else:
    print("Shazam! You only needed", guessAttempts, "attempts to get the four fruits right. You are a true mastermind.")
  
def takeGuesses(): # Receives guess input from user
  guessedFruits.clear()
  for i in range(4):
    guessInput = input("Enter your guess for the " + str(position[i]) + " fruit: ").upper()
    if guessInput in fruits:
      guessedFruits.append(guessInput)
    else:
      print("\nYou have entered a fruit that is not an APPLE, BANANA, COCONUT or DURIAN. Please re-enter your guesses.\n")
      takeGuesses()
      return
  print("\nThe fruits that you have picked are", guessedFruits, ".\n")

def compareGuesses(guessedFruits, correctFruits): # Compares user guesses with correct answer
  correctPlace = 0
  wrongPlace = 0
  for i in range(4):
    if guessedFruits[i] == correctFruits[i]: # Increments correctPlace for each correct fruit guessed in the right position
      correctPlace += 1
    else:
      reducedGuess.append(guessedFruits[i])
      reducedCorrect.append(correctFruits[i])
  for j in reducedGuess:
    if j in reducedCorrect:
      wrongPlace += 1
      reducedCorrect.remove(j)
  reducedGuess.clear()
  reducedCorrect.clear()
  print("Correct fruits guessed in the correct place =", correctPlace)
  print("Correct fruits but guessed in the wrong place =", wrongPlace)
  print("Take another guess...\n")
  takeGuesses()

def replayGame(replay):
  if replay == "YES":
    print("\nGenerating a new set of fruits...")
  elif replay == "NO":
    print("\nThank you for playing!")
  else:
    replay = str(input("\nI'm not quite sure what you mean. Please enter only YES or NO: ").upper())
    replayGame(replay)

position = ["first", "second", "third", "fourth"]
fruits = ["APPLE", "BANANA", "COCONUT", "DURIAN"]
replay = "YES"
guessedFruits = []
reducedGuess = []
reducedCorrect = []
print("Welcome to Mastermind!\n") # What the user first sees when the game is booted
print("The goal of the game is to guess the four fruits in their correct order. Each fruit may appear more than once or not at all.")

while replay != "NO":
  playGame()
  replay = str(input(("\nWould you like to play another game? [YES/NO]: ")).upper()) # Asks player if they wish to replay the game
  replayGame(replay)
