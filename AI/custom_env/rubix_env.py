import sys
import numpy

sys.path.insert(0, "/Users/xavierh/Rubix Cube Solve Fully/Game")
from runCubeGame import runCubeGame
from gym import Env
from gym.spaces import Discrete, Box
import numpy as np

IDEAL_NUMBER_OF_MOVES = 20
DELAY = .0000005
MAX_MOVES_TO_TIMEOUT = 30

class RubixEnv(Env):
    def __init__(self) -> None:
        super(RubixEnv, self).__init__()
        self.action_space = Discrete(12)
        # Color enum values go from 0 to 5
        self.observation_space = Box(low=0, high=5, shape=(54,), dtype=np.float32)

    def step(self, action):
        """Returns observation, reward, done, info"""
        #self.game.start(DELAY) for viszualization
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

        if self.game.model.hasWon():
            self.reward = 100
            self.done = True
        elif self.game.model.number_of_moves == MAX_MOVES_TO_TIMEOUT:
            self.reward = (-self.getSubstringCount() - self.game.model.number_of_moves)*2
            self.done = True
        else: 
            # should punish severely for taking too long
            self.reward = -self.getSubstringCount() - self.game.model.number_of_moves

        self.observation = self.get_observation()
        
        info = {}
        return self.observation, self.reward, self.done, info

    def reset(self, randomize_amount: int = 0):
        self.done = False
        self.game = runCubeGame(randomize_amount, False)
        
        # want to know left, right, up, down, front, back
        self.observation = self.get_observation()
        return self.observation

    def get_observation(self):
        """Returns a 54 element vector representing the cube."""
        [left, right, front, back, up, down] = [
        self.game.model.cube.left.get3x3(),
        self.game.model.cube.right.get3x3(),
        self.game.model.cube.front.get3x3(),
        self.game.model.cube.back.get3x3(),
        self.game.model.cube.up.get3x3(),
        self.game.model.cube.down.get3x3(),
        ]

        side_vector = np.reshape([left, right, front, back, up, down], (54,))
        side_vector = [element.getColor().value for element in side_vector]

        return np.array(side_vector, dtype=np.float32)
        
    def getSubstringCount(self):
        """lower the substrings the better 7 means cube is solved"""
        substrings = 0
        past_ele = -1
        for ele in self.observation:
            if past_ele != ele:
                substrings += 1
                past_ele = ele
        return substrings