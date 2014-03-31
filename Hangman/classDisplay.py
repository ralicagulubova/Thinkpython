
HANGMANPICS = [
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
        
    def game(self, currentword = "", hidden = "", wrongGuess=""): 
        """
        >>> first.game("parrot", "pa--ot","wdf")
        """
        
        self.currentword = currentword
        self.hidden = hidden 
        self. wrongGuess = wrongGuess
        
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
        print self.hidden
        
        
#         
# first = hangmanDisplay(HANGMANPICS)
# first.game("parrot", "pa--ot","wdf")
# first.Display_game()
# first.Display_hidden()