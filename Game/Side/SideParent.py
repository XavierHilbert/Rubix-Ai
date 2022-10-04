from abc import abstractmethod
import numpy as np


class SideParent:
    """Contains all the methods side and side3x3 have in common."""

    def __init__(self, side: np.ndarray):
        self.side = side

    def getSide(self):
        """Return the side."""
        return self.side

    def getRow(self, row_number):
        """Return the row of the side."""
        return self.side[row_number]

    def updateColor(self, new_arr):
        """Updates color of the side given counterClockwise or clockwise function."""
        for row_index in range(len(self.side)):
            for col_index in range(len(self.side[row_index])):
                if self.side[row_index][col_index] is not None:
                    self.side[row_index][col_index].setColor(
                        new_arr[row_index][col_index].getColor()
                    )

    def getCol(self, col_number):
        """Return the column of the side."""
        return self.side[:, col_number]

    def isEqual(self, other):
        """Return true if the sides are equal."""
        try:
            for row_index in range(len(self.side)):
                for col_index in range(len(self.side[row_index])):
                    if self.side[row_index][col_index] is not None:
                        if (
                            self.side[row_index][col_index].getColor()
                            != other.side[row_index][col_index].getColor()
                        ):
                            return False
            return True
        except:
            return False

    def __str__(self):
        """Return the side as a string."""
        side = ""
        for row in self.side:
            for row_index in range(len(row)):
                if row[row_index] is None:
                    side += "N "
                else:
                    side += row[row_index].getColor().name + " "
            side += "\n"
        return side

    @abstractmethod
    def rotateCounterClockwise(self):
        """Rotates the side counter clockwise."""
        pass

    @abstractmethod
    def rotateClockwise(self):
        """Rotates the side clockwise."""
        pass
