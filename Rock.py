from Coordinates import Coordinates
from Entity import Entity


class Rock(Entity):
    def __init__(self, coordinates: Coordinates) -> None:
        super().__init__(coordinates)
