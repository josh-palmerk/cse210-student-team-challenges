import random

# TODO: Define the Board class here

class Board():
    """
    Stereotype:
        Information Holder

    This class controls the board
    It generates a hidden number and checks that hidden number based upon a guess
    Returns the hint to player
    """
    def __init__(self):
        """
        Class initializer
        """
        #self._piles = [] # list of nums
        self._hidden_number = 0
        self.guess = ""
        self.hidden = []
    

    def return_hint(self, guess):
        """returns the new hint from guess
        
        Args:
         self (board) is and instance of board
         
        Returns:
            constructed hint
        """
        hint = []
        self.guess = guess

        for i in range(0, 3):
            hint.append(self.compare_guess_to_hidden(i))         
        return hint

    def generate_hidden_number(self):
        """
        Creates the private hidden number

        Args:
         self (board) is and instance of board
         
        Returns:
            Hidden number
        """
        self._hidden_number = range(random.randint(1000, 9999))
        self.hidden = list(str(self._hidden_number))
        return self.hidden

    def is_the_correct_guess(self, guess):
        """
        Checks if the guess is the same as the hidden number


        Args:
         self (board) is and instance of board
         
        Returns:
            boolean
        """
        if guess == list(self._hidden_number):
            return True
        else:
            return False
        

    def compare_guess_to_hidden(self, i):
        """
        Compares the guess to the hidden number

        Args:
         self (board) is and instance of board
         
        Returns:
            Symbol for constructing hint
        """
        if self.guess[i] == self.hidden[i]:
            return "X"
        elif self.guess[i] == self.hidden[0] or self.guess[i] == self.hidden[1] or self.guess[i] == self.hidden[2] or self.guess[i] == self.hidden[3]:
            return "O"
        else:
            return "*" 
        
