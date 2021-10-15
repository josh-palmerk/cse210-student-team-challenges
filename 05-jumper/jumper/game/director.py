from game.words import Words


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

        self.keep_playing = True
        self.is_hardmode = False
        self.wrong_guesses = 0

    # maybe add a function that asks for hardmode? or a custom wordbank filename?

    def start_game(self):
        print ("This is essentally a game of hang man. If you guess wrong the parachuter will loose part of his parachute and you may eventually die.")
        
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

        
        # print(f"{self.words.current_word}") # this is for debugging
    
    def get_inputs(self):
        self.words.fetch_word()


    def do_updates(self):
        pass


    def do_outputs(self):
        pass
   

    # I dont know what else this class needs. good luck

