from queue import Queue
from puzzle.constants import SQUARE_SIZE

def solve_puzzle(initial_state):
    class State:
        def __init__(self, grid, actions=[]):
            self.grid = grid
            self.actions = actions

        def is_goal(self):
            # Check if every row and column is a palindrome
            for i in range(SQUARE_SIZE):
                row = [x for x in self.grid[i] if x != 0]
                if row != row[::-1]:
                    return False
                col = [self.grid[j][i] for j in range(SQUARE_SIZE) if self.grid[j][i] != 0]
                if col != col[::-1]:
                    return False
            return True

        def successors(self):
            for i in range(SQUARE_SIZE):
                for j in range(SQUARE_SIZE):
                    if self.grid[i][j] == 0:
                        for shape in range(1, 4):
                            new_grid = [row[:] for row in self.grid]
                            new_grid[i][j] = shape
                            yield State(new_grid, self.actions + [(i, j, shape)])

    visited = set()
    q = Queue()
    initial = State(initial_state)

    q.put(initial)
    visited.add(tuple(map(tuple, initial.grid)))

    while not q.empty():
        state = q.get()
        if state.is_goal():
            return state.actions

        for successor in state.successors():
            if tuple(map(tuple, successor.grid)) not in visited:
                q.put(successor)
                visited.add(tuple(map(tuple, successor.grid)))

    return None