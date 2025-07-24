# ball.py

# ball.py

import pygame
import random
from constants import *

class Ball:
    def __init__(self, speed=5):
        self.rect = pygame.Rect(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, BALL_SIZE, BALL_SIZE)
        self.base_speed = speed
        self.speed_x = 0
        self.speed_y = 0
        self.reset()

    def reset(self):
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        direction_x = random.choice((-1, 1))
        direction_y = random.choice((-1, 1))
        self.speed_x = self.base_speed * direction_x
        self.speed_y = self.base_speed * direction_y

    def update_speed(self, new_speed):
        """Actualiza la velocidad manteniendo la dirección."""
        sign_x = 1 if self.speed_x >= 0 else -1
        sign_y = 1 if self.speed_y >= 0 else -1
        self.base_speed = new_speed
        self.speed_x = sign_x * new_speed
        self.speed_y = sign_y * new_speed

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)
