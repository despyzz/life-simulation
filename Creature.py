from abc import ABC

from Coordinates import Coordinates
from Entity import Entity


class Creature(Entity, ABC):
    def __init__(self, coordinates: Coordinates) -> None:
        super().__init__(coordinates)

    def move_to(self, coordinates: Coordinates) -> None:
        self.__init__(coordinates)