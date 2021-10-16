from pathlib import Path
from random import randint

class Words():
    """
    Handles all word processing and string-checking needed for a hangman game.

    Attributes:
        current_word (str): the word to guess
        hidden_word (list): underscores and guessed letters
        wrong_guesses (int): number of times user has guessed incorrectly
        wordbank_filename (str): wordbank being randomly pulled from
        guessed_letters (list): list of guessed letters, indexed with binary for some reason

    Methods:
        check_guess()
        fetch_word()
        get_blanks()
        fill_blanks()
        if_win()
    """

    def __init__(self):
        """
        Class initializer
        """
        self.current_word = ""
        self.hidden_word = []
        self.wrong_guesses = 0
        self.wordbank_filename = "wordbank-1.csv" #default wordbank
        self.guessed_letters = [0]

    
    def check_guess(self, guess):
        """
        Determines if guess is in the current_word.
        
        Args:
            guess (str): a-z 1-character string
        
        return: bool 
        """
        if guess in self.current_word:
            return True
        else:
            return False
    

    def fetch_word(self):
        """
        This Method gets the wordbank and assigns a random word to self.current_word
        """
        base_path = Path(__file__).parent
        file_path = (base_path / f"../game/{self.wordbank_filename}").resolve()

        with open(file_path, "rt") as csvfile:
            wordline = csvfile.read()
            word_bank = wordline.split(", ")
            self.current_word = word_bank[randint(0, len(word_bank) - 1)]


    def get_blanks(self):
        """
        This method turns the length of the string to underscores and addes it to the self.hidden_word
        return (str): Underscores matching length of current_word
        """
        i = 0
        while i < len(self.current_word):
            self.hidden_word.append("_")
            i += 1
        return self.hidden_word


    def fill_blanks(self, guess):
        """
        This method with an input of guess changes the blanks to the letter that was guessed
        Args:
            guess (str): one-letter string
        """
        word = self.current_word
        word = list(word)
        for i in range(0, len(self.current_word)):
            if word[i] == guess:
                self.hidden_word[i] = guess


    def if_win(self):
        """
        Determines if win condition has been met
        """
        if self.hidden_word == list(self.current_word):
            return True
