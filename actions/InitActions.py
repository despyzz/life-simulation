from simulation.Coordinates import Coordinates
from simulation.GameRules import GameRules
from simulation.Map import Map
import random


class InitActions:
    def __init__(self, rules: GameRules):
        self.__rules = rules

    def init_simulation(self, simulation_map: Map) -> None:
        for entity, count in self.__rules.entities_counts.items():
            for _ in range(count):
                coordinates = self.__generate_unique_coordinates(simulation_map)
                simulation_map.set_to(coordinates, entity())

    def __generate_coordinates(self):
        x = random.randint(0, self.__rules.map_size-1)
        y = random.randint(0, self.__rules.map_size-1)
        coordinates = Coordinates(x, y)
        return coordinates

    def __generate_unique_coordinates(self, simulation_map: Map):
        coordinates = self.__generate_coordinates()
        while coordinates in simulation_map.entities.keys():
            coordinates = self.__generate_coordinates()
        return coordinates
