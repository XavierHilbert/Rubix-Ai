import sys

sys.path.insert(0, "Game")
from Game.runCubeGame import runCubeGame

import numpy as np

if __name__ == "__main__":
    game = runCubeGame(30)
    game.start()
