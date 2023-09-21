from GUIRenderer import GUIRenderer
from entities.creatures.Herbivore import Herbivore
from entities.creatures.Predator import Predator
from entities.environment.Grass import Grass
from entities.environment.Rock import Rock
from entities.environment.Tree import Tree
from simulation.GameRules import GameRules
from simulation.Simulation import Simulation
from time import sleep


def main():
    rules = GameRules(map_size=10,
                      entities_counts={Predator: 3, Herbivore: 5, Tree: 6, Grass: 8, Rock: 6})

    simulation = Simulation(rules)
    simulation.init_simulation()

    renderer = GUIRenderer(simulation)
    while True:
        renderer.render_simulation()

        if not simulation.on_pause:
            simulation.next_turn()

            # one turn once per second
            sleep(1)


if __name__ == '__main__':
    main()
