# paddle.py

import pygame
from constants import *

class Paddle:
    def __init__(self, x, y, speed=5):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = speed

    def move(self, up=True):
        if up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        self.rect.y = max(0, min(WINDOW_HEIGHT - PADDLE_HEIGHT, self.rect.y))

    def auto_move(self, ball_y, difficulty=10):
        """La IA se mueve con cierta torpeza según el nivel de dificultad."""
        # Rango para errores intencionados
        offset = max(0, 20 - difficulty * 2)

        if self.rect.centery < ball_y - offset:
            self.move(up=False)
        elif self.rect.centery > ball_y + offset:
            self.move(up=True)

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

