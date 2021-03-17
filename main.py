import numpy as np
from mario_world import World
from settings import Settings
from agent import Agent


def main():
    map = np.array([[0, 1, 0, 2],
                    [0, 0, 0, 1],
                    [0, 1, 0, 1],
                    [2, 1, 0, 0]])
    settings = Settings()
    agent = Agent(settings)
    world = World(map, settings, agent)

    print("\n Wall-> 1 - Pipe-> 2")
    print("\n Initial map: \n",world.map)
    
    print("\n Mario position is: (0,0)")
    # Mario position in map
    mario_pos = (0,0)  

    path = World.travel_path_bfs (world, mario_pos)

    print("\n Number of squares to the nearest pipe:",len(path))
    print("\n Path Mario must follow:", path)

if __name__ == "__main__":
    main()