import numpy as np
from mario_world import World
from settings import Settings


def main():
    map = np.array([[0, 1, 0, 2],
                    [0, 0, 0, 1],
                    [0, 1, 0, 1],
                    [2, 1, 0, 0]])
    settings = Settings()
    world = World(map, settings)

    mapa = World.travel_path_bfs (world, (1,0))
    print(world.map)
    print(mapa)
    print(len(mapa))

if __name__ == "__main__":
    main()