class Guess():
    """
    gets guess and verifies input
    """
    def __init__(self):
        """
        Class constructor
        """
        self._unfiltered_guess = ""
        self._guess = ""

    def get_guess(self):
        return self._guess

    def user_input(self):
        """
        saves guess into private var
        """
        self._unfiltered_guess = input(f"What is your guess? ")

    def verify_input(self):
        """
        ONLY determines whether input is 4 numbers 0-9
        returns bool
        """
        self._unfiltered_guess = self._unfiltered_guess.strip()
        if len(self._unfiltered_guess) == 4:
            self._guess = self._unfiltered_guess
            return True
        else:
            return False
