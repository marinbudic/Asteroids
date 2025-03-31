import sys
import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    black = (0, 0, 0)
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Shot.containers = (updateable, drawable, shots)
    field = AsteroidField()
    p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)
        screen.fill(black)
        
        for o in drawable:
            o.draw(screen)
        
        for o in asteroids:
            if o.check_collision(p1):
                print("Game over!")
                sys.exit()

            for bullet in shots:
                if bullet.check_collision(o):
                    bullet.kill()
                    o.split()
        
        pygame.display.flip()
        time_passed = clock.tick(60)
        dt = time_passed / 1000



if __name__ == "__main__":
    main()
