import random 

def clear():
    print('\n'*20)

with open('Words-en.txt', 'r') as textFile:
    lines = textFile.readlines() 

with open('fullTable.txt','r') as fullTableFile:
    fullTable = fullTableFile.read().split(',')

def createWord():
    word = random.choice(lines)  # selects a random number
    word = word.strip()  # This removes the \n after the word
    return word

def createcorrectGuesses(word):  
    correctGuesses = []
    for _ in range(len(word)):
        correctGuesses.append('-')
    return correctGuesses

def printTable(incorrect,word):
    print(fullTable[incorrect-1])  # Prints the current hangman stage
    if incorrect > 8:  # There are 9 stages until hanged
        gameOver(word)

def guess(correctGuesses,guessed,word,incorrect):
    guessedStr = ''.join(guessed)    
    print(''.join(correctGuesses))
    guess = input(f'What is your guess? Guessed: {guessedStr}\n')
    while guess in guessed:
        print('You already guessed that!')
        guess = input(f'What is your guess? Guessed: {guessedStr}\n')   

    guessed.append(guess)  # Add the guess to guessed words     
    clear()
    checker = False
    for i,v in enumerate(word):
        if v == guess:
            correctGuesses[i]=guess  # Add the correctly guessed letter to guessed           
            checker = True            
    if checker is True:             
         print('Correct!\n')
         return 'correct'
    else:
        print('Incorrect!\n')
        return 'incorrect'
          
    
        


def checkWin(word,correctGuesses):
    
    if word == ''.join(correctGuesses):
        print(f'Congratulations, The word was {word}')
        repeat()

def gameOver(word):
    print(f'Computer Won! The word was {word}')
    repeat()

def main():
    incorrect = 0
    guessed = []
    word = createWord()
    correctGuesses = createcorrectGuesses(word)

    while True:
        if guess(correctGuesses,guessed,word,incorrect) == 'incorrect':
            incorrect += 1
            printTable(incorrect,word)
        
        checkWin(word,correctGuesses)

        
        
def repeat():
    x = int(input('To go again, enter 1...'))
    if x == 1:
        main()
    exit()



main()



 
