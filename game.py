import pygame
from new.constants import *

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()


    def new(self, filename):
        with open(filename) as f:
            self.grid = []
            self.original_grid = [] 
            for line in f:
                row = [int(x) for x in line.split()]
                if row:
                    self.grid.append(row)
                    self.original_grid.append(row.copy()) 
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('SYMMETRY PUZZLE')

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        pass
    
    def draw_grid(self):
        for row in range(0, SQUARE_SIZE * TILESIZE + 1, TILESIZE):
            pygame.draw.line(self.screen, BLACK, (row, 0), (row, SQUARE_SIZE * TILESIZE))
        for col in range(0, SQUARE_SIZE * TILESIZE + 1, TILESIZE):
            pygame.draw.line(self.screen, GREY, (0, col), (SQUARE_SIZE * TILESIZE, col))

    def draw(self):
        self.screen.fill(WHITE)
        self.draw_grid()

        font = pygame.font.Font(None, 30)
        for i in range(SQUARE_SIZE):
            for j in range(SQUARE_SIZE):
                shape = self.grid[i][j]
                x = j * TILESIZE + TILESIZE // 2
                y = i * TILESIZE + TILESIZE // 2
               
                if shape == 1:
                    pygame.draw.circle(self.screen, GREEN, (x, y), TILESIZE // 2 - 2)
                elif shape == 2:
                    pygame.draw.rect(self.screen, RED, (x - TILESIZE // 2 + 2, y - TILESIZE // 2 + 2, TILESIZE - 4, TILESIZE - 4))
                elif shape == 3:
                    pygame.draw.polygon(self.screen, BLUE, [(x - TILESIZE // 2 + 2, y + TILESIZE // 2 - 2), (x + TILESIZE // 2 - 2, y + TILESIZE // 2 - 2), (x, y - TILESIZE // 2 + 2)])

        pygame.display.flip()

    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // TILESIZE, x // TILESIZE
                print(self.grid[row][col])
                if self.original_grid[row][col] == 0:
                        if self.board[row][col] == 0:
                            self.board[row][col] = 1
                        elif self.board[row][col] == 1:
                            self.board[row][col] = 2
                        elif self.board[row][col] == 2:
                            self.board[row][col] = 3
                        elif self.board[row][col] == 3:
                            self.board[row][col] = 0
                        else:
                            pass



game = Game()

filename = input("what puzzle do you want? ")

if filename.isdigit() and int(filename) in range(1, 21):
    game.new(f'displays/{filename}.txt')
    print(game.grid)
    game.run()
else:
    print("Invalid filename")
    pygame.quit()
    quit(0)

game.run()
