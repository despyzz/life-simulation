from abc import ABC, abstractmethod

from entities.Entity import Entity


class Creature(Entity, ABC):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    @abstractmethod
    def get_food_type():
        pass

    @staticmethod
    @abstractmethod
    def get_vision_range():
        pass