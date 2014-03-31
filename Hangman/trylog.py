
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
    def __init__(self, HANGMANPICS):
        self.HANGMANPICS = HANGMANPICS
        
    def game(self, word, hidden, wrongGuess="",): 
        self.word = word
        self.hidden = hidden 
        self. wrongGuess = wrongGuess
        
    def Display_game(self):
        print self.HANGMANPICS[len(self.wrongGuess)]
        
    def Display_hidden(self):
        print self.hidden
        
        
        
# first = hangmanDisplay(HANGMANPICS)
# first.game("parrot", " pa--ot", "ghl")
# first.Display_game()
# first.Display_hidden()

log_file = open("game.log", 'r')
lines = []
for line in log_file:
    if not (line.startswith('@') or line.startswith('#')):
        lines.append(line.strip())
        
first = hangmanDisplay(HANGMANPICS)
first.game((lines[0].split(",")[0]),(lines[1].split(",")[2]),lines[1].split(",")[1])
first.Display_game()
first.Display_hidden()
 
first.game(lines[0].split(",")[0],lines[2].split(",")[2],lines[2].split(",")[1])
first.Display_game()
first.Display_hidden()    
     
first.game(lines[0].split(",")[0],lines[3].split(",")[2],lines[3].split(",")[1])
first.Display_game()
first.Display_hidden()
 
first.game(lines[0].split(",")[0],lines[4].split(",")[2],lines[4].split(",")[1])
first.Display_game()
first.Display_hidden()
 
first.game(lines[0].split(",")[0],lines[5].split(",")[2],lines[5].split(",")[1])
first.Display_game()
first.Display_hidden() 
 
first.game(lines[0].split(",")[0],lines[6].split(",")[2],lines[6].split(",")[1])
first.Display_game()
first.Display_hidden() 
 
first.game(lines[0].split(",")[0],lines[7].split(",")[2],lines[7].split(",")[1])
first.Display_game()
first.Display_hidden()  
         

# for line in lines:
#     print line.split(",")
    

    


