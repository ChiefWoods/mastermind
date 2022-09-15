import random #Imports a Python library that allows for random number generation 

def guessInput(): #Prompts guess input from the user
    for i in range(4):
        guessList.append(str(input("Enter your guess for the " + str(position[i]) + " fruit: ")).upper())
    print("\nThe fruits that you have picked are", guessList, ".\n")
    validator(guessList)

def validator(guessList): #Invalidates any input that is not one of the four fruits
    for i in guessList:
        if i not in fourFruits:
            print("You have entered a fruit that is not a COCONUT, KIWI, MANGO or GRAPE. Please reenter your guesses.\n")
            del guessList[:] #Resets guess entry if invalid input is detected
            guessInput()

def main(guessList, fruitsList): #Compares player input with predetermined fruits and clues player on how close they are to guessing them
    guessAttempts = 1 #Resets guess attempt counter for every new game
    while guessList != fruitsList:
        correctPlace = 0
        wrongPlace = 0
        for i in range(4):
            if guessList[i] == fruitsList[i]: #Increments correctPlace value by one for each correct fruit guessed in the right position
                correctPlace += 1
            else:
                reducedGuessList.append(guessList[i])
                reducedFruitsList.append(fruitsList[i])
        for j in range(len(reducedGuessList)):
            if reducedGuessList[j] in reducedFruitsList:
                wrongPlace += 1
                reducedFruitsList[reducedFruitsList.index(reducedGuessList[j])] = ""
        print("Correct fruits in the correct place:", correctPlace)
        print("Correct fruits but in the wrong place:", wrongPlace)
        print("Take another guess...\n")
        guessAttempts += 1 #Increments guess attempt count by 1 for each failed guess
        del guessList[:] #Resets all related lists before asking for a new input of fruits
        del reducedGuessList[:]
        del reducedFruitsList[:]
        guessInput()
    if guessAttempts > 7:
        print("Congratulations! It took you", guessAttempts, "attempts to get the four fruits right.")
    else:
        print("Shazam! You only needed", guessAttempts, "attempts to get the four fruits right. You are truly a mastermind.")

def playAgain(replay): #Decides whether game gets replayed depending on the player's decision
    if replay == "YES":
        print("\nGlad to hear you are enjoying this. Generating a new set of four fruits...")
    elif replay == "NO":
        print("\nThank you for playing!")
    elif replay != "YES" and "NO":
        replay = str(input("\nI'm not quite sure what you mean. Please enter only YES or NO: ").upper())
        playAgain(replay)

position = ["first", "second", "third", "fourth"]
fourFruits = ["COCONUT", "KIWI", "MANGO", "GRAPE"]
replay = "YES"
print("Welcome to Mastermind!\n") #What the user first sees when the game is booted
print("The goal of the game is to guess the four fruits in order correctly. Each fruit may appear more than one time or not at all.")
while replay != "NO":
    guessList = []
    fruitsList = []
    reducedGuessList = []
    reducedFruitsList = []
    print("\nYou may pick between COCONUT, KIWI, MANGO and GRAPE.\n")
    for i in range(4):
        fruitsList.append(fourFruits[random.randint(0, 3)]) #Selects four random fruits to be guessed
    print("Answer =", fruitsList, "\n") #For testing purposes only, add/remove '#' to front of line to disable/enable testing mode
    guessInput()
    main(guessList, fruitsList)
    #replay = str(input(("\nWould you like to play another game? [YES/NO]: ")).upper()) #Asks player if they wish to replay the game
    playAgain(replay)
