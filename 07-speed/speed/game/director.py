from random import randint
from pathlib import Path
import raylibpy
import importlib
from game import constants
from game.score_board import ScoreBoard
from game.word import Word
from game.buffer import Buffer
from game.point import Point
from time import sleep
from game.snake import Snake
from game.food import Food
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


        #YAY! The snake is back
        self._food = Food()
        self._snake = Snake()

        # constants crap defaults to words
        self._snake_is_on = constants.W_SNAKE_IS_ON
        self._do_words_expire = constants.W_DO_WORDS_EXPIRE
        self._do_words_subtract = constants.W_DO_WORDS_SUBTRACT
        self._starting_spawn_rate = constants.W_STARTING_SPAWN_RATE
        self._spawnrate_factor = constants.W_SPAWNRATE_FACTOR
        self._bonus_word_chance = constants.W_BONUS_WORD_CHANCE



    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        print("Starting game... with a snake")

        self._get_wordbank()

        self._output_service.open_window("Speed")

        self._start_screen()

        self._spawn_custom_word("asdf") # remove for finished product

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

        if self._snake_is_on:
            direction = self._input_service.get_direction()
            self._snake.turn_head(direction)

    def _do_updates(self):
        """
        $$$ check if word reached end of screen
        $$$ handle buffer check & reset
        $$$ add points and remove word if typed
        $$$ spawn new words
        """
        self._kill_checker(expire=self._do_words_expire, subtract=self._do_words_subtract)
        
        self._move_words()

        self._random_spawn()

        if self._snake_is_on:
            #Snake?
            self._snake.move()
            self._handle_body_collision()
            self._handle_food_collision()

    def _do_outputs(self):
        """uh"""
        self._output_service.clear_screen() #remove this line for free epilepsy
        self._output_service.draw_actor(self._score_board)
        self._output_service.draw_actor(self._buffer)

        #SNAKE!
        if self._snake_is_on:
            self._output_service.draw_actor(self._food)
            self._output_service.draw_actors(self._snake.get_all())

        for word in self._current_words:
            self._output_service.draw_actor(word)
        self._output_service.flush_buffer()


    def _kill_checker(self, subtract=True, expire=True):
        """"""
        q = 0
        for i in range(len(self._current_words)):
            word = self._current_words[q]
            if self._is_dead(word):
                if subtract:
                    self._score_board.add_points(-word.get_points())
                if expire:
                    self._current_words.pop(q)
                    q -= 1
                if self._score_board.get_points() < 0:
                    print("You ran out of points!")
                    self._keep_playing = False
                    break
            if self._is_contained(word):
                self._score_board.add_points(word.get_points()) 
                self._current_words.pop(q)
                q -= 1
                self._buffer.clear_buffer()
            q += 1

    def _move_words(self):
        for word in self._current_words:
            word.move_next()

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
        """
        Rolls a random number between 0 and constants.SPAWNRATE_FACTOR. If the spawn_chance is greater
        than that number, a word is spawned. On top of that, there is a 1 in constants.BONUS_WORD_CHANCE
        chance that a bonus ord is spawned instead of a regular word.
        Your spawn_chance is determined by your current point score and the starting spawn rate.
        If there are no words onscreen, a word is immediately spawned.
        """
        spawn_chance = self._starting_spawn_rate + (self._score_board._points * 1.5)
        will_spawn = False
        if spawn_chance > randint(0, self._spawnrate_factor):
            will_spawn = True
        elif len(self._current_words) == 0:
            will_spawn = True
        
        if will_spawn:
            if randint(0, self._bonus_word_chance) == 0:
                self._spawn_bonus_word()
            else:
                self._spawn_word()
        
    def _get_wordbank(self):
        for word in constants.LIBRARY:
            self._word_bank.append(word.strip())

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

    def _spawn_custom_word(self, word):
        self._current_words.append(Word(word))

    def _spawn_bonus_word(self):
        """bonus word worth triple points with double speed and maybe red color?"""
        random_word_index = randint(0, len(self._word_bank) - 1)
        random_word = self._word_bank[random_word_index]
        bonus_word = Word(random_word)

        if randint(0, 3) == 0:    # SUPER Word :O
            bonus_word.set_velocity(Point((constants.DEFAULT_WORD_SPEED * 2.5), 4))
            bonus_word.set_points(bonus_word.get_points() * 5)
        else:
            bonus_word.set_velocity(Point((constants.DEFAULT_WORD_SPEED * 2), 0))
            bonus_word.set_points(bonus_word.get_points() * 3)
        # need to add to outputservice to make custom colors and stuff drawable

        self._current_words.append(bonus_word)
        

    # start screen
    def _start_screen(self):
        """"""
        start = False
        self._spawn_custom_word("words")
        self._spawn_custom_word("snake")
        self._current_words[-1].set_velocity(Point(3, 2))
        self._current_words[-2].set_velocity(Point(2, -3))
        self._current_words[-1].set_position(Point(100, 20))
        self._current_words[-2].set_position(Point(15, 15))
        
        while not start:
            self._get_inputs()
            self._kill_checker(subtract=False, expire=False)
            self._move_words()
            self._do_outputs()
            self._output_service.draw_text((constants.MAX_X / 2), (constants.MAX_Y / 2), "WordSnake", True, size=50)
            if len(self._current_words) == 1:
                if self._current_words[-1].get_text() == "words": # checks remaining, so result is backwards
                    self._snake_is_on = constants.S_SNAKE_IS_ON
                    self._do_words_expire = constants.S_DO_WORDS_EXPIRE
                    self._do_words_subtract = constants.S_DO_WORDS_SUBTRACT
                    self._starting_spawn_rate = constants.S_STARTING_SPAWN_RATE
                    self._spawnrate_factor = constants.S_SPAWNRATE_FACTOR
                    self._bonus_word_chance = constants.S_BONUS_WORD_CHANCE
                    self._current_words.pop(-1)
                    start = True
                elif self._current_words[-1].get_text() == "snake":
                    self._current_words.pop(-1)
                    start = True
                




    #SNAAAAAAAAAAAAAANKEEEEEEEEEEEEEEEE!!!!!!!!!!!!!!!
    def _handle_body_collision(self):
        """Handles collisions between the snake's head and body. Stops the game 
        if there is one.

        Args:
            self (Director): An instance of Director.
        """
        head = self._snake.get_head()
        body = self._snake.get_collidable_segments()
        for segment in body:
            if head.get_position().equals(segment.get_position()):
                print("Your snake hit itself!")
                self._keep_playing = False
                break

    def _is_collision(self, first, second):
        x1 = first.get_position().get_x()
        y1 = first.get_position().get_y()
        width1 = first.get_width()
        height1 = first.get_height()

        rectangle1 = raylibpy.Rectangle(x1, y1, width1, height1)

        x2 = second.get_position().get_x()
        y2 = second.get_position().get_y()
        width2 = first.get_width()
        height2 = first.get_height()

        rectangle2 = raylibpy.Rectangle(x2, y2, width2, height2)

        return raylibpy.check_collision_recs(rectangle1, rectangle2)

    def _handle_food_collision(self):
        """Handles collisions between the snake's head and the food. Grows the 
        snake, updates the score and moves the food if there is one.

        Args:
        self (Director): An instance of Director.
        """
        head = self._snake.get_head()
        if self._is_collision(head, self._food):
            # get the amount the food is worth
            points = self._food.get_points()

            # grow the tail by that much
            self._snake.grow_tail(points)

            # add to the score
            self._score_board.add_points(points)

            # get a new food
            self._food.reset() 
