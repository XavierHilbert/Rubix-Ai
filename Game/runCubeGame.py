from visualizer import Visualizer
from Controller import Controller
from model import Model
from cube import Cube
from Side.side3x3 import Side3x3
from Color.colors_enum import Colors_Enum
from Color.color import Color


class runCubeGame:
    """Create a new cube env."""

    def __init__(self, number_of_times_randomize=1) -> None:
        red = Side3x3(
            [Color(Colors_Enum.RED), Color(Colors_Enum.RED), Color(Colors_Enum.RED)],
            [Color(Colors_Enum.RED), Color(Colors_Enum.RED), Color(Colors_Enum.RED)],
            [Color(Colors_Enum.RED), Color(Colors_Enum.RED), Color(Colors_Enum.RED)],
        )

        blue = Side3x3(
            [Color(Colors_Enum.BLUE), Color(Colors_Enum.BLUE), Color(Colors_Enum.BLUE)],
            [Color(Colors_Enum.BLUE), Color(Colors_Enum.BLUE), Color(Colors_Enum.BLUE)],
            [Color(Colors_Enum.BLUE), Color(Colors_Enum.BLUE), Color(Colors_Enum.BLUE)],
        )

        yellow = Side3x3(
            [
                Color(Colors_Enum.YELLOW),
                Color(Colors_Enum.YELLOW),
                Color(Colors_Enum.YELLOW),
            ],
            [
                Color(Colors_Enum.YELLOW),
                Color(Colors_Enum.YELLOW),
                Color(Colors_Enum.YELLOW),
            ],
            [
                Color(Colors_Enum.YELLOW),
                Color(Colors_Enum.YELLOW),
                Color(Colors_Enum.YELLOW),
            ],
        )

        green = Side3x3(
            [
                Color(Colors_Enum.GREEN),
                Color(Colors_Enum.GREEN),
                Color(Colors_Enum.GREEN),
            ],
            [
                Color(Colors_Enum.GREEN),
                Color(Colors_Enum.GREEN),
                Color(Colors_Enum.GREEN),
            ],
            [
                Color(Colors_Enum.GREEN),
                Color(Colors_Enum.GREEN),
                Color(Colors_Enum.GREEN),
            ],
        )

        white = Side3x3(
            [
                Color(Colors_Enum.WHITE),
                Color(Colors_Enum.WHITE),
                Color(Colors_Enum.WHITE),
            ],
            [
                Color(Colors_Enum.WHITE),
                Color(Colors_Enum.WHITE),
                Color(Colors_Enum.WHITE),
            ],
            [
                Color(Colors_Enum.WHITE),
                Color(Colors_Enum.WHITE),
                Color(Colors_Enum.WHITE),
            ],
        )

        orange = Side3x3(
            [
                Color(Colors_Enum.ORANGE),
                Color(Colors_Enum.ORANGE),
                Color(Colors_Enum.ORANGE),
            ],
            [
                Color(Colors_Enum.ORANGE),
                Color(Colors_Enum.ORANGE),
                Color(Colors_Enum.ORANGE),
            ],
            [
                Color(Colors_Enum.ORANGE),
                Color(Colors_Enum.ORANGE),
                Color(Colors_Enum.ORANGE),
            ],
        )

        c = Cube(front=red, left=blue, right=green, up=yellow, down=white, back=orange)

        self.visualizer = Visualizer()
        self.model = Model(
            visualizer=self.visualizer,
            cube=c,
            number_of_times_randomize=number_of_times_randomize,
        )
        self.controller = Controller(model=self.model, visualizer=self.visualizer)

    def start(self, delay=0):
        """Start the game."""
        self.model.firstRender(delay)
