class Player:
    """A person taking part in a game. The responsibility of Player is to keep track of their identity and last guess.
    
    Stereotype: 
        Information Holder

    Attributes:
        _name (string): The player's name.
        _guess (Guess): The player's last guess.
    """

    def __init__(self, name):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
        """
        self._name = name
        self._guess = ["-", "-", "-", "-"]
        self._prev_hint = ["-", "-", "-", "-"]
        
    def get_guess(self):
        """Returns the player's last guess (an instance of guess). If the player 
        hasn't guessed yet this method returns None.

        Args:
            self (Player): an instance of Player.
        """
        return self._guess

    def get_name(self):
        """Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        return self._name

    def set_guess(self, guess):
        """Sets the player's last guess to the given instance of Guess.

        Args:
            self (Player): an instance of Player.
            guess (Guess): an instance of guess
        """
        self._guess = guess

    def set_prev_hint(self, prev_hint):
        """Sets the player's last hint to the given parameter.

        Args:
            self (Player): an instance of Player.
            prev_hint
        """
        self._prev_hint = prev_hint

    def get_prev_hint(self):
        """Returns the player's last hint. If the player 
        hasn't guessed yet this method returns None.

        Args:
            self (Player): an instance of Player.
        """
        return self._prev_hint
