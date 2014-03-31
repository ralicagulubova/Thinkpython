from classWord import Word
from classPlayer import Player

HANGMANPICS= [
'  +---+   \n  |   |   \n      |   \n      |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n      |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n  |   |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|   |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n /    |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n / \\  |   \n      |   \n========= \n'
]


class hangmanDisplay:
    """ Display Hangman pictures and hidden word """
    
    def __init__(self, HANGMANPICS):
        """ Initialize the object
        
        >>> first = hangmanDisplay(HANGMANPICS)

        """
        self.HANGMANPICS = HANGMANPICS
        
    def game(self, word, hidden, wrongGuess=[], rightGuess=[]): 
        """
        >>> first.game("parrot", "pa--ot","wdf")
        """
        
        self.word = Word()
        self.hidden = Word()
        self. wrongGuess = wrongGuess
        self.rightGuess = rightGuess
        
    def Display_game(self):
        """
        >>> first.Display_game()
        >>> +---+   
            |   |   
            0   |   
           /|   |   
                |   
                |   
          ========= 
        """
        
        print self.HANGMANPICS[len(self.wrongGuess)]
        
    def Display_hidden(self):
        """
        >>> first.Display_hidden()
        >>> pa--ot
        """
        self.hidden = "-"*len(self.word.currentWord())
        for i in range(len(self.word.currentWord())):
            if self.word.currentWord()[i] in self.rightGuess:
                self.hidden = self.hidden[:i] + self.word.currentWord()[i] +self.hidden[i+1:]
        print self.hidden 
        
        