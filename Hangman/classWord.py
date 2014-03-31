import random
class Word:
    """ Choice a word from different categories """
    def category(self):
        self.category = random.choice(["animals", "colour"])
        print self.category
        
    def currentWord(self): 
        with open(self.category) as f:
                words = f.read().split()
                self.currentWord = random.choice(words)
                print self.currentWord
        
  
  
# ob1 = Word()
# ob1.category()
# ob1.currentWord()
          
           
