class Board(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.state = []
        # Create board
        for row in range(self.height):
            self.state.append([])
            for cell in range(self.width):
                self.state[row].append(0)
