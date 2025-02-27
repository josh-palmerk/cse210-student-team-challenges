from game.words import Words

class Jumper():
    """
    The "player" class of this program. Handles the few player inputs we have.

    Attributes:
        num_guesses (int): Current number of guesses
        guess (str): the lowercase version of the player's letter guess
        guessed_letters (list): list of gessed letters, indexed with binary for some reason
    
    Methods:
        return_guess(): prompts for, checks, and returns guess. also updates above attributes
    """

    def __init__(self):
        """
        Class initializer
        """
        self.num_guesses = 0
        self.guess = ""
        self.guessed_letters = [0]
        for i in range(0,26):
            self.guessed_letters.append(0)
        self.words = Words()


    def return_guess(self):
        """
        Promts user for guess and ensures valid user input for a one-letter lowercase hangman guess.
        Also updates self.num_guesses and self.guess

        Args:
            self: Instance of jumper

        return (str): one-character lowercase alphabetical user guess
        """
        valid = False
        while not valid:
            user_guess = input("Guess a letter [a-z]: ").lower().strip()
            if user_guess.isalpha():
                if len(user_guess) == 1:
                    if(self.guessed_letters[ord(user_guess)-97]):
                        print("You all ready Guessed that STUPID!")
                    else:
                        self.guessed_letters[ord(user_guess)-97] = 1
                        self.num_guesses += 1   #Problay get rid of this
                        self.guess = user_guess
                        return user_guess
                else:
                    print("Please guess ONE letter.")
            else:
                print("Input invalid. Please guess one (1) letter from a to z.")
