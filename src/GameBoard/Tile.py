import numpy as np
import pygame
from pygame.locals import (
    RLEACCEL
)

import Constants

class Tile(pygame.sprite.Sprite):
    surfaces = {
        'grass': pygame.image.load("src/images/tiles/grass.png"),
        'dirt': pygame.image.load("src/images/tiles/dirt.png")
    }

    # These need to be set manually based on the tile image files
    x_pixel_offset = 0
    y_pixel_offset = -14 + 14

    width = surfaces['grass'].get_width() * Constants.SCALE
    height = surfaces['grass'].get_height() * Constants.SCALE

    for key in surfaces.keys():
        surfaces[key] = pygame.transform.scale(surfaces[key], (width, height))

    def build(surf_type):
        surf_type = surf_type.lower()

        return Tile(Tile.surfaces[surf_type]) 

    def __init__(self, surface):
        super(Tile, self).__init__()
        # self.surf.set_colorkey((25, 25, 255), RLEACCEL)
        # self.surf = pygame.Surface((75, 75))
        self.surface = surface
        self.surface.fill((np.random.uniform(), np.random.uniform(), np.random.uniform()), special_flags=pygame.BLEND_ADD)
        self.rect = self.surface.get_rect()
        self.origin = (0, 0)
        self.offset = (0, 0)

    def render(self, screen, player, offset):
        x = offset['x'] * Tile.width + offset['x'] * Tile.x_pixel_offset
        y = offset['y'] * Tile.height + offset['y'] * Tile.y_pixel_offset
        if offset['y'] % 2 == 0:
            x += Tile.width / 2

        pixel_offset_x = Constants.SCREEN_WIDTH / 2 
        pixel_offset_y = Constants.SCREEN_HEIGHT / 2
        screen.blit(self.surface, self.rect.move(x + pixel_offset_x, y + pixel_offset_y))
