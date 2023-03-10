import pygame
from puzzle.constants import WIDTH, HEIGHT
from puzzle.board import Board


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SYMMETRY PUZZLES')

def main():
    run = True
    board = Board()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        
        board.draw_squares(WIN)       
        pygame.display.update()
        test
    
    pygame.quit()

main()













"""
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Symmetry Puzzles')


def main():

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # preenchendo a tela com a cor branca
        screen.fill(BLACK)

        # construindo o tabuleiro
        build_board(screen)

        pygame.display.update()

    pygame.quit()

main()

"""