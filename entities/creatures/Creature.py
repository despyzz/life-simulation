from abc import ABC

from entities.Entity import Entity


class Creature(Entity, ABC):
    def __init__(self) -> None:
        super().__init__()
