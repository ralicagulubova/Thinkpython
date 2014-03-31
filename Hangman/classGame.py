from classPlayer import *
from classDisplay import *
from classWord import Word
import sys
import logging

class Game(object):
    word = Word()
    category = word.category()
    currentword = word.currentWord()

    player = Player()
    name = player.name()
    #guess = player.char()

    display = hangmanDisplay(HANGMANPICS)
#     display.game()
#     display.Display_game()
#     display.Display_hidden()

    
    def __init__(self, currentword = "", hidden = "", rightGuess= "", wrongGuess="",used = "", SHOTS = 6):
        self.currentword = currentword
        self.hidden = hidden
        self.rightGuess = rightGuess
        self.wrongGuess = wrongGuess
        self.used = used
        self.SHOTS = SHOTS
        
    def hidden(self):
        self.hidden = "-" * len(self.currentword)
        for i in range(len(self.currentword)):
            if self.currentword[i] in self.rightGuess:
                self.hidden= self.hidden[:i] + self.currentword[i] + self.hidden[i+1:]
            print self.hidden    
        
    def get_char(self):
        leng = 0
        while leng < self.SHOTS:
            guess = self.player.char() 
            #guess = self.guess.lower()
            if len(guess) == 1 and guess in "abcdefghijklmnopqrstuvwxyz" and guess not in self.used: 
                return guess
            else:
                print "You should enter only one character from the alphabet without repeating it"
            
            
    def play(self):

        while True:
            self.used = self.wrongGuess + self.rightGuess 
            self.get_char()
            if self.guess in self.currentword:
                self.rightGuess += self.guess       
            else:
                self.wrongGuess += self.guess
                
                #display = hangmanDisplay(HANGMANPICS)
                self.display.game(self.currentword, self.hidden, self.wrongGuess)
                self.display.Display_game()
                self.display.Display_hidden()
    
                logging.info("%s,%s,%s,%s",self.rightGuess,self.wrongGuess,self.hidden,len(self.wrongGuess))
    
    
    
            if len(self.wrongGuess) == self.SHOTS:
                print " You loose the word was \" {word} \" try next time"#.format(word=self.currentword)
                logging.info("@@@@The user lost and finish the game")
                sys.exit()
            if self.hidden == self.currentword:
                print " You are smart the word was \" {word} \" Good job"#.format(word = self.currentword)
                logging.info("@@@@The user win and finish the the game")
        
                sys.exit()
                
                
                
                

            
