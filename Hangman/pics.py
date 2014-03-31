HANGMANPICS = [
'  +---+   \n  |   |   \n      |   \n      |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n      |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n  |   |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|   |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n /    |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n / \\  |   \n      |   \n========= \n'
]


def display_game(HANGMANPICS, wrongGuess, rightGuess, hidden):
    print HANGMANPICS[len(wrongGuess)]
    print ("Wrong guesses are : "), 
    for letter in wrongGuess:
        print letter
    print ("Right guesses are: ")
    for letter in rightGuess:
        print letter 
    hidden = "-" *len(word)
    for i in range(len(word)):
        if word[i] in rightGuess:
            hidden = hidden[:i] + word[i] + hidden[i+1:]
    print "Word till now is: ", hidden
        


word = "lion"      
display_game(HANGMANPICS, "wpyg", "li", "")

        
                 
            
    
    