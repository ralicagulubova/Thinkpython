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
        


log_file = open("game.log", 'r')
lines = []
for line in log_file:
    line = line.strip()
    if line and not (line.startswith('@') or line.startswith('#')):
        lines.append(line)

word = lines[0].split(",")[0] 
hidden = []
wrongGuess = []

  
while (word != hidden) or (wrongGuess < len(HANGMANPICS)):
    for i in range(len(lines)-1):
        hidden = lines[i].split(",")[2] = lines[i+1].split(",")[2] 
        wrongGuess = lines[i].split(",")[1] = lines[i+1].split(",")[1]
        first = hangmanDisplay(HANGMANPICS)
        first.game(word,hidden,wrongGuess)
        first.Display_game()
        first.Display_hidden()
    else:
        print "\"The end\""
        
    
    