with open('Words-en.txt', 'r') as textFile:
    lines = textFile.readlines() 

import random 

fullTable = [
r"""
  
 
 
 
 
 

_____

""",
             
r"""
  
 |
 |     
 |      
 |       
 |      
 |
 |
_|___


""",
             
r"""
  
 |/     
 |      
 |      
 |       
 |      
 |
 |
_|___

""",
             
r"""
  _______
 |/      
 |      
 |     
 |       
 |      
 |
 |
_|___

""",
             
r"""
  _______
 |/      |
 |      
 |      
 |      
 |      
 |
 |
_|___

""",
             
r"""
  _______
 |/      |
 |      (_)
 |      
 |       
 |      
 |
 |
_|___

""",
             
r"""
  _______
 |/      |
 |      (_)
 |       |
 |       |
 |      
 |
 |
_|___

""",
r"""
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |
 |
 |
_|___

""",
r"""
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      / \
 |
 |
_|___

"""]





############### --Functions-- ###############

def createWord():
    global word
    randomNum = random.randint(0,len(lines))
    word = lines[randomNum]#selects a random number
    word = word[:-1]#This removes the \n after the word




def createGuessesLog():#This func makes a log which records
    global guessesLog,guessed
                           #the user's correct guesses
    guessesLog=''

    for _ in range(len(word)):
        
        guessesLog += '-'#makes it as long as the word
    guessesLog = list(guessesLog)#Turns it into an array because it was a str
    guessed = '' #As this is only called at the start, there have been no guesses


def printTable():
    global incorrect

        
    print(fullTable[incorrect-1])#Prints the current hangman stage

    if incorrect > 8:#There are 9 stages untill hanged
        gameOver()



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
    for i in range(len(word)):
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
    guessed += guess #Add the guess to guessed words
    guessed += ','     


def checkWin():
    global word, joinedGuessLog
    if word == joinedGuessLog:
        print(f'Congratulations, The word was {word}')
        repeat()

def gameOver():
    print(f'Computer Won! The word was {word}')
    repeat()

        

def main():
    global word, guessesLog, incorrect, guessed
    incorrect = 0
    createWord()
    createGuessesLog()

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



 
