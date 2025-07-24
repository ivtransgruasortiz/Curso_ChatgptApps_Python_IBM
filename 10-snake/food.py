# food.py

import random
import pygame
from constants import *

class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        cols = WINDOW_WIDTH // CELL_SIZE
        rows = WINDOW_HEIGHT // CELL_SIZE
        return (random.randint(1, cols - 2), random.randint(1, rows - 2))

    def draw(self, screen):
        rect = pygame.Rect(self.position[0]*CELL_SIZE, self.position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, ORANGE, rect)
