import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here...

class Food(Actor):
    def __init__(self):
        super().__init__()
        self.set_width(constants.DEFAULT_SQUARE_LENGTH)
        self.set_height(constants.DEFAULT_SQUARE_LENGTH)
        self._points = 0
        self.reset()

        
    def get_points(self):
        return self._points
    
    def reset(self):
        x = random.randint(0,constants.MAX_X)
        y = random.randint(0,(constants.MAX_Y - (constants.MAX_Y/10)))
        self.set_position(Point(x,y))
        self._points = random.randint(1,10)
        self.set_text(str(self._points))
    

