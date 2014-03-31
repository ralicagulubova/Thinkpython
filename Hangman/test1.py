import random
import sys
import logging
logging.basicConfig(filename = "", level = logging.DEBUG)
from ConfigParser import SafeConfigParser
parser = SafeConfigParser()
parser.read("ConfigRarser.ini")


#import gettext
#t = gettext.translation('Game', "/.locales", languages = ["bg_BG"])
#_ = t.ugettext
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
fileWords = parser.get("Categories", "listword")
with open(fileWords) as f:
    words = f.read().split()
word = random.choice(words)
logging.info(word)
print word
noRepeatWord="".join(set(word))
wrongGuess = ""
rightGuess = ""

SHOTS = parser.getint("Tries", "guess")
    
print " Hello this is HANGMAN game!!! Enjooy"
print  " U can guess wrong only 6 times"
print "Hint : words are only animals "
print HANGMANPICS[0]
def display(HANGMANPICS, wrongGuess):
    print HANGMANPICS[len(wrongGuess)]
        
def getChar(wrongGuess, allreadyGuess):
    leng = 0
    while leng < SHOTS:
        print " Please enter a character"
        guess = raw_input()
        guess = guess.lower()
        logging.info(guess)
       
        if len(guess) == 1 and guess in "abcdefghijklmnopqrstuvwxyz" and guess not in allreadyGuess: #==Change here
            return guess
        else:
            print "You should enter only one character from the alphabet without repeating it"

while True:
    allreadyGuess = wrongGuess + rightGuess #================== change her
    guess = getChar(wrongGuess, allreadyGuess)
    
    if guess in word:
        rightGuess += guess
        logging.info(rightGuess)
    else:
        wrongGuess += guess
    
    display(HANGMANPICS, wrongGuess)
    
    if len(wrongGuess) == 6:
        print " You loose the word was {"+word+"} try next time"
        sys.exit()
    if len(rightGuess) == len(noRepeatWord):
        print " You are smart the word was {"+word+"} Good job"
        sys.exit()