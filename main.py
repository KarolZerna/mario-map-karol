import numpy as np
from mario_world import World
from settings import Settings
from agent import Agent


def main():
    map = np.array([[1, 3, 0, 2],
                    [0, 0, 0, 3],
                    [0, 3, 0, 3],
                    [2, 3, 0, 0]])

    settings = Settings()
    agent = Agent(settings)
    world = World(map, settings, agent)

    number_boxes = world.number_of_box()

    print(world.map)
    print(number_boxes)


if __name__ == "__main__":
    main()