# snake.py

import pygame
from constants import *

class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.direction = (1, 0)  # Hacia la derecha
        self.grow_flag = False

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.body.insert(0, new_head)
        if not self.grow_flag:
            self.body.pop()
        else:
            self.grow_flag = False

    def change_direction(self, new_dir):
        if (new_dir[0] * -1, new_dir[1] * -1) != self.direction:
            self.direction = new_dir

    def grow(self):
        self.grow_flag = True

    def draw(self, screen):
        for segment in self.body:
            rect = pygame.Rect(segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect)

    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:]

    def get_head(self):
        return self.body[0]
