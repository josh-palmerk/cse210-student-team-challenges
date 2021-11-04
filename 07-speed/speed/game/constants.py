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

""" Game Balance """
STARTING_WORDS = 5
DEFAULT_WORD_SPEED = -1

STARTING_SPAWN_RATE = 75 
SPAWNRATE_FACTOR = 13000 # smaller number = more spawns
BONUS_WORD_CHANCE = 4 # chance is 1 in x
