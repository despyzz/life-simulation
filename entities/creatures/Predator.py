from entities.creatures.Creature import Creature
from entities.creatures.Herbivore import Herbivore


class Predator(Creature):
    @staticmethod
    def get_vision_range() -> int:
        return 4

    @staticmethod
    def get_food_type():
        return Herbivore

    def __init__(self) -> None:
        super().__init__()
