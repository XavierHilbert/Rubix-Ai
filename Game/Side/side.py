import numpy as np
from Color.color import Color
import copy
from Side.SideParent import SideParent


class Side(SideParent):
    """Has the following Representation
    (N is None and C is color enum):
    N C C C N
    C C C C C
    C C C C C
    C C C C C
    N C C C N"""

    def __init__(self, first_row, second_row, third_row, fourth_row, fifth_row):
        super().__init__(
            np.array(
                [first_row, second_row, third_row, fourth_row, fifth_row], dtype=Color
            )
        )

    def rotateCounterClockwise(self):
        """Rotates the side counter clockwise."""
        new_arr = copy.deepcopy(np.rot90(self.side, 1))
        super().updateColor(new_arr)

    def rotateClockwise(self):
        """Rotates the side clockwise."""
        new_arr = copy.deepcopy(np.rot90(self.side, -1))
        super().updateColor(new_arr)

    def get3x3(self):
        """Returns the 3x3 array of the side."""
        return self.side[1:4, 1:4]

    def oneColor(self):
        """Returns true if side is one color."""
        side3x3 = self.get3x3()
        color = side3x3[0][0]
        for row in side3x3:
            for col in row:
                if col != color:
                    return False
        return True
