from simulation.GameRules import GameRules
from simulation.Map import Map
import  random

class InitActions:
    def __init__(self, rules: GameRules):
        self.__rules = rules

    def init_simulation(self, simulation_map: Map) -> None:

        for entity, count in self.__rules.entities_counts:


