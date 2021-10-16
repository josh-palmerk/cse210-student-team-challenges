from game.jumper import Jumper
from game.words import Words

class Console():
    """
    Console class. Handles user ins and outs by pulling functions from most other classes.

    Attributes:
        jumper_art
        dead_jumper_art

    Methods:
        print_outputs()
    """

    def __init__(self):
        """
        Class initializer
        """
        self.words = Words()
        self.jumper = Jumper()
        self.jumper_art = [
            "\n  ___  ",
            " /___\ ",
            " \   / ",
            "  \ /  ",
            "   0   ",
            "  /|\  ",
            "  / \  ",
            "       ",
            "^^^^^^^",
        ]
        self.dead_jumper_art = [
            "\n   X   ",
            "  /|\  ",
            "  / \  ",
            "       ",
            "^^^^^^^",
        ]


    def print_outputs(self):
        print(*self.words.hidden_word, sep=' ')
        # Check for number of wrong guesses. 
        if self.words.wrong_guesses < 5:             # If under 5 it will print the normal jumper art.
            for i in range(self.words.wrong_guesses, 9):
                print(self.jumper_art[i])
        elif self.words.wrong_guesses == 5:          # If over 5 it will print the dead art.
            for i in range(5):
                print(self.dead_jumper_art[i])
