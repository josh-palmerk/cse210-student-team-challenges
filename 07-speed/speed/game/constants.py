import os
""" App Config """
MAX_X = 900
MAX_Y = 600
FRAME_LENGTH = 0.08
FRAME_RATE = 30

""" Wordbank """
PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()

""" Formatting """
DEFAULT_WORD_HEIGHT = 20
DEFAULT_FONT_SIZE = 22
DEFAULT_TEXT_OFFSET = 5


""" GAme RUles"""
# Snake Rules indicated by S_
S_SNAKE_IS_ON = True
S_DO_WORDS_EXPIRE = True
S_DO_WORDS_SUBTRACT = True

S_STARTING_SPAWN_RATE = 45 
S_SPAWNRATE_FACTOR = 18000 # smaller number = more spawns
S_BONUS_WORD_CHANCE = 4 # chance is 1 in x

# Words Rules indicated by W_
W_SNAKE_IS_ON = False
W_DO_WORDS_EXPIRE = True
W_DO_WORDS_SUBTRACT = True

W_STARTING_SPAWN_RATE = 75 
W_SPAWNRATE_FACTOR = 13000 # smaller number = more spawns
W_BONUS_WORD_CHANCE = 4 # chance is 1 in x


""" Game Balance """
STARTING_WORDS = 5
DEFAULT_WORD_SPEED = -1


""" Hello Snake """
SNAKE_LENGTH = 10
DEFAULT_SQUARE_LENGTH = 20
SNAKE_VELOCITY = 6
