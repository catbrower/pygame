import pygame

import Constants
from GameBoard.Tile import Tile
from GameBoard.Chunk import Chunk
from GameBoard.World import World

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

screen = pygame.display.set_mode([Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT])

world = World()

running = True
while running:
    for event in pygame.event.get():
        world.update(event)
        if event.type == pygame.QUIT:
            running = False

    # pressed_keys = pygame.key.get_pressed()
    # print(events)

    # tile.update(pressed_keys)
    screen.fill((0, 0, 0))

    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # screen.blit(tile.surf, tile.rect)
    # chunk.render(screen)
    world.render(screen)

    pygame.display.flip()
pygame.quit()