from game.jumper import Jumper
from game.words import Words

class Console():
    """
    Console class. Handles user ins and outs by pulling functions from most other classes.

    Attributes:
        jumper_art
        dead_jumper_art

    Methods:
        get_inputs (?)
        do_updates (?)
        print_outputs()
    """
    # fill in the thing above if you get the chance. gets us brownie points in grading

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

        #prints hidden word
        print(*self.words.hidden_word, sep='')

        #check for number of wrong guesses, if under 5 it will print the normal jumper art,
        #if over 5 it will print the dead art.
        if self.words.wrong_guesses < 5:
            for i in range(self.words.wrong_guesses, 9):
                print(self.jumper_art[i])
        elif self.words.wrong_guesses == 5:
            for i in range(5):
                print(self.dead_jumper_art[i])
