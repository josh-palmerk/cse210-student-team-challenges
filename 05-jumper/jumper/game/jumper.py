
class Jumper():
    """
    The "player" class of this program. Handles the few player inputs we have.

    Attributes:
        num_guesses (int): Current number of guesses
        guess (str): the lowercase version of the player's letter guess
    
    Methods:
        return_guess(): self explanatory

    """
    # fill in the thing above if you get the chance. gets us brownie points in grading

    def __init__(self):
        """
        Class initializer
        """
        self.num_guesses = 0
        self.guess = ""

    def return_guess(self):
        """
        Ensures valid user input for a one-letter lowercase hangman guess.

        Args:
            self: Instance of jumper

        return (str): one-character lowercase alphabetical user guess
        """
        #make sure to have .lower() on it, and try/except for good user input or test it with a while loop
        

    