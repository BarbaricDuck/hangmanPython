text_file = open("words-en.txt", "r") #Reads the file with all the words
lines = text_file.readlines() #Reads the lines
text_file.close() #Must close the text file
import random 
import time 

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
             r' |      \|/',
             ' |       |',
             ' |        ',
             ' |',
             ' |',
             '_|___\n'],
             ['  _______',
             ' |/      |',
             ' |      (_)',
             r' |      \|/',
             ' |       |',
             r' |      / \ ',
             ' |',
             ' |',
             '_|___\n']]




############### --Functions-- ###############

def createWord():
    randomNum = random.randint(0,len(lines))
    word = lines[randomNum]#selects a random number
    word = word[:-1]#This removes the \n after the word
    return(word)



def createGuessesLog(word):#This func makes a log which records
                           #the user's correct guesses
    guessesLog=''

    for i in range(len(word)):
        
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



    
    checker = False
    for _ in range(len(word)):
        if word[i] == guess:
            guessesLog[i]=guess #Add the correctly guessed letter to guessed
            
            checker = True #There has been a correct guess

        joinedGuessLog = "".join(guessesLog)#Puts the guessLog back into a str
            
    if checker is True:#If there wasn't a correctly guessed word
                       #using 'is' is better because it is a boolean
                
         print('Correct!\n')
    else:

        print('Incorrect!\n')
        incorrect+=1
        printTable()#Print the hangman


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





 
