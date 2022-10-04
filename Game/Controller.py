from model import Model
from visualizer import Visualizer
from matplotlib.widgets import Button


class Controller:
    """Controller class for the game"""

    def __init__(self, model: Model, visualizer: Visualizer):
        """Initialize the controller."""
        self.model = model
        self.visualizer = visualizer

        # setting buttons with functions
        self.visualizer.bFrontRotateClockWise.on_clicked(
            self.model.rotateFrontClockwise
        )
        self.visualizer.bFrontRotateCounterClockWise.on_clicked(
            self.model.rotateFrontCounterClockwise
        )

        self.visualizer.bBackRotateClockWise.on_clicked(self.model.rotateBackClockwise)
        self.visualizer.bBackRotateCounterClockWise.on_clicked(
            self.model.rotateBackCounterClockwise
        )

        self.visualizer.bLeftRotateClockWise.on_clicked(self.model.rotateLeftClockwise)
        self.visualizer.bLeftRotateCounterClockWise.on_clicked(
            self.model.rotateLeftCounterClockwise
        )

        self.visualizer.bRightRotateClockWise.on_clicked(
            self.model.rotateRightClockwise
        )
        self.visualizer.bRightRotateCounterClockWise.on_clicked(
            self.model.rotateRightCounterClockwise
        )

        self.visualizer.bUpRotateClockWise.on_clicked(self.model.rotateUpClockwise)
        self.visualizer.bUpRotateCounterClockWise.on_clicked(
            self.model.rotateUpCounterClockwise
        )

        self.visualizer.bDownRotateClockWise.on_clicked(self.model.rotateDownClockwise)
        self.visualizer.bDownRotateCounterClockWise.on_clicked(
            self.model.rotateDownCounterClockwise
        )
