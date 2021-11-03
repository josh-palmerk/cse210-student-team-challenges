from random import randint
from pathlib import Path
import raylibpy

from game import constants

from game.score_board import ScoreBoard

from game.word import Word

from game.buffer import Buffer

class Director():
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        input_service (InputService): The input mechanism.
        output_service (OutputService): The output mechanism.
        ??? keep_playing (boolean): Whether or not the game can continue.
        ??? score (Score): The current score.
        
    """
    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._input_service = input_service
        self._output_service = output_service
        self._keep_playing = True
        self._score_board = ScoreBoard()
        self._buffer = Buffer()
        self._word_bank = [] # words.txt
        self._current_words = [] # onscreen words
        # add more attributes and instances based on game needs

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        print("Starting game...")

        self._get_wordbank()

        self._output_service.open_window("Speed")

        self._spawn_debug_word() # remove for finished product

        self._starting_wordspawn()


        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

            if self._input_service.window_should_close():
                self._keep_playing = False

        print("Game over!")

    def _get_inputs(self):
        key_press = self._input_service.get_key_press()
        self._buffer.add_character_to_buffer(key_press)

    def _do_updates(self):
        """
        $$$ check if word reached end of screen
        $$$ handle buffer check & reset
        $$$ add points and remove word if typed
        $$$ spawn new words
        """
        
        for i in range(len(self._current_words) - 1):
            word = self._current_words[i]
            if self._is_dead(word):
                self._score_board.add_points(-word.get_points())
                self._current_words.pop(i)
                if self._score_board.get_points() <= 0:
                    self._keep_playing = False
            if self._is_contained(word):
                self._score_board.add_points(word.get_points()) 
                self._current_words.pop(i)
                self._buffer.clear_buffer()
        
        for word in self._current_words:
            word.move_next()

        self._random_spawn()


    def _do_outputs(self):
        """uh"""
        self._output_service.clear_screen() #remove this line for free epilepsy
        self._output_service.draw_actor(self._score_board)
        self._output_service.draw_actor(self._buffer)

        for word in self._current_words:
            self._output_service.draw_actor(word)
        self._output_service.flush_buffer()

    def _spawn_word(self):
        """
        adds random instance of Word to (constants.MAX_X)_current_words
        """
        random_word_index = randint(0, len(self._word_bank) - 1)
        random_word = self._word_bank[random_word_index]
        new_word = Word(random_word)
        self._current_words.append(new_word)

    def _starting_wordspawn(self):
        for i in range(5):
            self._spawn_word()

    def _random_spawn(self):
        """spawns at random based on current points """
        spawn_chance = constants.STARTING_SPAWN_RATE + self._score_board._points
        if spawn_chance > randint(0, constants.SPAWNRATE_FACTOR):
            self._spawn_word()

    def _get_wordbank(self):
        for word in constants.LIBRARY:
            self._word_bank.append(word.strip())
        # base_path = Path(__file__).parent
        # file_path = (base_path / f"../game/words.txt").resolve()
        # with open(file_path, "rt") as infile:
        #     for line in infile:
        #         self._word_bank.append(line.strip())

    def _is_dead(self, word):
        """ returns false if word is not at left side of screen 
        TAKES WORD CLASS AS PARAMETER, NOT STRING
        """
        position = word.get_position()
        if position.get_x() <= 2:
            return True
        else:
            return False

    def _is_contained(self, word):
        """
        returns true if word is in buffer
        Takes class not string
        """
        string = word.get_word()
        buffer = self._buffer.get_buffer()
        if string in buffer:
            return True
        else:
            return False

    def _spawn_debug_word(self):
        self._current_words.append(Word("asdf"))