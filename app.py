from GUIRenderer import GUIRenderer
from entities.creatures.Herbivore import Herbivore
from entities.creatures.Predator import Predator
from entities.environment.Grass import Grass
from entities.environment.Rock import Rock
from entities.environment.Tree import Tree
from simulation.GameRules import GameRules
from simulation.Simulation import Simulation


def main():
    map_size = 10
    entities_counts = {
        Predator: 3,
        Herbivore: 5,
        Tree: 6,
        Grass: 8,
        Rock: 6
    }
    rules = GameRules(map_size, entities_counts)

    simulation = Simulation(rules)
    simulation.init_simulation()

    renderer = GUIRenderer(simulation)
    while True:
        renderer.render_simulation()
        if not simulation.on_pause:
            simulation.next_turn()


if __name__ == '__main__':
    main()
