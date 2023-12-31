class GameRules:
    def __init__(self, map_size: int, entities_counts: dict) -> None:
        if 0 < map_size < 20:
            self.__map_size = map_size
        else:
            raise ValueError
        if isinstance(entities_counts, dict):
            self.__entities_counts = entities_counts
        else:
            raise TypeError

    def __copy__(self):
        return GameRules(self.__map_size, self.__entities_counts)

    @property
    def entities_counts(self):
        return dict(self.__entities_counts)

    @property
    def map_size(self):
        return self.__map_size
