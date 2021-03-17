import collections
import queue
#import Queue as queue

class World:
    def __init__(self, map, settings):
        self.map = map
        self.settings = settings
        (self.rows, self.columns) = self.map.shape


    def travel_path_bfs(self, start):
        queue = collections.deque([[start]]) 
        seen = set([start])

        while queue:
            path = queue.popleft()
            x, y = path[-1]

            if self.map[x][y] == self.settings.PIPE:
                return path
        
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < self.rows and 0 <= y2 < self.columns and self.map[x2][y2] != self.settings.WALL and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))