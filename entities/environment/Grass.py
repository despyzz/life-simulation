from simulation.Coordinates import Coordinates
from entities.Entity import Entity


class Grass(Entity):
    def __init__(self, coordinates: Coordinates) -> None:
        super().__init__(coordinates)