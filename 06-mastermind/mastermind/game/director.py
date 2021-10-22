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
        self._roster = Roster()
        self._guess = Guess()


    def start_game(self):
        """"
        It starts to run the game
        """
        print("----------------------------------------------------------------")
        print (" This is a game of MASTERMIND, a random 4 digit number will be generated. \n What you are trying to do is guess that number.\n An X will be printed if you guess the right number in the right spot.\n An O will be printed if that number is in the generated number but not in the right spot. \n And a * will be printed in the spot if the number is not in the hidden number. ")
        print("----------------------------------------------------------------")
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """
        It gets the Info needed to run the game
        """
        self._board.generate_hidden_number()
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
        self._console.write(f"{player.get_name()}'s turn:")
        while not valid:
            self._guess.user_input()
            valid = self._guess.verify_input()
        self._guess.guess_to_list()
        player.set_guess(self._guess.get_guess())


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
        guess = player.get_guess()
        hint = self._board.return_hint(guess)
        self._console.print_hint(hint)

        if self._board.is_the_correct_guess(player.get_guess()):
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()

        
