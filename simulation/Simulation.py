import copy

from actions.InitActions import InitActions
from actions.TurnActions import TurnActions
from simulation.GameRules import GameRules
from simulation.Map import Map
from simulation.TurnCounter import TurnCounter


class Simulation:
    def __init__(self, rules: GameRules):
        self.__rules = rules
        self.__map = Map()
        self.__turn_counter = TurnCounter()
        self.__turn_actions = TurnActions(rules)
        self.__init_actions = InitActions(rules)
        self.__on_pause = True

    @property
    def on_pause(self):
        return self.__on_pause

    @property
    def turn_counter(self):
        return self.__turn_counter

    def init_simulation(self):
        self.__init_actions.init_simulation(self.__map)

    def start_simulation(self):
        self.__on_pause = False

    def pause_simulation(self):
        self.__on_pause = True

    def next_turn(self):
        # TurnActions
        ...

    @property
    def map(self):
        return copy.copy(self.__map)

    @property
    def game_rules(self):
        return copy.copy(self.__rules)
