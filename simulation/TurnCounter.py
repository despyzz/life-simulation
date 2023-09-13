class TurnCounter:
    def __init__(self) -> None:
        self.__counter = 0

    def next_turn(self) -> None:
        self.__counter += 1

    @property
    def counter(self):
        return self.__counter
