


class Words():
    """
    Handles all word processing and string-checking needed for a hangman game.

    Attributes:


    Methods:
        
    """
    # fill in the thing above if you get the chance. gets us brownie points in grading

    def __init__(self):
        """
        Class initializer
        """
        self.word = ""
        self.hidden_word = [] #This is going to be a list

        # maybe have 2 attributes called word and hidden_word (hidden_word holds the one with just
        # underscores and guessed letters)
    
    def check_guess(self,guess):
        # for i, v in enumerate(self.word):
        #     if v == guess:
        if guess in self.word:
            return True
        else:
            return False
    
                


    def read_string(self):
        """This Method gets the wordbank
        
        """
        with open('wordbank.txt') as f:
            lines = f.readlines()

    def get_blanks(self):
        """This method turns the length of the string to underscores and addes it to the self.hidden_word"""
        i = 0
        while i < len(self.word):
            self.hidden_word.append("_")
            i += 1

    def fill_blanks(self, guess):
        """This method with an input of guess changes the blanks to the letter that was guessed
        
        """
        word = self.word
        word = list(word)
        for i in range(0, len(self.word)):
            if word[i] == guess:
                self.hidden_word[i] = guess
            else:
                self.hidden_word[i] = "_"
                

    def get_word(self):
        pass

    # I don't know if you need all of these functions, I just wrote what was on the board
