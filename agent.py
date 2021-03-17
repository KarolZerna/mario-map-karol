class Agent:
    def __init__(self, settings):
        self.settings = settings

    def transition_function(self, x, y, actions):
        successors = []
        for action in actions:
            if action == self.settings.UP:
                successors.append([x - 1, y])
            if action == self.settings.DOWN:
                successors.append([x + 1, y])
            if action == self.settings.LEFT:
                successors.append([x, y - 1])
            if action == self.settings.RIGHT:
                successors.append([x, y + 1])
        return successors