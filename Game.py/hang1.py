import random
import sys

print "Welcome! This is HANGMAN game"
name = raw_input("What is your name?")
print "Ok, " + name + ", are you ready?! You can guess wrong only six times"

HANGMAN = ['''
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

max_wrong = len(HANGMAN) - 1
wordlist = [ "apple", "orange", "lemon", "grape", "strawberry" ]
word = random.choice(wordlist)
state = "-" * len(word)
wrongguess = 0
usedwords = []
rightGuess = ""


#print "Welcome! This is HANGMAN game"
#name = raw_input("What is your name?")
#print "Ok, " + name + ". Are you ready to die?!"
print " I have one word for you.It is ", state
print "Guess what is it.."

while wrongguess < max_wrong:
    print HANGMAN[wrongguess]
    print "You already used", usedwords
    print state
    guess = raw_input("Guess a letter: ")
    if len(guess) > 1:
        print "Please enter only one letter from the alphabet"
    usedwords.append(guess)
    
    if guess in word:
        rightGuess += guess
        print "Good choice :) " + guess.upper() + " is in my word"
        for i in range(len(word)):
            if word[i] in rightGuess:
                state = state[:i] + word[i] + state[i+1:]
                
                
    else:
        print " Sorry, but " + guess.upper() + " is not in my word "
        wrongguess += 1
        

        
    if wrongguess == max_wrong:
        print HANGMAN[wrongguess]     
        print "You lose!"
        sys.exit()
    if len(rightGuess) == len(word):
        print "You win ! The word was: ", rightGuess
        sys.exit()
        
        