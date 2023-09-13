import copy

from actions.InitActions import InitActions
from actions.TurnActions import TurnActions
from simulation.GameRules import GameRules
from simulation.Map import Map
from simulation.TurnCounter import TurnCounter


class Simulation:
    def __init__(self, rules: GameRules):
        self.__map = Map()
        self.__turn_counter = TurnCounter()
        self.__turn_actions = TurnActions(rules)
        self.__init_actions = InitActions(rules)

    def start_simulation(self):
        self.__init_actions.init_simulation(self.__map)

    def pause_simulation(self):
        # ???
        ...

    def next_turn(self):
        # TurnActions
        ...

    @property
    def map(self):
        return copy.copy(self.__map)