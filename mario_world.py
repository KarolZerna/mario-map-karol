import queue
#import Queue as queue

class World:
    def __init__(self, map, settings, agent):
        self.map = map
        self.settings = settings
        self.agent = agent

        (self.rows, self.columns) = self.map.shape

    def discard_successors(self, successors):
        filtered_successors = []

        for successor in successors:
            i = successor[0]
            j = successor[1]

            if 0 <= i < self.rows and  0 <= j < self.columns and self.map[i][j] == self.settings.MARIO:
                filtered_successors.append(successor)

        return filtered_successors

    def travel_path_bfs(self, i, j):
        open = queue.SimpleQueue()
        close = []

        open.put([i, j])

        while open.qsize() != 0:
            state = open.get()
            # mark it as visited
            self.map[state[0]][state[1]] = self.settings.VISITED
            print(self.map, "\n")

            actions = [self.settings.UP, self.settings.DOWN, self.settings.LEFT, self.settings.RIGHT]
            successors = self.agent.transition_function(state, actions)
            successors = self.discard_successors(successors)

            close.append(state)

            for successor in successors:
                open.put(successor)


    def number_of_box(self):
        boxes = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.map[i][j] == 1:
                    self.travel_path_bfs(i, j)
                    boxes += 1

        return boxes