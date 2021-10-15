from pathlib import Path
from random import randint


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
        self.current_word = "" # Renamed for clarity
        self.hidden_word = [] #This is going to be a list
        self.wrong_guesses = 0
        self.wordbank_filename = "wordbank-1.csv" #default wordbank
        self.guessed_letters = [0]
        for i in range[26]:
            self.guessed_letters.append(0)
    
    def check_guess(self, guess):
        # for i, v in enumerate(self.word):
        #     if v == guess:
        
        already_guessed = True
        while(already_guessed):
            if(self.guessed_letters[ord(guess)-97]):
                print("You all ready Guessed that STUPID!")
            else:
                self.guessed_letters[ord(guess)-97] = 1
                already_guessed = False


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
        # the above with() indent should get a random word from wordbank-1.csv and save it into self.word.
        # this is useful because if we want to expand our program to allow selection of different wordbank csv's, 
        # we don't have to manually format them all because that's really annoying. plus you're not even 
        # halfway done splitting up the current one


    def get_blanks(self):
        """
        This method turns the length of the string to underscores and addes it to the self.hidden_word
        """
        i = 0
        while i < len(self.current_word):
            self.hidden_word.append("_")
            i += 1

    def fill_blanks(self, guess):
        """
        This method with an input of guess changes the blanks to the letter that was guessed
        """
        word = self.current_word
        word = list(word)
        for i in range(0, len(self.current_word)):
            if word[i] == guess:
                self.hidden_word[i] = guess
            else:
                self.hidden_word[i] = "_"
                

    def get_word(self):
        pass

    # I don't know if you need all of these functions, I just wrote what was on the board
