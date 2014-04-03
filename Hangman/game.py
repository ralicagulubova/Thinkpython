""" Final game"""
from ClassPlayer import Player
from ClassDisplay import HangmanDisplay
from ClassWord import Word
from ClassGame import Game
#import gettext
import logging

def main():
    """ pass"""
    from ConfigParser import SafeConfigParser
    parser = SafeConfigParser()
    parser.read("ConfigParser.ini")
    shots = parser.getint("Tries", "guess")
    
    word = Word()
    category = word.choice_category()
    print category

    player = Player()
    player_name = player.get_name()
    
    file_name = "%s.log" % player_name 
    logging.basicConfig(filename = file_name, level = logging.DEBUG, \
                        format = "%(message)s")
    logging.info("@@@@The user start game")
    logging.info("# word, name, category, guesses ")
   

    current_word = word.choice_word()
    logging.info("%s,%s,%s,%s",current_word, player_name, category, shots )
    play_game = Game(current_word)
    play_game.play()
    

if __name__ == "__main__":
    main()

