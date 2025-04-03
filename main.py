import sys
sys.path.append('d:/artis/Documents/asteroids/venv/')  # Add the path to constants.py

from lib import *
import constants # Import the constants module
# test_pygame.py
import pygame
from Player import Player  # Ensure the Player class is imported from the correct module
from pygame.locals import *  # Import all constants from pygame.locals
from constants import *  # Import all constants from constants
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()  # Initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Use constants from constants.py
    pygame.display.set_caption("Asteroids") # Set the window title  to "Asteroids"
    clock = pygame.time.Clock() 
    dt = 0  # Initialize the time delta between frames
    
    updateables = pygame.sprite.Group()  # Create a group for updateable objects
    drawables = pygame.sprite.Group()  # Create a group for drawable objects
    asteroids = pygame.sprite.Group()  # Create a group for all asteroids

    # Set the containers for the Player class
    Player.containers = (updateables, drawables)  # Set the containers for the Player class
    # Set the containers for the Asteroid class
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = updateables
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Create a player object at the center of the screen
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                return
        
        # Update the game state and draw the screen here
        updateables.update(dt)  # Update the player state

        pygame.Surface.fill(screen, (0, 0, 0), rect=None)  # Fill the screen with black
        for obj in drawables:
            obj.draw(screen)  # Draw the player on the screen
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0  # Set the frame rate to 60 FPS
    

if __name__ == "__main__":
    main()
