
class Jumper():
    """
    The "player" class of this program. Handles the few player inputs we have.

    Attributes:
        num_guesses (int): Current number of guesses
        guess (str): the lowercase version of the player's letter guess
    
    Methods:
        return_guess(): prompts for, checks, and returns guess. also updates above attributes

    """

    def __init__(self):
        """
        Class initializer
        """
        self.num_guesses = 0
        self.guess = ""

    def return_guess(self):
        """
        Promts user for guess and ensures valid user input for a one-letter lowercase hangman guess.
        Also updates self.num_guesses and self.guess

        Args:
            self: Instance of jumper

        return (str): one-character lowercase alphabetical user guess
        """
        valid = False
        while not valid:
            user_guess = input("Guess a letter [a-z]: ").lower().strip()
            if user_guess.isalpha():
                self.num_guesses += 1
                self.guess = user_guess
                return user_guess
            else:
                print("Input invalid. Please guess one (1) letter from a to z.")

        

    