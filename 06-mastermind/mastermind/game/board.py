import random

# TODO: Define the Board class here

class Board():
    """
    
    """
    def __init__(self):
        """
        Class initializer
        """
        #self._piles = [] # list of nums
        self.hidden_number

    def apply(self, move):
        #self._piles[move.get_pile()] = max(0, self._piles[move.get_pile()] - move.get_stones())
        pass


    def is_empty(self):
        # if sum(self._piles) == 0:
        #     return True
        # else:
        #     return False
        pass

    def to_string(self):
        # string_list = []
        # for i in range(len(self._piles)):
        #     string_list.append(f"{i}:  " + ("O " * self._piles[i]))
        # string = "\n".join(string_list)
        # return string
        pass

    def check_hidden_number(self):

        pass

    def apply_guess_to_player(self, guess):
        """reference guess in apply guess"""
        guess = list(guess)
        hidden = self.hidden_number
        hidden = list(hidden)
        hint = []

        for i in range(0, 3):
            if guess[i] == hidden[i]:
                hint.append ("0") 
            elif guess[i] == hidden[0] or guess [i] == hidden[1] or guess [i] == hidden[2] or guess [i] == hidden[3]:
                hint.append ("X")
        return hint

    def _generate_hidden_number(self):
        self.hidden_number = range(random.randint(1000, 9999))
        return self.hidden_number

    def is_the_correct_guess(self, guess):
        if guess == self.hidden_number:
            return True
        

    def compare_guess(self, guess):
        
        
