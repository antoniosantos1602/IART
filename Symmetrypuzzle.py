from copy import deepcopy
from collections import deque
import heapq
import time

    # definition of the problem
class Symmetry_puzzle:

        def __init__(self, board, move_history=None):
            # board(list[list[int]]) - the state of the board
            # move_history(list[list[list[int]]]) - the history of the moves up until this state
            self.board = deepcopy(board)

            if move_history is None:
                move_history = []
            
            # create an empty array and append move_history
            self.move_history = [] + move_history + [self.board]
        

        def children(self):
           children = []
 
           for i in range(len(self.board)):
             for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    for k in [1, 2, 3]:
                        child_board = deepcopy(self.board)
                        child_board[i][j] = k
                        child = Symmetry_puzzle(child_board, self.move_history)
                        
                        if child not in self.move_history and child not in children:
                            children.append(child)
           return children

      #  @move
       # def add_circle(self):
        #    for row in range(len(self.board)):
         #       for col in range(len(self.board[0])):
          #          if self.board[row][col] == 0:
           #             self.board[row][col] = 1
            #            return True
            #return False

        #@move
        #def add_square(self):
         #   for row in range(len(self.board)):
          #      for col in range(len(self.board[0])):
           #         if self.board[row][col] == 0:
            #            self.board[row][col] = 2
             #           return True
            #return False
        #@move
        #def add_triangle(self):
         #   for row in range(len(self.board)):
          #      for col in range(len(self.board[0])):
           #         if self.board[row][col] == 0:
            #            self.board[row][col] = 3
             #           return True
            #return False
       
    # objetive state where all rows and columns of the matrix are palindromes.
        def objective_state(self):
                # Check if every row and column is a palindrome
                for i in range(len(self.board)):
                    # Obter a linha i e criar uma cópia sem os valores 0
                    row = []
                    for x in self.board[i]:
                        if x != 0:
                            row.append(x)

                    if row != row[::-1]:
                        return False
                    # Obter a coluna i e criar uma cópia sem os valores 0
                    col = []
                    for j in range(len(self.board)):
                        if self.board[j][i] != 0:
                            col.append(self.board[j][i])

                    if col != col[::-1]:
                        return False
                return True

        def __hash__(self):
            # to be able to use the state in a set
            return hash(str([item for sublist in self.board for item in sublist]))

        #def __eq__(self, other):
            # compares the two matrices
         #  return [item for sublist in self.board for item in sublist] == [item for sublist in other.board for item in sublist]

def h1(state):
    # count non-palindromic rows
    non_palindromic_rows = 0
    for row in state.board:
        row_trimmed = [c for c in row if c != 0]
        if len(row_trimmed) > 1 and row_trimmed != row_trimmed[::-1]:
            non_palindromic_rows += 1
    # count non-palindromic columns
    non_palindromic_cols = 0
    for j in range(len(state.board[0])):
        col = [state.board[i][j] for i in range(len(state.board))]
        col_trimmed = [c for c in col if c != 0]
        if len(col_trimmed) > 1 and col_trimmed != col_trimmed[::-1]:
            non_palindromic_cols += 1
    # return the sum of non-palindromic rows and columns
    return (non_palindromic_rows + non_palindromic_cols)/2

def greedy_search(problem, heuristic):
    setattr(Symmetry_puzzle,"__lt__", lambda self, other: heuristic(self) < heuristic(other))
    states = [problem]
    visited = set()
   

    while states:
        node = heapq.heappop(states)
        visited.add(node)

        if node.objective_state():
            return node.move_history
        
        for child in node.children():
            
            if child not in visited:
                print(child.board)
                heapq.heappush(states,child)
        heapq.heapify(states)  
    return None

def print_sequence(sequence):
        if sequence is None:
         print("No solution found")
         return

        print("Steps:", len(sequence) - 1)
        # prints the sequence of states
        for state in sequence:
            for row in state:
                print(row)
            print()


def generate_tree(node, depth):
    if depth == 0:
        return
    children = node.children()
    for child in children:
        
        generate_tree(child, depth - 1)


    #def problems():
    #   return (
    #      Symmetry_puzzle([[1, 2, 3], [5, 0, 6], [4, 7, 8]]),
    #     Symmetry_puzzle([[1, 3, 6], [5, 2, 0], [4, 7, 8]]),
        #    Symmetry_puzzle([[1, 6, 2], [5, 7, 3], [0, 4, 8]]),
        #   Symmetry_puzzle([[5, 1, 3, 4], [2, 0, 7, 8], [
        #               10, 6, 11, 12], [9, 13, 14, 15]]),
    # )

def bfs(problem):   
        # problem(NPuzzleState) - the initial state
        queue = deque([problem]) # can also also use array and pop(0)
        visited = set() # to not visit the same state twice
    
        while queue:
            
            node = queue.popleft();
            
            if node.objective_state():  
                return node.move_history

            for child in node.children():
                if(child not in visited):
               
                    print(child.board)
                    visited.add(child)
                    queue.append(child)
        return None

def dfs(problem): 
        # problem(NPuzzleState) - the initial state
        stack = deque([problem]) # can also also use array and pop(0)
        visited = set() # to not visit the same state twice
        while stack:
            node = stack.pop();
            
            if node.objective_state():  
                return node.move_history
            
            for child in node.children():
                if(child not in visited):
                    visited.add(child)
                    stack.append(child)
        return None

def a_star_search(problem,heuristic):
    return greedy_search(problem,lambda state: len(state.move_history) + heuristic(state))

             

problem = Symmetry_puzzle([[0,0,0,3,2],
                           [0,0,0,2,0],
                           [1,1,1,0,1],
                           [0,3,3,0,1],
                           [0,0,2,0,0]])

print("What mode do you want to play:\nManual(1)\nAuto(2)")
mode = int(input("Input: "))

if(mode != 1 and mode != 2):
    print("invalid input")
else:
    if(mode == 2):
      print("What algorithm do you want to use:\nBFS(1)\nDFS(2)\nGreedy(3)\nA-Star(4)")
      value = int(input("Input: "))

      if(value > 4 or value < 1):
       print("No such algorithm")
      else:
        if(value == 1):
         print_sequence(bfs(problem))
        if(value == 2):
         print_sequence(dfs(problem))
        if(value == 3):
         print_sequence(greedy_search(problem,h1))
        if(value == 4):
         print_sequence(a_star_search(problem,h1))
    if(mode == 1):
        print("")





