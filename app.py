from simulation.GameRules import GameRules
from simulation.Simulation import Simulation


def main():
    rules = GameRules()
    simulation = Simulation(rules)
    simulation.start_simulation()


if __name__ == '__main__':
    main()
