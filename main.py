# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    black_rgb = (0,0,0)
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player_1 = player(x,y)
    i = True
    clock = pygame.time.Clock()
    dt = 0
    while i == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black_rgb)
        player_1.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()