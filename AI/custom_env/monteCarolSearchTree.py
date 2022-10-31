from email import policy
import sys
sys.path.insert(0, "/Users/xavierh/Rubix Cube Solve Fully/Game")
from runCubeGame import runCubeGame
import numpy as np
from copy import deepcopy


def dummy_model(game):
    """Returns a dummy model that does nothing."""
    value_head = .5
    policy_head = np.array([1/12] * 12, dtype=np.float32)
    return value_head, policy_head

class Node: 
    def __init__(self, prior, game, state):
        self.prior = prior
        self.state = state
        self.game = deepcopy(game)
        self.children = {}
        self.value = 0
    
    def expand(self, action_probs):
        for action, prob in enumerate(action_probs):
            if prob > 0:
                game_copy = deepcopy(self.game)
                self.preform_action(game_copy, action)
                new_state = get_observation(self.state)
                self.children[action] = Node(prob, game, new_state)
    
    def preform_action(self, action):
        """Preforms action on stored cube."""
        if action == 0:
            self.game.model.rotateLeftCounterClockwise(None)
        elif action == 1:
            self.game.model.rotateLeftClockwise(None)
        elif action == 2:
            self.game.model.rotateRightCounterClockwise(None)
        elif action == 3:
            self.game.model.rotateRightClockwise(None)
        elif action == 4:
            self.game.model.rotateUpCounterClockwise(None)
        elif action == 5:
            self.game.model.rotateUpClockwise(None)
        elif action == 6:
            self.game.model.rotateDownCounterClockwise(None)
        elif action == 7:
            self.game.model.rotateDownClockwise(None)
        elif action == 8:
            self.game.model.rotateFrontCounterClockwise(None)
        elif action == 9:
            self.game.model.rotateFrontClockwise(None)
        elif action == 10:
            self.game.model.rotateBackCounterClockwise(None)
        elif action == 11:
            self.game.model.rotateBackClockwise(None)

    
def get_observation(game):
    """Returns a 54 element vector representing the cube."""
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

    return np.array(side_vector, dtype=np.float32)


if __name__ == "__main__":
    value, action_probs = dummy_model(None)
    game = runCubeGame()
    root = Node(prior=0, game=game, state=get_observation(game))
    root.expand(action_probs)

    root.children[0]


