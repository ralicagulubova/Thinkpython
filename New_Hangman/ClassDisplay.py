""" Display Hangman pictures and hidden word """

HANGMANPICS = [
'  +---+   \n  |   |   \n      |   \n      |   \n      |   \n      |'
'   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n      |   \n      |   \n      |'
'   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n  |   |   \n      |   \n      |'
'   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|   |   \n      |   \n      |'
'   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n      |   \n      |'
'  \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n /    |   \n      |'
'   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n / \\  |   \n      |'
'   \n========= \n'
]


class HangmanDisplay(object):
    """ Display Hangman pictures and hidden word """
    hangman_pics = ''
    current_word = ''
    hidden = ''
    wrong_guess = ''
    def __init__(self, hangman_pics=''):
        """ Initialize the object
        >>> HANGMANPICS = [1,2,3,4,5,6]
        >>> first = HangmanDisplay(HANGMANPICS)

        """
        self.hangman_pics = hangman_pics or HANGMANPICS 
        
    def game(self, current_word, hidden, wrong_guess=""): 
        """
        >>> first.game("parrot", "pa--ot","wdf")
        """
        
        self.current_word = current_word
        self.hidden = hidden 
        self.wrong_guess = wrong_guess
        
    def display_game(self):
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
        
        print self.hangman_pics[len(self.wrong_guess)]
        
    def display_hidden(self):
        """
        >>> first.Display_hidden()
        >>> pa--ot
        """
        print self.hidden
        
        
#         
# first = HangmanDisplay(HANGMANPICS)
# first.game("parrot", "pa--ot","wdf")
# first.Display_game()
# first.Display_hidden()
