import numpy as np
import pandas as pd
from GameBoard.Chunk import Chunk
from GameBoard.Tile import Tile

class World():
    expansion_size = 11
    render_distance = 2

    def __init__(self):
        self.player = {'x': 0, 'y': 0}
        start = -1 * round(World.expansion_size / 2) + 1
        stop = start + World.expansion_size
        index = []
        for i in range(start, stop):
            for j in range(start, stop):
                index.append((i, j))

        self.chunks = pd.DataFrame(index=pd.MultiIndex.from_tuples(index, names=['x', 'y']))
        for i in range(start, stop):
            for j in range(start, stop):
                self.chunks[i, j] = Chunk(i, j)

        # print(self.chunks.iloc[(0,0)])
    def render(self, screen):
        # Determine player chunk locations
        # TODO execute this only on player move
        chunk_x = int(np.floor(self.player['x'] / Chunk.size))
        chunk_y = int(np.floor(self.player['y'] / Chunk.size))

        chunk_start = -World.render_distance
        for i in range(chunk_start, World.render_distance):
            for j in range(chunk_start, World.render_distance):
                self.chunks.iloc[(chunk_x + i, chunk_y + j)].render(screen, self.player, offset={'x': chunk_x + i, 'y': chunk_y + j})

    # def update(self, pressed_keys):
    #     if pressed_keys[K_UP]:
    #         self.rect.move_ip(0, -5)
    #     if pressed_keys[K_DOWN]:
    #         self.rect.move_ip(0, 5)
    #     if pressed_keys[K_LEFT]:
    #         self.rect.move_ip(-5, 0)
    #     if pressed_keys[K_RIGHT]:
    #         self.rect.move_ip(5, 0)

    #     if self.rect.left < 0:
    #         self.rect.left = 0
    #     if self.rect.right > SCREEN_WIDTH:
    #         self.rect.right = SCREEN_WIDTH
    #     if self.rect.top <= 0:
    #         self.rect.top = 0
    #     if self.rect.bottom >= SCREEN_HEIGHT:
    #         self.rect.bottom = SCREEN_HEIGHT
