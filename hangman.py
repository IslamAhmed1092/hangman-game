# Hangman game

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

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
    for char in secretWord:
        if char in lettersGuessed:
            continue
        else:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedword = ['_ '] * len(secretWord)
    for char in lettersGuessed:
        if char in secretWord:
            for i in range(len(secretWord)):
                if secretWord[i] == char:
                    guessedword[i] = char
    guessedword = ''.join(guessedword)
    return guessedword


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    AvailableLetters = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in AvailableLetters:
            AvailableLetters.remove(letter)
    AvailableLetters = ''.join(AvailableLetters)
    return AvailableLetters

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
    mistakesMade = 0
    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    while True:
        print("-------------")
        print("You have", 8 - mistakesMade, "guesses left.")
        print("Available letters:", availableLetters)
        letter = input("Please guess a letter: ")
        letter_lowercase = letter.lower()
        if letter_lowercase not in availableLetters:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            continue
        lettersGuessed += letter_lowercase
        availableLetters = getAvailableLetters(lettersGuessed)
        if letter_lowercase in secretWord:
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        else:
            mistakesMade += 1
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        if isWordGuessed(secretWord, lettersGuessed):
            print("-------------")
            print("Congratulations, you won!")
            break
        if mistakesMade == 8:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was", secretWord)
            break

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
