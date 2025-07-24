# wall.py

import pygame
from constants import *

class Wall:
    def __init__(self):
        self.cells = []
        cols = WINDOW_WIDTH // CELL_SIZE
        rows = WINDOW_HEIGHT // CELL_SIZE

        for x in range(cols):
            self.cells.append((x, 0))
            self.cells.append((x, rows - 1))
        for y in range(rows):
            self.cells.append((0, y))
            self.cells.append((cols - 1, y))

    def draw(self, screen):
        for cell in self.cells:
            rect = pygame.Rect(cell[0]*CELL_SIZE, cell[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect)

    def is_collision(self, position):
        return position in self.cells
