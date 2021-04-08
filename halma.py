import pygame
from halma.constants import WIDTH, HEIGHT, SQUARE_SIZE
from halma.board import Board

FPS = 60

WIN = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'Halma' )

# user being able to move pieces by clicking
def mouseClick(pos):
    pass

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick( FPS )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw( WIN )
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()