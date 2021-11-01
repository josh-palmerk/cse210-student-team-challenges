from random import randint
import raylibpy

from game import constants

from game.score_board import ScoreBoard

from game.word import Word

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
        # add key to current buffer

    def _do_updates(self):
        """
        $$$ check if word reached end of screen
        $$$ handle buffer check & reset
        $$$ add points and remove word if typed
        $$$ spawn new words
        """
        for i in range(len(self._current_words)):
            word = self._current_words[i]
            if self._is_dead(word):
                self._score_board._points -= word._get_points()
            if self._is_contained(word):
                self._score_board._points += word._get_points()
                self._current_words.pop(i)
                # reset buffer
        
        self._random_spawn()


    def _do_outputs(self):
        pass

    def _spawn_word(self):
        """
        adds random instance of Word to _current_words
        """
        new_word =  Word(self._word_bank[randint(0, len(self._word_bank))])
        self._current_words.append(new_word)

    def _starting_wordspawn(self):
        for i in range(5):
            self._spawn_word()

    def _random_spawn(self):
        """spawns at random based on current points """
        spawn_chance = constants.STARTING_SPAWN_RATE + self._score_board._points
        if spawn_chance < randint(0, constants.SPAWNRATE_FACTOR):
            self._spawn_word()

    def _get_wordbank(self):
        with open("words.txt") as infile:
            for line in infile:
                self._word_bank.append(line.strip())

    def _is_dead(self, word):
        """ returns false if word is not at left side of screen 
        TAKES WORD CLASS AS PARAMETER, NOT STRING
        """
        position = word.get_position()
        if position.get_x() == 0:
            return True
        else:
            return False

    def _is_contained(self, word):
        """
        returns true if word is in buffer
        Takes class not string
        """
        string = word.get_word()
        # if string in buffer return true
        #else return false
