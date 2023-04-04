import pygame
from game import Game

def main():
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
    
    if __name__ == '__main__':
        main()