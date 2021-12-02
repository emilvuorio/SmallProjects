global lives
lives = 5
global guesses
global display
global answer
display = []
answer = []
guesses = []
global word
def getWord():
    global word
    word = input("Choose a word: ")
    for i in word:
        answer.append(i)
        display.append("_")
    playGame()

def playGame():

    while lives > 0:
        print("Your guesses" +str(guesses))
        print(display)
        
        guess = input("Make a guess: ")
        if guess in guesses:
            print("You already tried that")
        else:
            if len(guess) > 1:
                guessWord(guess)
            else:
                guessLetter(guess)
    gameLost()

def guessWord(guess):
    if guess == word:
        gameWon()
    else:
        guesses.append(guess)
        wrongAnswer()

def guessLetter(guess):
    guesses.append(guess)
    if guess in answer:
        print("Correct")
        for i in range(len(answer)):
                if (answer[i] is guess):
                    display[i] = guess
        if display == answer:
            gameWon()
        else:
            return display
    
    else: 
        wrongAnswer()

def wrongAnswer():
    global lives
    lives = lives -1
    print("Wrong. Lives left: " + str(lives))
    drawHangman()
    if lives == 0:
        gameLost()


def gameWon():
    print("Congratulations you won! The word was " +word)
    exit()
def gameLost():
    print("Oh no you lost. The word was: " +word)
    exit()

def drawHangman():
    if lives == 4:
        print("__|__")
    if lives == 3:
        print("  |  ")
        print("  |  ")
        print("  |  ")
        print("__|__")
    if lives == 2:
        print("  ___________ ")
        print("  |  ")
        print("  |  ")
        print("  |  ")
        print("__|__")
    if lives == 1:
        print("  ___________ ")
        print("  |          |")
        print("  |  ")
        print("  |  ")
        print("__|__")

    if lives == 0:
        print("  ___________ ")
        print("  |          |")
        print("  |          O ")
        print("  |          \/")
        print("  |          /\ ")
        print("__|__")
def main():
    getWord()

if __name__ == "__main__":
    main()
