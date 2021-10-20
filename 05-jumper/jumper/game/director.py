from game.console import Console
from game.jumper import Jumper

class Director():
    """
    Director class. Runs game loop.

    Attributes:
        is_hardmode (bool): sets gamemode
        wrong_guesses (int): number of wrong guesses

    Methods:
        start_game()
        get_inputs()
        do_updates()
        do_outputs()
    """

    def __init__(self):
        """
        Class initializer
        """
        self.console = Console()
        self.jumper = Jumper()
        self.keep_playing = True # used for "play again?"
        self.alive = True # used for current round alive status
        self.is_hardmode = False
        self.guess = ""

    # maybe add a function that asks for hardmode? or a custom wordbank filename?

    def start_game(self):
        """
        This function initializes the game and runs the basic game loop.
        """
        # put initializing input loops here. hardmode, custom word bank, etc
        print ("This is essentally a game of hangman.\nIf you guess wrong, the parachuter will lose part of his parachute and you may eventually die. \nIf you complete the word without him dying, you win.")
        self.console.words.fetch_word()
        self.console.words.get_blanks()
        print(*self.console.words.hidden_word, sep=' ')

        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    
    def get_inputs(self):
        """
        This function gets the necessary inputs for the current gamemode.
        """
        self.guess = self.jumper.return_guess()


    def do_updates(self):
        """
        This function performs all updates that need to occur based on player input.
        """
        correct = self.console.words.check_guess(self.guess)

        if correct:
            self.console.words.fill_blanks(self.guess)
        
        elif not correct:
            self.console.words.wrong_guesses += 1 
        
        if self.console.words.wrong_guesses >= 5:
            self.alive = False

        
    def do_outputs(self):
        """
        This function prints all necessary information for the player to read.
        """
        self.console.print_outputs()
        if not self.alive:
            print(f"Game over! :(\nThe word was: {self.console.words.current_word}\n")
            self.keep_playing = False
            # would you like to play again?

        if self.console.words.if_win():
            print("\nYou Win!\n")
            self.keep_playing = False #remove if play again function added
            