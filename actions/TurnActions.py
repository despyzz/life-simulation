from collections import deque
import copy

from entities.creatures.Creature import Creature
from simulation.Coordinates import Coordinates
from simulation.GameRules import GameRules
from simulation.Map import Map


class TurnActions:
    def __init__(self, rules: GameRules):
        self.__rules = rules

    @staticmethod
    def __reconstruct_path(came_from, start, end):
        path = [end]
        while end != start:
            end = came_from[end]
            path.append(end)
        return path[::-1]

    def next_turn(self, simulation_map: Map):
        self.__move_creatures(simulation_map)

    def __move_creatures(self, simulation_map: Map):
        map_copy = copy.copy(simulation_map)
        for entity_coordinates, entity in map_copy.entities.items():
            if not isinstance(entity, Creature):
                continue
            vision_range = entity.get_vision_range()
            food_type = entity.get_food_type()

            entity_x = entity_coordinates.x
            entity_y = entity_coordinates.y

            x1 = max(0, entity_x - vision_range)
            y1 = max(0, entity_y - vision_range)
            x2 = min(self.__rules.map_size - 1, entity_x + vision_range)
            y2 = min(self.__rules.map_size - 1, entity_y + vision_range)

            blocked = set()
            finish = set()
            for y in range(y1, y2):
                for x in range(x1, x2):
                    coordinates = Coordinates(x, y)
                    if coordinates in map_copy.entities.keys():
                        if isinstance(map_copy.entities[coordinates], food_type):
                            finish.add(coordinates)
                        else:
                            blocked.add(coordinates)

            queue = deque([Coordinates(entity_x, entity_y)])
            visited = {Coordinates(entity_x, entity_y)}
            came_from = {}

            path = None
            while queue:
                current = queue.popleft()

                if current in finish:
                    path = TurnActions.__reconstruct_path(came_from, entity_coordinates, current)
                    break

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    next_x = current.x + dx
                    next_y = current.y + dy
                    next_coordinates = Coordinates(next_x, next_y)

                    if next_coordinates in blocked:
                        continue

                    if x1 <= next_x <= x2 and y1 <= next_y <= y2 and next_coordinates not in visited:
                        queue.append(next_coordinates)
                        visited.add(next_coordinates)
                        came_from[next_coordinates] = current

            if path is None:
                continue
            move_to_coordinates = path[1]
            if move_to_coordinates in simulation_map.entities.keys():
                simulation_map.pop_from(move_to_coordinates)
            entity = simulation_map.pop_from(entity_coordinates)
            simulation_map.set_to(move_to_coordinates, entity)
