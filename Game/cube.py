import numpy as np
from Side.side import Side
from Side.side3x3 import Side3x3
import random


class Cube:
    """Stores sides for the cubes."""

    def __init__(
        self,
        front: Side3x3,
        back: Side3x3,
        left: Side3x3,
        right: Side3x3,
        up: Side3x3,
        down: Side3x3,
    ) -> None:
        """Initialize the cube.
        Turn side 3x3 objects into side objects (5x5)."""
        self.front: Side = self.__getFront(
            front=front, left=left, right=right, up=up, down=down
        )
        self.back: Side = self.__getBack(
            back=back, left=left, right=right, up=up, down=down
        )
        self.left: Side = self.__getLeft(
            left=left, back=back, up=up, down=down, front=front
        )
        self.right: Side = self.__getRight(
            right=right, back=back, up=up, down=down, front=front
        )
        self.up: Side = self.__getUp(
            up=up, right=right, back=back, front=front, left=left
        )
        self.down: Side = self.__getDown(
            down=down, right=right, back=back, front=front, left=left
        )

    def randomize(self, number_of_times_randomize) -> None:
        """Randomize the cube."""
        for _ in range(number_of_times_randomize):
            side = random.choice(
                [self.front, self.back, self.left, self.right, self.up, self.down]
            )
            random.choice([side.rotateClockwise, side.rotateCounterClockwise])()

    def __getFront(
        self, front: Side3x3, left: Side3x3, right: Side3x3, up: Side3x3, down: Side3x3
    ):
        """Return 5x5 Side for front."""
        first_row = np.array(
            [None, up.getRow(2)[0], up.getRow(2)[1], up.getRow(2)[2], None]
        )
        second_row = np.array([left.getCol(2)[0], *front.getRow(0), right.getCol(0)[0]])
        third_row = np.array([left.getCol(2)[1], *front.getRow(1), right.getCol(0)[1]])
        fourth_row = np.array([left.getCol(2)[2], *front.getRow(2), right.getCol(0)[2]])
        fifth_row = np.array([None, *down.getRow(2), None])
        return Side(first_row, second_row, third_row, fourth_row, fifth_row)

    def __getBack(
        self, back: Side3x3, left: Side3x3, right: Side3x3, up: Side3x3, down: Side3x3
    ):
        """Return 5x5 Side for back."""
        first_row = np.array(
            [None, up.getRow(0)[2], up.getRow(0)[1], up.getRow(0)[0], None]
        )
        second_row = np.array([right.getCol(2)[0], *back.getRow(0), left.getCol(0)[0]])
        third_row = np.array([right.getCol(2)[1], *back.getRow(1), left.getCol(0)[1]])
        fourth_row = np.array([right.getCol(2)[2], *back.getRow(2), left.getCol(0)[2]])
        fifth_row = np.array(
            [None, down.getRow(2)[2], down.getRow(2)[1], down.getRow(2)[0], None]
        )
        return Side(first_row, second_row, third_row, fourth_row, fifth_row)

    def __getLeft(
        self, left: Side3x3, back: Side3x3, up: Side3x3, down: Side3x3, front: Side3x3
    ):
        """Return 5x5 Side for left."""
        first_row = np.array([None, *up.getCol(0), None])
        second_row = np.array([back.getCol(2)[0], *left.getRow(0), front.getCol(0)[0]])
        third_row = np.array([back.getCol(2)[1], *left.getRow(1), front.getCol(0)[1]])
        fourth_row = np.array([back.getCol(2)[2], *left.getRow(2), front.getCol(0)[2]])
        fifth_row = np.array(
            [None, down.getCol(0)[2], down.getCol(0)[1], down.getCol(0)[0], None]
        )
        return Side(first_row, second_row, third_row, fourth_row, fifth_row)

    def __getRight(
        self, right: Side3x3, back: Side3x3, up: Side3x3, down: Side3x3, front: Side3x3
    ):
        """Return 5x5 Side for right."""
        first_row = np.array(
            [None, up.getCol(2)[2], up.getCol(2)[1], up.getCol(2)[0], None]
        )
        second_row = np.array([front.getCol(2)[0], *right.getRow(0), back.getCol(0)[0]])
        third_row = np.array([front.getCol(2)[1], *right.getRow(1), back.getCol(0)[1]])
        fourth_row = np.array([front.getCol(2)[2], *right.getRow(2), back.getCol(0)[2]])
        fifth_row = np.array([None, *down.getCol(2), None])
        return Side(first_row, second_row, third_row, fourth_row, fifth_row)

    def __getUp(
        self, up: Side3x3, right: Side3x3, back: Side3x3, front: Side3x3, left: Side3x3
    ):
        """Return 5x5 Side for up"""
        first_row = np.array(
            [None, back.getRow(0)[2], back.getRow(0)[1], back.getRow(0)[0], None]
        )
        second_row = np.array([left.getRow(0)[0], *up.getRow(0), right.getRow(0)[2]])
        third_row = np.array([left.getRow(0)[1], *up.getRow(1), right.getRow(0)[1]])
        fourth_row = np.array([left.getRow(0)[2], *up.getRow(2), right.getRow(0)[0]])
        fifth_row = np.array([None, *front.getRow(0), None])
        return Side(first_row, second_row, third_row, fourth_row, fifth_row)

    def __getDown(
        self,
        down: Side3x3,
        right: Side3x3,
        back: Side3x3,
        front: Side3x3,
        left: Side3x3,
    ):
        """RReturn 5x5 Side for down."""
        first_row = np.array(
            [None, back.getRow(2)[2], back.getRow(2)[1], back.getRow(2)[0], None]
        )
        second_row = np.array([left.getRow(2)[0], *down.getRow(2), right.getRow(2)[2]])
        third_row = np.array([left.getRow(2)[1], *down.getRow(1), right.getRow(2)[1]])
        fourth_row = np.array([left.getRow(2)[2], *down.getRow(0), right.getRow(2)[0]])
        fifth_row = np.array([None, *front.getRow(2), None])
        return Side(first_row, second_row, third_row, fourth_row, fifth_row)
