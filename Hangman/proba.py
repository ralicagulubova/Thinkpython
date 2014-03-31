# from classPlayer import *
# from classDisplay import *
# from classWord import *
from classGame import Game
import logging

from ConfigParser import SafeConfigParser


parser = SafeConfigParser()
parser.read("ConfigParser.ini")
SHOTS = parser.getint("Tries", "guess")

logging.info("# word, name, category, guesses ")


# ob = Word()
# category = ob.category()

# player = Player()
# playerName = player.name()
# filename = "%s.log" % playerName
# logging.basicConfig(filename=filename,level=logging.DEBUG,format="%(message)s")
# logging.info("@@@@The user start game")

# word = ob.currentWord()
# print word

playGame = Game()
playGame.play()