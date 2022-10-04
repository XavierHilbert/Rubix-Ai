from Color.colors_enum import Colors_Enum


class Color:
    """Encapsulates a color enum"""

    def __init__(self, color: Colors_Enum):
        """Initialize the color of the object."""
        self.color = color

    def setColor(self, color: Colors_Enum):
        """Set the color of the object."""
        self.color = color

    def getColor(self) -> Colors_Enum:
        """Return the color of the object."""
        return self.color

    def __eq__(self, other):
        """Return true if the colors are equal."""
        return self.color == other.color

    def __str__(self):
        """Return name of color."""
        return self.color.name
