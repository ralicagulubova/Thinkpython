""" Choice category and word from this category """
import random
class Word(object):
    """ Choice a word from different categories """
    category = ''
    current_word = ''
    def choice_category(self):
        """ Choice category"""
        self.category = "words/" + random.choice(["animals", "colour"])
        return self.category
    def choice_word(self):
        """Choice word""" 
        with open(self.category) as myfile:
            words = myfile.read().split()
            self.current_word = random.choice(words)
            return self.current_word



# ob1 = Word()
# ob1.choice_category()
# ob1.choice_word()
