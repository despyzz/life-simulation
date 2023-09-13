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

    def pop_from(self, coordinates: Coordinates):