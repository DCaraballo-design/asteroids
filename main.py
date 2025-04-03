# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
sys.path.append('d:/artis/Documents/asteroids/venv/')  # Add the path to constants.py

from lib import *

import constants # Import the constants module
# test_pygame.py
import pygame

from pygame.locals import *  # Import all constants from pygame.locals
from constants import *  # Import all constants from constants

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")  # Access SCREEN_WIDTH from constants
    print(f"Screen height: {constants.SCREEN_HEIGHT}")  # Access SCREEN_HEIGHT from constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Use constants from constants.py
    pygame.display.set_caption("Asteroids") # Set the window title  to "Asteroids"
    color = (0, 0, 0)  # Set the background color to black
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                return
        
        # Update the game state and draw the screen here
        #screen.blit(background, (0, 0)) # Draw the background image
        pygame.Surface.fill(screen, (0, 0, 0), rect=None)  # Fill the screen with black
        pygame.display.flip()
        clock = pygame.time.Clock()  # Create a clock object to control the frame rate  of the game loop
    # Load the background image and scale it to fit the screen
    #background = pygame.image.load("assets/background.png").convert()               # Load the background image
    #background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Scale the background image to fit the screen size
    # Load the spaceship image and scale it to fit the screen   (optional)
    #spaceship = pygame.image.load("assets/spaceship.png").convert_alpha()  # Load the spaceship image with transparency

if __name__ == "__main__":
    main()
