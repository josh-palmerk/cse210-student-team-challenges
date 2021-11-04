from random import randint
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):
    def __init__(self, word):
        super().__init__()
        
        self._word = word
        self.set_width = len(self._word) * 6 # test value for expanded text box for diff word lengths
        self._points = len(self._word) # words
        self.set_text(f"{self._word}") # word text

        self.set_height = constants.DEFAULT_WORD_HEIGHT
        self.set_position(Point(constants.MAX_X, randint(constants.DEFAULT_FONT_SIZE + 5, (constants.MAX_Y - (constants.DEFAULT_FONT_SIZE * 4)))))
        self.set_velocity(Point(constants.DEFAULT_WORD_SPEED, 0))

    def get_points(self):
        return self._points

    def get_word(self):
        """ in case we need it i guess """
        return self._word
        
    def set_points(self, points):
        self._points = points
