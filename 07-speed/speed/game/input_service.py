import sys
from game.point import Point
import raylibpy

class InputService:
    """
    we need to change this to get keys and maybe pput them on the box on the bottom? or maybe that's an outputservice

    Stereotype: 
        Service Provider

    Attributes:
        
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._current = Point(10, 0)
        
    def get_direction(self):
        """Gets the selected direction. If one hasn't been selected the last 
        one is returned.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        
        if self.is_left_pressed():
            self._current = Point(-10, 0)
        elif self.is_right_pressed():
            self._current = Point(10, 0)
        elif self.is_up_pressed():
            self._current = Point(0, -10)
        elif self.is_down_pressed():
            self._current = Point(0, 10)

        return self._current

    def get_key_press(self):
        """
        we probably need to filter the keys to be only regular letters
        """
        key_int = raylibpy.get_key_pressed()

        key_string = None

        if key_int != -1:
            key_string = chr(key_int)
        
        return key_string

    def is_left_pressed(self):
        """
        Determines if the left key is currently being pushed
        """
        return raylibpy.is_key_down(raylibpy.KEY_LEFT)

    def is_right_pressed(self):
        """
        Determines if the right key is currently being pushed
        """
        return raylibpy.is_key_down(raylibpy.KEY_RIGHT)

    def is_up_pressed(self):
        """
        Determines if the up key is currently being pushed
        """
        return raylibpy.is_key_down(raylibpy.KEY_UP)

    def is_down_pressed(self):
        """
        Determines if the down key is currently being pushed
        """
        return raylibpy.is_key_down(raylibpy.KEY_DOWN)

    def window_should_close(self):
        """
        Determines if the user is trying to close the window
        """
        return raylibpy.window_should_close()
