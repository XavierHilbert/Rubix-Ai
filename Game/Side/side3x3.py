import numpy as np
from Side.SideParent import SideParent
from Color.color import Color
import copy


class Side3x3(SideParent):
    """Has the following Representation (C is color enum):
    C C C
    C C C
    C C C"""

    def __init__(self, first_row, second_row, third_row):
        super().__init__(np.array([first_row, second_row, third_row], dtype=Color))

    def rotateCounterClockwise(self):
        """Rotates the side counter clockwise."""
        new_arr = copy.deepcopy(np.rot90(self.side, 1))
        self.__dict__.update(Side3x3(*new_arr).__dict__)

    def rotateClockwise(self):
        """Rotates the side clockwise."""
        new_arr = np.rot90(self.side, -1)
        self.__dict__.update(Side3x3(*new_arr).__dict__)
