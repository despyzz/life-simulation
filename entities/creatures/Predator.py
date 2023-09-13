from simulation.Coordinates import Coordinates
from Creature import Creature


class Predator(Creature):
    def __init__(self, coordinates: Coordinates) -> None:
        super().__init__(coordinates)
