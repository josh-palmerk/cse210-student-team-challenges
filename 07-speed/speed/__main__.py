import os
from raylibpy import RAYLIB_BIN_PATH # this appeared automatically lol idk if itll throw errors
os.environ[RAYLIB_BIN_PATH] = "."


from game.director import Director
from game.input_service import InputService
from game.output_service import OutputService


def main(screen):
    input_service = InputService(screen)
    output_service = OutputService(screen)
    director = Director(input_service, output_service)
    director.start_game()

if __name__ == "__main__":
    main()
