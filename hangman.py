text_file = open("words-en.txt", "r") #Reads the file with all the words
lines = text_file.readlines() #Reads the lines
text_file.close() #Must close the text file
from random import * #using * stops the need for 'random.' 
from time import * #Vise versa

fullTable = [[' ',
              ' ',
              ' ',
             '_____\n'],
             [' |',
             ' |',
             ' |',
             ' |',
             ' |',
             ' |',
             ' |',
             '_|___\n'],
             [' |/      ',
             ' |',
             ' |',
             ' |',
             ' |',
             ' |',
             ' |',
             '_|___\n'],
             ['  _______',
             ' |/      ',
             ' |',
             ' |',
             ' |',
             ' |',
             ' |',
             ' |',
             '_|___\n'],
             ['  _______',
             ' |/      |',
             ' |',
             ' |',
             ' |',
             ' |',
             ' |',
             ' |',
             '_|___\n'],
             ['  _______',
             ' |/      |',
             ' |      (_)',
             ' |',
             ' |',
             ' |',
             ' |',
             ' |',
             '_|___\n'],
             ['  _______',
             ' |/      |',
             ' |      (_)',
             ' |       |',
             ' |       |',
             ' |        ',
             ' |',
             ' |',
             '_|___\n'],
             ['  _______',
             ' |/      |',
             ' |      (_)',
             ' |      \|/',
             ' |       |',
             ' |        ',
             ' |',
             ' |',
             '_|___\n'],
             ['  _______',
             ' |/      |',
             ' |      (_)',
             ' |      \|/',
             ' |       |',
             ' |      / \ ',
             ' |',
             ' |',
             '_|___\n']]




############### --Functions-- ###############

def createWord():
    randomNum = randint(0,len(lines))
    word = lines[randomNum]#selects a random number
    word = word[:-1]#This removes the \n after the word
    return(word)



def createGuessesLog(word):#This func makes a log which records
                           #the user's correct guesses
    guessesLog=''

    for _ in range(len(word)):
        
        guessesLog += '-'#makes it as long as the word
    guessesLog = list(guessesLog)#Turns it into an array because it was a str

    return guessesLog


def printTable():
    global incorrect
    if incorrect > 8:#There are 9 stages untill hanged
        gameOver()
        
    toPrint = (fullTable[incorrect-1])#Gets the array of the current hangman stage
    for i in range(len(fullTable[incorrect-1])):
        print(toPrint[i])#prints the hangman in stages



def guess():
    global word, guessesLog,incorrect,guessed,joinedGuessLog
    #Global allows the variables to be used in other funcs
    
    joinedGuessLog = "".join(guessesLog)#Puts the guessLog back into a str

    while True:
        print(joinedGuessLog)
        guess = input(f'\nWhat is your guess? Guessed: {guessed}\n')
        #f''allows variables to put in {}
        
        if guess in guessed:
            print('You already guessed that!\n')
            continue
        break

    guessed = guessed + guess


    checker = False #This checks if a letter has been guessed correctly
    for i in range(len(word)):
        if word[i] == guess:
            guessesLog[i]=guess #Add the correctly guessed letter to guessed
            
            checker = True #There has been a correct guess

        joinedGuessLog = "".join(guessesLog)#Puts the guessLog back into a str
            
    if checker == False:#If there wasn't a correctly guessed word
                
        print('Incorrect!\n')
        incorrect+=1
        printTable()#Print the hangman 
    else:
        print('Correct!\n')


def checkWin():
    global word, joinedGuessLog
    if word == joinedGuessLog:
        print(f'Congratulations, The word was {word}')
        repeat()

def gameOver():
    print(f'Computer Won! The word was {word}')
    repeat()

        

def main():
    global word,guessesLog,incorrect,guessed

    incorrect = 0
    guessed = ''
    word = createWord()
    guessesLog = createGuessesLog(word)

    while True:
        guess()
        checkWin()

        
        
def repeat():
    x = int(input('To go again, enter 1...'))
    if x == 1:
        main()
    exit()

############### --Call main()-- ###############

main()





 
