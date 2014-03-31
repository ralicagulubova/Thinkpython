import random
import sys
from ConfigParser import SafeConfigParser
#import gettext
import logging
name = raw_input("What is your name?")

filename = "%s.log" % name

logging.basicConfig(filename=filename,level=logging.DEBUG,format="%(message)s")
logging.info("@@@@The user start game")


#t = gettext.translation("Hangman", "./locales", languages =["bg_BG"])
#_ = t.ugettext

parser = SafeConfigParser()
parser.read("ConfigParser.ini")

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

SHOTS = parser.getint("Tries", "guess")
fileWords = parser.get("Categories", "listword")
logging.info("# word, name, category, guesses ")

with open(fileWords) as f:
    words = f.read().split()

word = random.choice(words)
print word
#logging.info("the word is:%s", word)
wordLength = len(word)
noRepeatWord="".join(set(word))
wrongGuess = ""
rightGuess = ""
hidden = "-" * wordLength

#name = raw_input("What is your name?")
#logging.info("The user's name is: %s", name)
print " Hello, "  + name + ".This is HANGMAN game!!! Enjooy".format(name=name)
print " You can guess wrong only 6 times"
print " The word you should guess has {word_length} characters ".format(word_length=wordLength)
print "Hint: all of words are animals"
print hidden
print HANGMANPICS[0]
logging.info(" %s,%s,animals,%s", word,name,SHOTS)
logging.info("#rightGuess,wrongGuess,hidden,status")
def display(HANGMANPICS, wrongGuess):
    """
  Print pictures after every wrong guess
  >>> display(HANGMANPICS, 1)
  >>>  +---+
       |   |
       O   |
           |
           |
           |
   =========
   >>> display (HANGMANPICS, 2)
   >>> +---+
       |   |
       O   |
       |   |
           |
           |
   =========
    """
     
    global hidden
    print HANGMANPICS[len(wrongGuess)] 
    #logging.info(HANGMANPICS[len(wrongGuess)])
    for i in range(len(word)):
        if word[i] in rightGuess:
            hidden = hidden[:i] + word[i] +hidden[i+1:]
    print hidden 
    #logging.info(hidden)  
        
def getChar(wrongGuess, allreadyGuess):
    """
    Ask the user to guess a letter
    >>> Please enter a character
    >>> dt
    >>> You should enter only one character from the alphabet without repeating it
    >>> Please enter a character
    >>> a
    >>> Please enter a character
    >>> 9
    >>> You should enter only one character from the alphabet without repeating it
    """
    
    leng = 0
    while leng < SHOTS:
        print " Please enter a character"
        guess = raw_input()
        guess = guess.lower()
        
        if len(guess) == 1 and guess in "abcdefghijklmnopqrstuvwxyz" and guess not in allreadyGuess: 
            #logging.info("The user guessed  is: %s", guess)
            return guess
            
        else:
            print "You should enter only one character from the alphabet without repeating it"
            
            
while True:
    allreadyGuess = wrongGuess + rightGuess
    guess = getChar(wrongGuess, allreadyGuess)
    
    if guess in word:
        rightGuess += guess
        #logging.info("Right guesses are: %s ", rightGuess)
    else:
        wrongGuess += guess
        #logging.info("Wrong guesses are: %s", wrongGuess)
    
    display(HANGMANPICS, wrongGuess)
    
    logging.info("%s,%s,%s,%s",rightGuess,wrongGuess,hidden,len(wrongGuess))
    
    
    
    if len(wrongGuess) == SHOTS:
        print " You loose the word was \" {word} \" try next time".format(word=word)
        #logging.info("The user lost and finish the game")
        sys.exit()
    if len(rightGuess) == len(noRepeatWord):
        print " You are smart the word was \" {word} \" Good job".format(word = word)
        logging.info("@@@@The user win and finish the the game")
        
        sys.exit()