import tkinter as tk

from entities.creatures.Herbivore import Herbivore
from entities.creatures.Predator import Predator
from entities.environment.Grass import Grass
from entities.environment.Rock import Rock
from entities.environment.Tree import Tree
from simulation.Coordinates import Coordinates
from simulation.Simulation import Simulation


class GUIRenderer:
    def __init__(self, simulation: Simulation) -> None:
        self.__simulation = simulation
        self.__entitiy_size = 30
        self.__map_size = simulation.game_rules.map_size

        self.__root = tk.Tk()
        self.__create_entities_map_canvas()
        self.__create_buttions_frame()

    def __create_buttions_frame(self):
        self.__buttons_frame = tk.Frame(master=self.__root)
        self.__start_button = tk.Button(master=self.__buttons_frame,
                                        text='Start Simulation',
                                        command=lambda: self.__simulation.start_simulation())
        self.__pause_button = tk.Button(master=self.__buttons_frame,
                                        text='Pause Simulation',
                                        command=lambda: self.__simulation.pause_simulation())
        self.__start_button.pack(side='left')
        self.__pause_button.pack(side='right')
        self.__buttons_frame.pack(side='bottom')

    def __create_entities_map_canvas(self):
        self.__entities_canvas = tk.Canvas(master=self.__root,
                                           width=self.__map_size * self.__entitiy_size,
                                           height=self.__map_size * self.__entitiy_size)
        self.__entities_canvas.pack(side='top')

    def __get_color(self, coordinates: Coordinates) -> str:
        if coordinates in self.__simulation.map.entities.keys():
            entity = self.__simulation.map.entities[coordinates]
            if isinstance(entity, Predator):
                return 'red'
            elif isinstance(entity, Herbivore):
                return 'blue'
            elif isinstance(entity, Grass):
                return 'green'
            elif isinstance(entity, (Rock, Tree)):
                return 'black'
        return 'white'

    def __render_entities_map(self):
        self.__entities_canvas.delete('all')
        for y in range(self.__map_size):
            for x in range(self.__map_size):
                coordinates = Coordinates(x, y)
                color = self.__get_color(coordinates)

                x1 = x * self.__entitiy_size
                y1 = y * self.__entitiy_size
                x2 = x1 + self.__entitiy_size
                y2 = y1 + self.__entitiy_size

                self.__entities_canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def __render_turn_counter(self) -> None:
        turn_counter = self.__simulation.turn_counter
        self.__root.title(f'Turns: {turn_counter.counter}')

    def render_simulation(self) -> None:
        # switch buttons
        if self.__simulation.on_pause:
            self.__pause_button.config(state='disabled')
            self.__start_button.config(state='normal')
        else:
            self.__pause_button.config(state='normal')
            self.__start_button.config(state='disabled')

        self.__render_turn_counter()
        self.__render_entities_map()

        self.__root.update_idletasks()
        self.__root.update()
