import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        dt = clock.tick(60) / 1000 # Set FPS cap
        log_state() # Run debugging tool

        for event in pygame.event.get(): # Quit loop if window closed
            if event.type == pygame.QUIT:
                return
            
        player.update(dt) # Update player position if key input detected
        screen.fill("black") # Wipe previous frame
        player.draw(screen) # Print new frame
        pygame.display.flip() # Push new frame to Surface



    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
