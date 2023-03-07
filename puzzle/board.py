import pygame
from .constants import *

class Board:
    
    def __init__(self):
        self.board = []
    

    def draw_squares(self, win):
        win.fill((0, 0, 0))
        MARGIN = 2
        for row in range(5):
            for col in range(5):
                x = col * (SQUARE_SIZE + MARGIN)
                y = row * (SQUARE_SIZE + MARGIN)
                pygame.draw.rect(win, (255, 255, 255), (x, y, SQUARE_SIZE, SQUARE_SIZE))

         

