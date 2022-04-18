import numpy as np
import pygame

from GameBoard.Tile import Tile
import Constants

class Chunk():
    size = Constants.CHUNK_SIZE
    DEBUG = False

    def __init__(self, chunk_x, chunk_y):
        self.chunk_x = chunk_x
        self.chunk_y = chunk_y

        self.tiles = np.array([Tile.build(np.random.choice(['grass', 'dirt'])) for n in range(Chunk.size ** 2)]).reshape((Chunk.size, Chunk.size))

    # interpret offset as how many chunks x & y away from player chunk
    def render(self, screen, player, offset):
        relative_player_x = abs(player['x']) % Chunk.size
        relative_player_y = abs(player['y']) % Chunk.size

        # Calculate tile offset used for rendering tiles
        # these values should be zero for the tile the player is in
        tile_offset_x = offset['x'] * Chunk.size - player['x']
        tile_offset_y = offset['y'] * Chunk.size - player['y']

        index = range(Chunk.size)
        for i in index:
            for j in index:
                x = tile_offset_x + i
                y = tile_offset_y + j
                self.tiles[i, j].render(screen, player, offset={'x': x, 'y': y})

        if Chunk.DEBUG:
            font_size = int(100 * Constants.SCALE)
            font = pygame.font.SysFont(None, font_size)
            loc_text = font.render(f'(%d, %d)' % (offset['x'], offset['y']), True, 255)

            text_offset = Tile.width * Chunk.size / 2
            text_offset = Tile.height * Chunk.size / 2
            pixel_x = tile_offset_x * (Tile.width + Tile.x_pixel_offset) + Constants.SCREEN_WIDTH / 2
            pixel_y = tile_offset_y * (Tile.height + Tile.y_pixel_offset) + Constants.SCREEN_HEIGHT / 2

            width = Chunk.size * (Tile.width + Tile.x_pixel_offset)
            height = Chunk.size * (Tile.height + Tile.y_pixel_offset)
            pygame.draw.rect(screen, 255, pygame.Rect(pixel_x, pixel_y, width, height), width=1)
            screen.blit(loc_text, (pixel_x + text_offset - font_size / 2, pixel_y + text_offset - font_size / 2))