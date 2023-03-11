import pygame
import random
import time 
from puzzle.constants import *

class Game: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('SYMETRY PUZZLE')
        self.clock = pygame.time.Clock()

        self.grid = [[0 for j in range(SQUARE_SIZE)] for i in range(SQUARE_SIZE)]

        for i in range(SQUARE_SIZE):
            for j in range(SQUARE_SIZE):
                 self.grid[i][j] = random.choice(['circle', 'square', 'triangle'])

    def new(self):
        pass

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
        for row in range(-1,SQUARE_SIZE * TILESIZE, TILESIZE):
            pygame.draw.line(self.screen,BLACK,(row,0),(row,SQUARE_SIZE * TILESIZE))
        for col in range(-1,SQUARE_SIZE * TILESIZE, TILESIZE):
                        pygame.draw.line(self.screen,GREY,(0,col),(SQUARE_SIZE * TILESIZE,col))
    def draw(self):
        self.screen.fill(WHITE)
        self.draw_grid()

        font = pygame.font.Font(None, 30)
        for i in range(SQUARE_SIZE):
            for j in range(SQUARE_SIZE):
                shape = self.grid[i][j]
                x = i * TILESIZE + TILESIZE // 2
                y = j * TILESIZE + TILESIZE // 2
               
                if shape == 'circle':
                    pygame.draw.circle(self.screen, GREEN, (x, y), TILESIZE // 2 - 2)
                elif shape == 'square':
                    pygame.draw.rect(self.screen, RED, (x - TILESIZE // 2 + 2, y - TILESIZE // 2 + 2, TILESIZE - 4, TILESIZE - 4))
                elif shape == 'triangle':
                    pygame.draw.polygon(self.screen, BLUE, [(x - TILESIZE // 2 + 2, y + TILESIZE // 2 - 2), (x + TILESIZE // 2 - 2, y + TILESIZE // 2 - 2), (x, y - TILESIZE // 2 + 2)])


        pygame.display.flip()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
    
    def add_20_to_grid(self):
        # Add 20 to every element in the grid
        for i in range(SQUARE_SIZE):
            for j in range(SQUARE_SIZE):
                self.grid[i][j] += 20

game = Game() #instance of the game
while True:
    game.new() #new game
    game.run() #run game










