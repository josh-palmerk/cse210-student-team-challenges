from game.board import Board
from game.console import Console
from game.guess import Guess
from game.player import Player
from game.roster import Roster

class Director():
    """
    The object for the director of a game of Mastermind. This class can officiate the game.

    Methods:
        _prepare_game()
        start_game()
        get_inputs()
        do_updates()
        do_outputs()
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
        This method runs _prepare_game() and handles the gameloop.
        """
        print("----------------------------------------------------------------")
        print(" This is a game of MASTERMIND, a random 4 digit number will be generated. \n What you are trying to do is guess that number.\n An X will be printed if you guess the right number in the right spot.\n An O will be printed if that number is in the generated number but not in the right spot. \n And a * will be printed in the spot if the number is not in the hidden number. ")
        print("----------------------------------------------------------------\n")
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            #self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """
        This method readies the game to be played.
        """
        self._board.generate_hidden_number()
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)
        self._roster.next_player() # Makes player 1 current player
        

    def _get_inputs(self):
        """
        This method gets the inputs needed from the user.
        """
        player = self._roster.get_current()
        valid = False
        self._console.write(f"\n{player.get_name()}'s turn:")
        while not valid:
            self._guess.user_input()
            valid = self._guess.verify_input()
            if not valid:
                self._console.write(f"\n{player.get_name()}, that is not a valid guess.\n")
        self._guess.guess_to_list()
        player.set_guess(self._guess.get_guess())


    # def _do_updates(self):
    #     """
    #     This method takes the inputs and updates the game.
    #     """
    #     player = self._roster.get_current()
    #     player.get_guess()


    def _do_outputs(self):
        """
        This method prints the output of the game to the terminal.
        """
        current_player = self._roster.get_current()
        player1 = self._roster.players[0]
        player2 = self._roster.players[1]
        guess = current_player.get_guess()
        hint = self._board.return_hint(guess)
        current_player.set_prev_hint(hint)
        self._console.write("\n---------------------------------------")
        self._console.write("Previous guesses:")
        print(player1.get_name(), ": ", *player1.get_guess(), "  ", *player1.get_prev_hint(), sep="")
        print(player2.get_name(), ": ", *player2.get_guess(), "  ", *player2.get_prev_hint(), sep="")
        self._console.write("---------------------------------------")
        if (current_player.get_prev_hint() == (['*', '*', '*', '*'])):
            self._console.write("Ha Ha, you got it all wrong!")


        if self._board.is_the_correct_guess(current_player.get_guess()):
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!\nThanks for playing!\n")
            self._keep_playing = False
        
        self._roster.next_player()
