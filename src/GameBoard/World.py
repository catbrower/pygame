import numpy as np
import pandas as pd
import pygame
from GameBoard.Chunk import Chunk
from GameBoard.Tile import Tile

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class World():
    expansion_size = 11
    render_distance = 20

    def __init__(self):
        self.player = {'x': 0, 'y': 0}
        start = -1 * round(World.expansion_size / 2) + 1
        stop = start + World.expansion_size
        index = []
        tile_values = []
        for i in range(start, stop):
            for j in range(start, stop):
                index.append((i, j))
                tile_values.append(Chunk(i, j))

        index = pd.MultiIndex.from_tuples(index, names=['x', 'y'])
        # print(index)

        self.chunks = pd.Series(data=np.array(tile_values), index=index)
        

        # print(self.chunks.iloc[(0,0)])
    def render(self, screen):
        # Determine player chunk locations
        # TODO execute this only on player move
        chunk_x = int(np.floor(self.player['x'] / Chunk.size))
        chunk_y = int(np.floor(self.player['y'] / Chunk.size))

        chunk_start = -World.render_distance
        for i in range(chunk_start, World.render_distance):
            for j in range(chunk_start, World.render_distance):
                idx = (chunk_x + i, chunk_y + j)
                if idx in self.chunks.index:
                    self.chunks.loc[idx].render(screen, self.player, offset={'x': chunk_x + i, 'y': chunk_y + j})

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                self.player['y'] -= 1
            if event.key == K_DOWN:
                self.player['y'] += 1
            if event.key == K_LEFT:
                self.player['x'] -= 1
            if event.key == K_RIGHT:
                self.player['x'] += 1

        # if self.rect.left < 0:
        #     self.rect.left = 0
        # if self.rect.right > SCREEN_WIDTH:
        #     self.rect.right = SCREEN_WIDTH
        # if self.rect.top <= 0:
        #     self.rect.top = 0
        # if self.rect.bottom >= SCREEN_HEIGHT:
        #     self.rect.bottom = SCREEN_HEIGHT
