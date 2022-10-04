from visualizer import Visualizer
from Controller import Controller
from model import Model
from cube import Cube
from Side.side3x3 import Side3x3
from Color.colors_enum import Colors_Enum
from Color.color import Color


class runCubeGame:
    """Create a new cube env."""

    def __init__(self, number_of_times_randomize=1, visualize = True , delay = 0) -> None:
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

        if visualize: 
            self.visualizer = Visualizer()
        else:
            self.visualizer = None
        self.model = Model(
            visualizer=self.visualizer,
            cube=c,
            number_of_times_randomize=number_of_times_randomize,
        )   
        if visualize:
            self.controller = Controller(model=self.model, visualizer=self.visualizer)
            self.model.firstRender(delay)