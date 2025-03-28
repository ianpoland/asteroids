# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    black_rgb = (0,0,0)
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    i = True
    while i == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black_rgb)
        pygame.display.flip()

if __name__ == "__main__":
    main()