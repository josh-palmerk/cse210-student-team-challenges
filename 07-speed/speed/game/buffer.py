from game.actor import Actor
from game.point import Point
import game.constants as constants

class Buffer(Actor):
    """ This is an information class. This holds the inputs from the user and displyas it """
    def __init__(self):
        super().__init__()
        self.set_text("")
        self.set_height(constants.DEFAULT_WORD_HEIGHT)
        self.set_width(constants.DEFAULT_FONT_SIZE * len(self.get_text())) 
        self.set_position(Point(10, constants.MAX_Y - (constants.DEFAULT_FONT_SIZE * 2)))#Point((constants.MAX_X / 2), (constants.MAX_Y / 2)))

    def clear_buffer(self):
        """Clears the Buffer List"""
        self.set_text("")

    def get_buffer(self):
        """Getter method"""
        return self.get_text()      

    def add_character_to_buffer(self, character):
        """Changes the typed string to be able to output """
        if character is not None:
            self.set_text(self.get_text() + character)