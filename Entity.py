from abc import ABC
from Coordinates import Coordinates


class Entity(ABC):
    def __init__(self, coordinates: Coordinates) -> None:
        if isinstance(coordinates, Coordinates):
            self.coordinates = coordinates
        else:
            raise TypeError

    @property
    def coordinates(self) -> Coordinates:
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, value: Coordinates) -> None:
        if isinstance(value, Coordinates):
            self.__coordinates = value
        else:
            raise TypeError
