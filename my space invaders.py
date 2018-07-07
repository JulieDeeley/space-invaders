import pygame
from pygame.locals import *  # allows recognition of quit and x to quit
import random
import math

# my Space Invaders July 7 2018

pygame.init()
clock = pygame.time.Clock()

# screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#x_img = pygame.image.load('ship.png') example
IMAGE_NAMES = ["ship"]
IMAGES = {name: pygame.image.load(f'{name}.png')for name in IMAGE_NAMES}
# ship sprite 24 X 30 px

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLUE = (10, 100, 255)
LIGHT_BLUE = (100, 100, 255)
LIGHT_RED = (255, 100, 100)
LIGHT_GREEN = (100, 128, 100)
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)

class Ship():
    def __init__(self):
        self.image = IMAGES['ship']
        self.rect = self.image.get_rect(topleft=(SCREEN_WIDTH//2-15, 540))
        self.vel = 5

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.vel



def main(self):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (
                 event.type == KEYDOWN and (
                  event.key == K_ESCAPE or
                  event.key == K_q
                 )):
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.rect.x  -=5
                elif event.key == pygame.K_RIGHT:
                    self.rect.x  +=5


        # User let up on a key
            elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.rect.x = 0


        pygame.display.update()
        clock.tick(60)  # sets fps to 60


main()
