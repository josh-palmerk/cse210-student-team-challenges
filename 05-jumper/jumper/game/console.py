from game.jumper import Jumper
from game.words import Words

class Console():
    """
    Console class. Handles user ins and outs by pulling functions from most other classes.

    Attributes:


    Methods:
        
    """
    # fill in the thing above if you get the chance. gets us brownie points in grading

    def __init__(self):
        """
        Class initializer
        """
        self.words = Words()
        self.jumper = Jumper()
        self.jumper_art = [
            "  ___  ",
            " /___\ ",
            " \   / ",
            "  \ /  ",
            "   0   ",
            "  /|\  ",
            "  / \  ",
            "       ",
            "^^^^^^^",
        ]

    def get_inputs(self):
        # needs to get guess and...?
        self.jumper.return_guess()

    def do_updates(self):
        """
        this needs to:
            ###done### check if user guess is in current word
            ###done### update num guesses
            update hidden word or update ascii art (if statement)
            update right or wrong guesses
            check if game is over

        """
        correct = self.words.check_guess(self.jumper.guess)

        if correct:
            #update hidden word
            pass
        elif not correct:
            self.words.wrong_guesses += 1
            # update ascii art with jumper
        
        # check if game_over here

        

    def print_outputs(self):
        # needs to print ascii art, hidden word, etc??
        pass
