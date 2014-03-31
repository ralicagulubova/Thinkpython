from classPlayer import *
from classDisplay import *
from classWord import *
import sys
import logging

ob = Word()
category = ob.category()
word = ob.currentWord()
ob1 = Player()
guess = ob1.char()
name = ob1.name()
ob2 = hangmanDisplay(HANGMANPICS)
game = ob2.game()
display = ob2.Display_game()
hidden = ob2.Display_hidden()

class Game(object):
    def __init__(self, word,hidden, rightGuess= [], wrongGuess=[],used = [], SHOTS = 6):
        self.word = word
        self.hidden = hidden
        self.rightGuess = rightGuess
        self.wrongGuess = wrongGuess
        self.used = used
        self.SHOTS = SHOTS
        
    def hidden(self):
        for i in range(len(self.word)):
            if self.word[i] in self.rightGuess:
                self.hidden= self.hidden[:i] + self.word[i] + self.hidden[i+1:]
            print self.hidden    
        
    def get_char(self):
        leng = 0
        while leng < self.SHOTS:
            print " Please enter a character"
            guess 
            guess = guess.lower()
            if len(guess) == 1 and guess in "abcdefghijklmnopqrstuvwxyz" and guess not in self.used: 
                return guess
            else:
                print "You should enter only one character from the alphabet without repeating it"
            
            
    def play(self):
        while True:
            self.used = self.wrongGuess + self.rightGuess
            if guess in self.word:
                self.rightGuess += guess        
            else:
                self.wrongGuess += guess
                game(word, self.hidden, self.wrongGuess)
                display=ob2.Display_game()
                hidden= ob2.Display_hidden()
    
                logging.info("%s,%s,%s,%s",self.rightGuess,self.wrongGuess,self.hidden,len(self.wrongGuess))
    
    
    
            if len(self.wrongGuess) == self.SHOTS:
                print " You loose the word was \" {word} \" try next time".format(word=word)
                logging.info("@@@@The user lost and finish the game")
                sys.exit()
            if self.hidden == self.word:
                print " You are smart the word was \" {word} \" Good job".format(word = word)
                logging.info("@@@@The user win and finish the the game")
        
                sys.exit()
            
            
            
    
        