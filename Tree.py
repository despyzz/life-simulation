from Coordinates import Coordinates
from Entity import Entity


class Tree(Entity):
    def __init__(self, coordinates: Coordinates) -> None:
        super().__init__(coordinates)
