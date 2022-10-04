import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import mpl_toolkits.mplot3d.art3d as art3d
from Color.colors_enum import Colors_Enum
from matplotlib.widgets import Button
import time

BUTTON_WIDTH = 1 / 6.0  # evenly distribute buttons


class Visualizer:
    """Visualizer for the cube."""

    colors = {
        Colors_Enum.WHITE: "w",
        Colors_Enum.RED: "r",
        Colors_Enum.BLUE: "b",
        Colors_Enum.GREEN: "g",
        Colors_Enum.ORANGE: "orange",
        Colors_Enum.YELLOW: "y",
    }

    def __init__(self) -> None:
        """Initializes the visualizer."""
        # Init 3d cube
        self.fig = plt.figure(figsize=(9, 9))
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.ax.set_xlim(0, 3)
        self.ax.set_ylim(0, 3)
        self.ax.set_zlim(0, 3)
        self.ax.set_aspect("auto")
        self.ax.set_autoscale_on(True)
        plt.ylabel("Front")
        plt.xlabel("Left")
        self.ax.xaxis.set_ticklabels([])
        self.ax.yaxis.set_ticklabels([])
        self.ax.zaxis.set_ticklabels([])
        self.fig.canvas.set_window_title("Rubix Cube")
        self.ax.view_init(24, -9)

        self.frontRotateClockWise = self.fig.add_axes([0, 0, BUTTON_WIDTH, 0.075])
        self.bFrontRotateClockWise = Button(self.frontRotateClockWise, "F ClockWise")
        self.frontRotateCounterClockWise = self.fig.add_axes(
            [0, 0.075, BUTTON_WIDTH, 0.075]
        )
        self.bFrontRotateCounterClockWise = Button(
            self.frontRotateCounterClockWise, "F CounterClockWise"
        )

        self.backRotateClockWise = self.fig.add_axes(
            [BUTTON_WIDTH, 0, BUTTON_WIDTH, 0.075]
        )
        self.bBackRotateClockWise = Button(self.backRotateClockWise, "B ClockWise")

        self.backRotateCounterClockWise = self.fig.add_axes(
            [BUTTON_WIDTH, 0.075, BUTTON_WIDTH, 0.075]
        )
        self.bBackRotateCounterClockWise = Button(
            self.backRotateCounterClockWise, "B CounterClockWise"
        )

        self.leftRotateClockWise = self.fig.add_axes(
            [2 * BUTTON_WIDTH, 0, BUTTON_WIDTH, 0.075]
        )
        self.bLeftRotateClockWise = Button(self.leftRotateClockWise, "L ClockWise")

        self.leftRotateCounterClockWise = self.fig.add_axes(
            [2 * BUTTON_WIDTH, 0.075, BUTTON_WIDTH, 0.075]
        )
        self.bLeftRotateCounterClockWise = Button(
            self.leftRotateCounterClockWise, "L CounterClockWise"
        )

        self.rightRotateClockWise = self.fig.add_axes(
            [3 * BUTTON_WIDTH, 0, BUTTON_WIDTH, 0.075]
        )
        self.bRightRotateClockWise = Button(self.rightRotateClockWise, "R ClockWise")

        self.rightRotateCounterClockWise = self.fig.add_axes(
            [3 * BUTTON_WIDTH, 0.075, BUTTON_WIDTH, 0.075]
        )
        self.bRightRotateCounterClockWise = Button(
            self.rightRotateCounterClockWise, "R CounterClockWise"
        )

        self.upRotateClockWise = self.fig.add_axes(
            [4 * BUTTON_WIDTH, 0, BUTTON_WIDTH, 0.075]
        )
        self.bUpRotateClockWise = Button(self.upRotateClockWise, "U ClockWise")

        self.upRotateCounterClockWise = self.fig.add_axes(
            [4 * BUTTON_WIDTH, 0.075, BUTTON_WIDTH, 0.075]
        )
        self.bUpRotateCounterClockWise = Button(
            self.upRotateCounterClockWise, "U CounterClockWise"
        )

        self.downRotateClockWise = self.fig.add_axes(
            [5 * BUTTON_WIDTH, 0, BUTTON_WIDTH, 0.075]
        )
        self.bDownRotateClockWise = Button(self.downRotateClockWise, "D ClockWise")

        self.downRotateCounterClockWise = self.fig.add_axes(
            [5 * BUTTON_WIDTH, 0.075, BUTTON_WIDTH, 0.075]
        )
        self.bDownRotateCounterClockWise = Button(
            self.downRotateCounterClockWise, "D CounterClockWise"
        )

    def render(self, cube, hasWon: bool, number_of_moves: int):
        """renders game after every move"""
        with plt.ion():
            self.ax.patches.clear()
            self.__renderBack(cube)
            self.__renderFront(cube)
            self.__renderLeft(cube)
            self.__renderRight(cube)
            self.__renderDown(cube)
            self.__renderUp(cube)
            plt.title(
                label=f"{number_of_moves} moves",
                transform=self.ax.transAxes,
                loc="center",
                fontstyle="normal",
            )
            if hasWon:
                plt.suptitle(
                    f"Solved!",
                    fontstyle="italic",
                    color="green",
                    transform=self.ax.transAxes,
                )
            else:
                plt.suptitle("")

    def firstRender(self, cube, hasWon: bool, number_of_moves: int, delay: int):
        """Renders when game first starts"""
        self.__renderBack(cube)
        self.__renderFront(cube)
        self.__renderLeft(cube)
        self.__renderRight(cube)
        self.__renderDown(cube)
        self.__renderUp(cube)

        plt.title(
                label=f"{number_of_moves} moves",
                transform=self.ax.transAxes,
                loc="center",
                fontstyle="normal",
            )
        if hasWon:
            plt.suptitle(
                f"Solved!",
                fontstyle="italic",
                color="green",
                transform=self.ax.transAxes,
            ) 
        else:
            plt.suptitle("")
        
        if delay > 0:
            plt.pause(1)
        else: 
            plt.show()
        
        

    def __renderBack(self, cube):
        """Renders back side of cube."""
        for i in range(3):
            for j in range(3):
                side = Rectangle(
                    (2 - j, 2 - i),
                    1,
                    1,
                    lw=0.5,
                    edgecolor="black",
                    facecolor=self.colors.get(cube.back.get3x3()[i][j].getColor()),
                )
                self.ax.add_patch(side)
                art3d.pathpatch_2d_to_3d(side, z=0, zdir="x")

    def __renderFront(self, cube):
        """Renders front side of cube."""
        for j in range(3):
            for i in range(3):
                side = Rectangle(
                    (i, 2 - j),
                    1,
                    1,
                    lw=0.5,
                    edgecolor="black",
                    facecolor=self.colors.get(cube.front.get3x3()[j][i].getColor()),
                )
                self.ax.add_patch(side)
                art3d.pathpatch_2d_to_3d(side, z=3, zdir="x")

    def __renderLeft(self, cube):
        """Renders left side of cube."""
        for j in range(3):
            for i in range(3):
                side = Rectangle(
                    (i, 2 - j),
                    1,
                    1,
                    lw=0.5,
                    edgecolor="black",
                    facecolor=self.colors.get(cube.left.get3x3()[j][i].getColor()),
                )
                self.ax.add_patch(side)
                art3d.pathpatch_2d_to_3d(side, z=0, zdir="y")

    def __renderRight(self, cube):
        """Renders right side of cube."""
        for i in range(3):
            for j in range(3):
                side = Rectangle(
                    (2 - j, 2 - i),
                    1,
                    1,
                    lw=0.5,
                    edgecolor="black",
                    facecolor=self.colors.get(cube.right.get3x3()[i][j].getColor()),
                )
                self.ax.add_patch(side)
                art3d.pathpatch_2d_to_3d(side, z=3, zdir="y")

    def __renderDown(self, cube):
        """Renders down side of cube."""
        for j in range(3):
            for i in range(3):
                side = Rectangle(
                    (2 - i, j),
                    1,
                    1,
                    lw=0.5,
                    edgecolor="black",
                    facecolor=self.colors.get(cube.down.get3x3()[i][j].getColor()),
                )
                self.ax.add_patch(side)
                art3d.pathpatch_2d_to_3d(side, z=0, zdir="z")

    def __renderUp(self, cube):
        """Renders up side of cube."""
        for j in range(3):
            for i in range(3):
                side = Rectangle(
                    (i, j),
                    1,
                    1,
                    lw=0.5,
                    edgecolor="black",
                    facecolor=self.colors.get(cube.up.get3x3()[i][j].getColor()),
                )
                self.ax.add_patch(side)
                art3d.pathpatch_2d_to_3d(side, z=3, zdir="z")
