import sys

sys.path.insert(0, "Game")
from Game.runCubeGame import runCubeGame

import numpy as np

if __name__ == "__main__":
    game = runCubeGame(0)

    [left, right, front, back, up, down] = [
        game.model.cube.left.get3x3(),
        game.model.cube.right.get3x3(),
        game.model.cube.front.get3x3(),
        game.model.cube.back.get3x3(),
        game.model.cube.up.get3x3(),
        game.model.cube.down.get3x3(),
    ]

    side_vector = np.reshape([left, right, front, back, up, down], (54,))
    side_vector = [element.getColor().value for element in side_vector]

    print(side_vector)

    game.start()
