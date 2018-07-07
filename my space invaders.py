import pygame
from pygame.locals import *  # allows recognition of quit and x to quit


# my Space Invaders July 7 2018


# === CONSTANTS === (UPPER_CASE names)

# screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLUE = (10, 100, 255)
LIGHT_BLUE = (100, 100, 255)
LIGHT_RED = (255, 100, 100)
LIGHT_GREEN = (100, 128, 100)

# === LOAD IMAGES ===     x_img = pygame.image.load('ship.png') example

IMAGE_NAMES = ["ship"]
IMAGES = {name: pygame.image.load(f'{name}.png')for name in IMAGE_NAMES}
# ship sprite 24 X 30 px


# === CLASSES === (CamelCase names)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = IMAGES['ship']
        self.rect = self.image.get_rect(topleft=(SCREEN_WIDTH//2-15, 540))
        self.move_x = 0
        self.move_y = 0
        self.speed = 5

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y

    def event_handler(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_x -= self.speed
            elif event.key == pygame.K_RIGHT:
                self.move_x += self.speed
            elif event.key == pygame.K_UP:
                self.move_y -= self.speed
            elif event.key == pygame.K_DOWN:
                self.move_y += self.speed

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.move_x += self.speed
            elif event.key == pygame.K_RIGHT:
                self.move_x -= self.speed
            elif event.key == pygame.K_UP:
                self.move_y += self.speed
            elif event.key == pygame.K_DOWN:
                self.move_y -= self.speed

# === MAIN === (lower_case names)

# --- (global) variables ---

# --- init ---

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()


# --- objects ---

player = Player()

# --- mainloop ---

clock = pygame.time.Clock()
is_running = True

while is_running:

    # --- events ---

    for event in pygame.event.get():

        # --- global events ---

        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

        # --- objects events ---

        player.event_handler(event)

    # --- updates ---

    player.update()


    # --- draws ---

    screen.fill(BLACK)

    player.draw(screen)

    pygame.display.update()

    # --- FPS ---

    clock.tick(FPS)

# --- the end ---

pygame.quit()
