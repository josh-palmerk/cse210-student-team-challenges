class Guess():
    """
    Handles everything related to a guess.
    To use properly, run a while loop that depends on the 
    verify_input outcome, with user_input inside the loop.
    When loop is complete, run guess_to_list, then get your 
    result with the get_guess accessor method.
    Methods:
        user_input(): Prompts user and saves unfiltered guess
        verify_input(): Returns True if guess meets criteria
        guess_to_list(): Final processing piece for guess. Self explanatory
        get_guess(): Accessor method for "finished" guess
    """
    def __init__(self):
        """
        Class constructor
        """
        self._unfiltered_guess = ""
        self.str_guess = ""
        self._guess = ""

    def get_guess(self):
        """
        Accessor method for _guess
        """
        return self._guess

    def user_input(self):
        """
        Prompts user and saves guess into private attribute for verifying and processing
        """
        self._unfiltered_guess = input("What is your guess? ") # use console.read() ?

    def verify_input(self):
        """
        ONLY determines whether input is 4 numbers 0-9
        returns bool
        """
        self._unfiltered_guess = self._unfiltered_guess.strip()
        if len(self._unfiltered_guess) == 4 and self._unfiltered_guess.isdecimal():
            self._str_guess = self._unfiltered_guess
            return True
        else:
            return False

    def guess_to_list(self):
        """
        Turns _guess into a list with the contents of the _str_guess string.
        """
        self._guess = list(self._str_guess)
