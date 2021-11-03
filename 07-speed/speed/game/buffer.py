from game.actor import Actor
from game.point import Point
import game.constants as constants

class Buffer(Actor):
    """ This is an information class. This holds the inputs from the user and displyas it """
    def __init__(self):
        self._typed_string = ""
        self.set_height(constants.MAX_Y - constants.DEFAULT_WORD_HEIGHT)
        self.set_width(constants.MAX_X) 
        self.set_position(Point((constants.MAX_X), (0)))

    def clear_buffer(self):
        """Clears the Buffer List"""
        self._typed_string = ""

    def get_buffer(self):
        """Getter method"""
        return self._typed_string      

    def add_character_to_buffer(self, character):
        """Changes the typed string to be able to output """
        self._typed_string = (self._typed_string + character)