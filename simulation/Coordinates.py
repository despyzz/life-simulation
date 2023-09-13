class Coordinates:

    def __init__(self, x: int, y: int) -> None:
        if isinstance(x, int):
            self.__x = x
        else:
            raise TypeError
        if isinstance(y, int):
            self.__y = y
        else:
            raise TypeError

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __eq__(self, other) -> bool:
        if isinstance(other, Coordinates):
            return self.x == other.x and self.y == other.y
        else:
            raise TypeError

    def __hash__(self) -> int:
        return hash((self.x, self.y))
