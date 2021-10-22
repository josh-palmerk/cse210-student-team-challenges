from typing import Generator
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
        # self._player = Player()
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
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)
        

    def _get_inputs(self):
        """
        Get the inputs needed from the user
        """
        player = self._roster.get_current()
        valid = False
        while not valid:
            self._guess.user_input()
            valid = self._guess.verify_input()
        self._guess.guess_to_list()
        player.set_guess(self._guess.get_guess)


    def _do_updates(self):
        """
        It takes the inputs and updates the game
        """
        player = self._roster.get_current()
        player.get_guess()


    def _do_outputs(self):
        """
        Prints the Output of the game to the screen
        """
        player = self._roster.get_current()
        self._board.return_hint(player.get_guess())

        pass
