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
        self.keep_playing = True
        self.is_hardmode = False
        self.wrong_guesses = 0
        self.guess = ""

    # maybe add a function that asks for hardmode? or a custom wordbank filename?

    def start_game(self):

        print ("This is essentally a game of hang man.\nIf you guess wrong the parachuter will loose part of his parachute and you may eventually die. \nIf you complete the word without him dying, you win.")
        self.words.fetch_word()
        blank = self.words.get_blanks()
        self.words.hidden_word
        print (blank)
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

        
        # print(f"{self.words.current_word}") # this is for debugging
    
    def get_inputs(self):
        self.console.print_outputs()
        self.guess = self.jumper.return_guess()
        #self.words.fetch_word()


    def do_updates(self):
        self.words.fill_blanks(self.guess)



    def do_outputs(self):
        print (self.words.hidden_word)
        if self.jumper.is_alive() == True:
            self.keep_playing = True
        else:
            self.keep_playing = False
   

    # I dont know what else this class needs. good luck

