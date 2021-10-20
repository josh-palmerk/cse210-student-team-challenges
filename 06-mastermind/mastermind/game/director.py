from game.board import Board
from game.console import Console
from game.guess import Guess
from game.player import Player
from game.roster import Roster

class Director():
    """
    hosts start_game and runs gameloop
    """
    def __init__(self):
        """
        Class constructor
        """
        self._board = Board()
        self._console = Console()
        self._keep_playing = True
        self._player = Player()
        self._roster = Roster()
        self._guess = Guess()


    def start_game(self):
        """"
        It starts to run the game
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """
        It gets the Info needed to run the game
        """
        pass

    def _get_inputs(self):
        """
        Get the inputs needed from the user
        """
        pass

    def _do_updates(self):
        """
        It takes the inputs and updates the game
        """
        pass

    def _do_outputs(self):
        """
        Prints the Output of the game to the screen
        """
        pass
