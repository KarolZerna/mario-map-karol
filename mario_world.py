import collections
import queue

class World:
    def __init__(self, map, settings, agent):
        self.map = map
        self.settings = settings
        self.agent = agent
        (self.rows, self.columns) = self.map.shape


    def travel_path_bfs(self, mario_pos):
        queue = collections.deque([[mario_pos]]) 
        seen = set([mario_pos])

        while queue:
            path = queue.popleft()
            x, y = path[-1]

            if self.map[x][y] == self.settings.PIPE:
                return path
        
            actions = [self.settings.UP, self.settings.DOWN, self.settings.LEFT, self.settings.RIGHT]
            successors = self.agent.transition_function(x, y, actions)

            for x2,y2 in successors:
                if 0 <= x2 < self.rows and 0 <= y2 < self.columns and self.map[x2][y2] != self.settings.WALL and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))