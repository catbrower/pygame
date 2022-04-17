import pygame
from pygame.locals import (
    RLEACCEL
)

import Constants

class Tile(pygame.sprite.Sprite):
    surfaces = [
        pygame.image.load("src/images/tiles/grass.png")
    ]

    # These need to be set manually based on the tile image files
    x_pixel_offset = 1 * Constants.SCALE
    y_pixel_offset = -13 * Constants.SCALE

    width = surfaces[0].get_width() * Constants.SCALE
    height = surfaces[0].get_height() * Constants.SCALE

    for i in range(len(surfaces)):
        surfaces[i] = pygame.transform.scale(surfaces[i], (width, height))

    def build(surf_type):
        surf_type = surf_type.lower()

        if surf_type == 'grass':
            return Tile(Tile.surfaces[0]) 

    def __init__(self, surface):
        super(Tile, self).__init__()
        # self.surf.set_colorkey((25, 25, 255), RLEACCEL)
        # self.surf = pygame.Surface((75, 75))
        # self.surf.fill((255, 255, 255))
        self.surface = surface
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
