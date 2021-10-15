from game.words import Words
from game.console import Console
from game.jumper import Jumper

class Director():
    """
    Director class. Runs game loop.

    Attributes:
        is_hardmode (bool): sets gamemode
        wrong_guesses (int): number of wrong guesses

    Methods:
        
    """
    # fill in the thing above if you get the chance. gets us brownie points in grading

    def __init__(self):
        """
        Class initializer
        """
        self.words = Words()
        self.console = Console()
        self.jumper = Jumper()
        self.keep_playing = True # used for "play again?"
        self.alive = True # used for current round alive status
        self.is_hardmode = False
        self.wrong_guesses = 0
        self.guess = ""

    # maybe add a function that asks for hardmode? or a custom wordbank filename?

    def start_game(self):

        # put initializing imputs here. hardmode, custom word bank, etc
        print ("This is essentally a game of hang man.\nIf you guess wrong the parachuter will loose part of his parachute and you may eventually die. \nIf you complete the word without him dying, you win.")
        self.words.fetch_word()
        blank = self.words.get_blanks()
        print (blank)

        while self.keep_playing:
            while self.alive:
                self.get_inputs()
                self.do_updates()
                self.do_outputs()

        
        # print(f"{self.words.current_word}") # this is for debugging
    
    def get_inputs(self):
        # self.console.print_outputs()
        self.guess = self.jumper.return_guess()


    def do_updates(self):
        """
        this needs to:
            ###done### check if user guess is in current word
            ###done### update num guesses
            update hidden word or update ascii art (if statement)
            update right or wrong guesses
            ###done### check if game is over

        """
        correct = self.words.check_guess(self.jumper.guess)

        if correct:
            self.words.fill_blanks(self.guess)
        
        elif not correct:
            self.words.wrong_guesses += 1
            # update ascii art with jumper
        
        self.alive = self.jumper.is_alive()

        
    def do_outputs(self):
        self.console.print_outputs()
        if self.alive:
            print(self.words.hidden_word)
        else:
            # print(self.console.dead_jumper_art)
            print("Game over! :(")
            # would you like to play again?
            self.keep_playing = False #remove if play again function added
