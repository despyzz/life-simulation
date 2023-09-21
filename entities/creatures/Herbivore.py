from entities.creatures.Creature import Creature
from entities.environment.Grass import Grass


class Herbivore(Creature):
    @staticmethod
    def get_vision_range() -> int:
        return 3

    @staticmethod
    def get_food_type():
        return Grass

    def __init__(self) -> None:
        super().__init__()
