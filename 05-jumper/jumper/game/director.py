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


        self.is_hardmode = False
        self.wrong_guesses = 0

    # maybe add a function that asks for hardmode? or a custom wordbank filename?

    def start_game(self):
        self.words.fetch_word()
        # print(f"{self.words.current_word}") # this is for debugging
    
    def get_word(self):
        pass

    def get_input(self):
        pass

    # I dont know what else this class needs. good luck

