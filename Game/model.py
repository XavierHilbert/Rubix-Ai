import numpy as np
from Side.side3x3 import Side3x3
from Color.colors_enum import Colors_Enum
from Color.color import Color
import random
from cube import Cube
from visualizer import Visualizer
import numpy as np
from functools import lru_cache


class Model:
    """Contains state of the game."""

    def __init__(
        self, cube: Cube, visualizer: Visualizer, number_of_times_randomize
    ) -> None:
        self.cube = cube
        self.cube.randomize(number_of_times_randomize=number_of_times_randomize)
        self.number_of_moves = 0
        self.visualizer = visualizer

    def __render(self):
        """Update the game. Should be called on all changes.
        Check if has won, if so display.
        call update on visualizer."""
        self.number_of_moves += 1
        self.visualizer.render(
            cube=self.cube, hasWon=self.hasWon(), number_of_moves=self.number_of_moves
        )

    def firstRender(self, delay):
        """Update the game. Should be called on all changes.
        Check if has won, if so display.
        call update on visualizer."""
        self.visualizer.firstRender(cube=self.cube, hasWon=self.hasWon(), number_of_moves=self.number_of_moves, delay= delay)

    def hasWon(self):
        """Return true if the back has been solved."""
        # self.face_to_solve == self.cube.back.get3x3()
        return (
            self.cube.back.oneColor()
            and self.cube.front.oneColor()
            and self.cube.left.oneColor()
            and self.cube.right.oneColor()
            and self.cube.up.oneColor()
            and self.cube.down.oneColor()
        )

    def rotateFrontClockwise(self, _):
        """Rotates the front side of the cube clock wise by 90 degrees."""
        self.cube.front.rotateClockwise()
        self.__render()

    def rotateFrontCounterClockwise(self, _):
        """Rotates the front side of the cube counter clock wise by 90 degrees."""
        self.cube.front.rotateCounterClockwise()
        self.__render()

    def rotateBackClockwise(self, _):
        """Rotates the back side of the cube clock wise by 90 degrees."""
        self.cube.back.rotateClockwise()
        self.__render()

    def rotateBackCounterClockwise(self, _):
        """Rotates the back side of the cube counter clock wise by 90 degrees."""
        self.cube.back.rotateCounterClockwise()
        self.__render()

    def rotateUpClockwise(self, _):
        """Rotates the up side of the cube clock wise by 90 degrees."""
        self.cube.up.rotateClockwise()
        self.__render()

    def rotateUpCounterClockwise(self, _):
        """Rotates the up side of the cube counter clock wise by 90 degrees."""
        self.cube.up.rotateCounterClockwise()
        self.__render()

    def rotateDownClockwise(self, _):
        """Rotates the down side of the cube clock wise by 90 degrees."""
        self.cube.down.rotateClockwise()
        self.__render()

    def rotateDownCounterClockwise(self, _):
        """Rotates the down side of the cube counter clock wise by 90 degrees."""
        self.cube.down.rotateCounterClockwise()
        self.__render()

    def rotateRightClockwise(self, _):
        """Rotates the right side of the cube clock wise by 90 degrees."""
        self.cube.right.rotateClockwise()
        self.__render()

    def rotateRightCounterClockwise(self, _):
        """Rotates the right side of the cube counter clock wise by 90 degrees."""
        self.cube.right.rotateCounterClockwise()
        self.__render()

    def rotateLeftClockwise(self, _):
        """Rotates the left side of the cube clock wise by 90 degrees."""
        self.cube.left.rotateClockwise()
        self.__render()

    def rotateLeftCounterClockwise(self, _):
        """Rotates the left side of the cube counter clock wise by 90 degrees."""
        self.cube.left.rotateCounterClockwise()
        self.__render()
