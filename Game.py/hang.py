import random
HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

max_wrong = len(HANGMAN) - 1
wordlist = [ "apple", "orange", "lemon", "grape", "strawberry" ]
word = random.choice(wordlist)
state = "-" * len(word)
wrongguess = 0
usedwords = []

print "Welcome! This is HANGMAN game"
name = raw_input("What is your name?")
print "Ok, " + name + ". Are you ready to die?!"
print " I have one word for you.It is ", state
print "Guess what is it.."

while wrongguess < max_wrong and state != word:
    print HANGMAN[wrongguess]
    print ""
    guess = raw_input("Guess a letter: ")
    usedwords.append(guess)
    if guess in word:
        print "Good choice :) " + guess + " is in my word"
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
           # else:
                #new += state[i- 1]   
                #state = new
    else:
        print "Sorry, but " + guess + " is not in my word :("
        wrongguess += 1
if wrongguess == max_wrong:
    print HANGMAN[wrongguess]
    print " You lose!!!"
else:
    print " You win ! That was my word :)"                
                  
            
        
    


