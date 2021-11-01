import os

MAX_X = 60
MAX_Y = 20
FRAME_LENGTH = 0.08
STARTING_WORDS = 5
PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()

DEFAULT_WORD_HEIGHT = 20
DEFAULT_WORD_SPEED = -1

STARTING_SPAWN_RATE = 30
SPAWNRATE_FACTOR = 1000
