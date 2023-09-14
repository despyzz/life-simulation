from entities.Entity import Entity
from simulation.Coordinates import Coordinates


class Map:
    def __init__(self, entries=None) -> None:
        if entries is None:
            self.__entities = dict()
        elif isinstance(entries, dict):
            self.__entities = entries

    @property
    def entities(self) -> dict:
        return dict(self.__entities)

    def __copy__(self) -> object:
        return Map(self.__entities)

    def pop_from(self, coordinates: Coordinates) -> Entity:
        if coordinates not in self.__entities.keys():
            raise ValueError
        entity = self.__entities.pop(coordinates)
        return entity

    def set_to(self, coordinates: Coordinates, entity: Entity) -> None:
        if coordinates in self.__entities.keys():
            raise ValueError
        self.__entities[coordinates] = entity
