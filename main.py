import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    

    while True:
        dt = clock.tick(60) / 1000 # Set FPS cap
        log_state() # Run debugging tool

        for event in pygame.event.get(): # Quit loop if window closed
            if event.type == pygame.QUIT:
                return
            
        #player.update(dt) # Update player position if key input detected
        updatable.update(dt) # Update all updateable objects, not just the player
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        screen.fill("black") # Wipe previous frame
        #player.draw(screen) # Print new frame
        for drawing in drawable: # Print all items, not just the player
            drawing.draw(screen)
        pygame.display.flip() # Push new frame to Surface



    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
