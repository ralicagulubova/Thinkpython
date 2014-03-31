import random
import sys
from ConfigParser import SafeConfigParser
import gettext
import logging
from datetime import datetime

currentTime = datetime.now()

logging.basicConfig(filename='example.log',level=logging.DEBUG, format='%(asctime)s : %(message)s')
logging.info("user:%s start the game", currentTime )

t = gettext.translation('config', "./locales", languages=['bg_BG','en_US'])
_ = t.ugettext

parser = SafeConfigParser()
parser.read('config.ini')

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

SHOTS = parser.getint('shots', 'number_of_tryes')
fileWords = parser.get('categories', 'file_with_words')

with open(fileWords) as f:
    words = f.read().split()

word = random.choice(words)
print word
logging.info("the word is:%s", word)
wordLength = len(word)
noRepeatWord="".join(set(word))
wrongGuess = ""
rightGuess = ""
hidden = "-"*wordLength

print _(" Hello this is HANGMAN game!!! Enjooy")
print _(" U can guess wrong only 6 times")
print _(" Hint : words are only animals ")
print _(" The word you should guess has {word_length} characters ").format(word_length=wordLength)
print hidden
print HANGMANPICS[0]
def display(HANGMANPICS, wrongGuess):
    """
    Displays the pictures from HANGMANPIC according to the wronGuess number
    
    >>> display(HANGMANPICS, 1):
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    
    >>> display(HANGMANPICS, 1):
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """
    global hidden
    print HANGMANPICS[len(wrongGuess)] 
    for i in range(len(word)):
        if word[i] in rightGuess:
            hidden = hidden[:i] + word[i] +hidden[i+1:]
    print hidden   

        
def getChar(wrongGuess, allreadyGuess):
    """
    Ask the user to guess a character, check the entered value to be in the
    alphabet, to be one single character, and NOT to be all ready typed in 
    
    >>>Please enter a character
    >>>1
    You should enter only one character from the alphabet without repeating it
    
    >>>Please enter a character
    >>>asdasd
    You should enter only one character from the alphabet without repeating it
    
    >>> Please enter a character
    >>>a
    True
    """
    leng = 0
    while leng < SHOTS:
        print _(" Please enter a character")
        guess = raw_input()
        guess = guess.lower()
        
        if len(guess) == 1 and guess in "abcdefghijklmnopqrstuvwxyz" and guess not in allreadyGuess: 
            logging.info("enterd character by the user is: %s", guess)
            return guess
            
        else:
            print _("You should enter only one character from the alphabet without repeating it")

while True:
    allreadyGuess = wrongGuess + rightGuess 
    guess = getChar(wrongGuess, allreadyGuess)
    
    if guess in word:
        rightGuess += guess
    else:
        wrongGuess += guess
    
    display(HANGMANPICS, wrongGuess)
    
    if len(wrongGuess) == SHOTS:
        print _(" You loose the word was[ {word} ] try next time").format(word=word)
        logging.info("user:%s lost and finish the game", currentTime )
        sys.exit()
    if len(rightGuess) == len(noRepeatWord):
        print _(" You are smart the word was [ {word} ] Good job").format(word = word)
        logging.info("user:%s win and finish the the game", currentTime )
        sys.exit()