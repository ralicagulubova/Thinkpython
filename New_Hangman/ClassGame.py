""" Game"""
from ClassPlayer  import Player
from ClassDisplay import HangmanDisplay
from ClassWord import Word
#import gettext
import sys
import logging
# t = gettext.translation("Hangman", "./locales", languages =["bg_BG"])
# _ = t.ugettext

class Game(object):
    """Create the game"""
    player = Player()
    display = HangmanDisplay()
    #guess = player.get_letter()
    def __init__(self, current_word, right_guess= "", 
                 wrong_guess = "",used = "", shots = 6):
        """ initialization """
        self.current_word = current_word
        #self.hidden = hidden
        self.right_guess = right_guess
        self.wrong_guess = wrong_guess
        self.used = used
        self.shots = shots
        self.used = self.wrong_guess + self.right_guess 
       
    def hidden_word(self):
        """ Create the hidden word  """
        self.hidden = "-"*len(self.current_word)
        for i in range(len(self.current_word)):
            if self.current_word[i] in self.right_guess:
                self.hidden = self.hidden[:i] + self.current_word[i]\
                + self.hidden[i+1:]
            print self.hidden    

    def get_char(self):
        """Create an object from the Player class ask \
        the player to enter a character and check it """
        leng = 0
        while leng < self.shots:
            #self.player.get_letter()
            guess = self.player.get_letter()
            self.guess = guess
            
            if len(guess) !=1 or type(guess) is int:
                print "You should enter only one letter from the alphabet \
                without repeating it"
            elif guess in self.used:
                print "You should enter only one letter from the alphabet \
                without repeating it"
            else:
                return guess  

                    
            
#             if len(guess) == 1 and guess in "abcdefghijklmnopqrstuvwxyz" \
#                 and guess not in self.used: 
#                 return guess
#             else:
#                 print "You should enter only one character\
#                 from the alphabet without repeating it"


    def play(self):
        """ Display the game status"""
        #hidden = "-" * len(self.current_word)
        while True:
            self.used = self.wrong_guess + self.right_guess
            print "You already used: ", self.used
            self.get_char()
            if self.guess in self.current_word:
                self.right_guess += self.guess       
                
            else:
                self.wrong_guess += self.guess
                
            self.hidden_word()
            self.display.game(self.current_word,self.hidden, self.wrong_guess)
            self.display.display_game()
            self.display.display_hidden()

            logging.info("%s,%s,%s,%s", self.right_guess, self.wrong_guess,
                         self.hidden,len(self.wrong_guess))
            if len(self.wrong_guess) == self.shots:
                print " You loose the word was \"{word} \"try next time"\
                .format(word=self.current_word)
                logging.info("@@@@The user lost and finish the game")
                sys.exit()
            if len(self.right_guess) == len(self.current_word):
                print " You are smart the word was \"{word}\" Good job"\
                .format(word = self.current_word)
                logging.info("@@@@The user win and finish the the game")
                sys.exit()

