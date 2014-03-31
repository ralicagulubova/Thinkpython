class Player:
    """ Ask player for name and letter
    >>> ob = Player()
    """
    def name(self):
        """
        >>> ob.name()
        >>> What is your name?
        """
        self.name = raw_input("What is your name?")
         
    def char(self):
        """
        >>> ob.char()
        >>> Please enter a letter:
        """
        self.char = raw_input("Please enter a letter: ")
        
             
         
# ob = Player()
# ob.name()
# ob.char()        