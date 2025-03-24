import pygame
from constants import *
from player import Player 
from asteroids import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Initialize sprite groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    
    # Assign static containers for classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Create instances of Player and AsteroidField
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        #Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all updatable sprites
        updatable.update(dt)

        # Clear the screen for refreshing visuals
        screen.fill((0,0,0))

        # Draw all drawable sprites
        for entity in drawable:
            entity.draw(screen)

        # Update the display    
        pygame.display.flip()

        # Limit the frame rate and calculate time delta
        dt = clock.tick(60) / 1000  # 60 FPS target

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()