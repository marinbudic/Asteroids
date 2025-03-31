import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    black = (0, 0, 0)
    clock = pygame.time.Clock()
    dt = 0
    p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(black)
        p1.draw(screen)
        pygame.display.flip()
        time_passed = clock.tick(60)
        dt = 1000/time_passed



if __name__ == "__main__":
    main()
