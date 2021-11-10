import random
from game.actor import Actor
from game.point import Point

class Life(Actor):
    """Points earned. The responsibility of the ScoreBoard is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (Score): an instance of Score.
        """
        super().__init__()
        self._life = 10
        position = Point(200, 0)
        self.set_position(position)
        self.set_text(f"Life: {self._life}")
    
    def add_life(self, life):
        """Adds the given points to the running total and updates the text.
        
        Args:
            self (Score): An instance of Score.
            points (integer): The points to add.
        """
        self._life += life
        self.set_text(f"Life: {self._life}")

    def get_life(self):
        return self._life