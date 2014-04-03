""" Ask user for name and letter """
# import gettext
# t = gettext.translation("Hangman", "./locales", languages =["bg_BG"])
# _ = t.ugettext
class Player(object):
    """
    >>> ob = Player()
    """
    name = ''
    char = ''
    def get_name(self):
        """
        >>> ob.get_name()
        >>> What is your name?
        """
        self.name = raw_input("What is your name?")
        return self.name
    def get_letter(self):
        """
        >>> ob.get_letter()
        >>> Please enter a letter:
        """
        self.char = raw_input("Please enter a letter: ")
        return self.char
# ob = Player()
# ob.get_name()
# ob.get_letter()
