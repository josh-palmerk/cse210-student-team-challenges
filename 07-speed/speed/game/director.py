import raylibpy

from game import constants

from game.score_board import ScoreBoard

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
        # add more attributes and instances based on game needs