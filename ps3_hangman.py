# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in lettersGuessed:
        if len(secretWord) > 0:
            if i in secretWord:
                secretWord = secretWord.replace(i,'')
    if len(secretWord) == 0:
        return True
    else:
        return False
            
#secretWord = 'apple' 
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's', 'a','l']
#
#isWordGuessed(secretWord, lettersGuessed)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter not in lettersGuessed:
            secretWord = secretWord.replace(letter, '_ ')
    return secretWord
    
    
#secretWord = 'apple' 
#lettersGuessed = [ 'i', 'k', 'r', 's']   
#getGuessedWord(secretWord, lettersGuessed)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    string = string.ascii_lowercase
    for letter in lettersGuessed:
        string = string.replace(letter,'')
    return (string)
        

#lettersGuessed = [ 'i', 'k', 'r', 's']      
#getAvailableLetters(lettersGuessed)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guesses = 8
    lettersGuessed = []
    while guesses > 0:
        lettersLeft = getAvailableLetters(lettersGuessed)
        print('The word contains ', len(secretWord), 'letters.')
        print('You have', guesses, 'guesses left')
        print('The available letters are:', lettersLeft) 
        guess = input('What is your guess? ')
        while guess in lettersGuessed:
            guess = input('Oops, youve guessed that already, what is your guess? ')
        lettersGuessed += guess
        if guess in secretWord:
            print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))
            if isWordGuessed(secretWord, lettersGuessed) == True:
                return print('You Win!!')
        else:
            guesses -= 1
            print('Nope!', getGuessedWord(secretWord, lettersGuessed))
            if guesses == 0:
                return print('You Lose')
    
            

        




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
secretWord = 'apple'
hangman(secretWord)
