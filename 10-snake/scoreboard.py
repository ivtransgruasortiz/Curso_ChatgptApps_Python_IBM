# scoreboard.py

import pygame
from constants import *

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 24)
        self.large_font = pygame.font.SysFont("Arial", 48)

    def increase(self):
        self.score += 1

    def draw(self, screen, speed, game_over=False):
        # Puntos
        text = self.font.render(f"Puntos: {self.score}", True, WHITE)
        screen.blit(text, (10, 10))

        # Velocidad (barra)
        pygame.draw.rect(screen, WHITE, (10, 40, 100, 10), 2)
        pygame.draw.rect(screen, WHITE, (10, 40, speed * 10, 10))
        speed_text = self.font.render(f"Velocidad: {speed}", True, WHITE)
        screen.blit(speed_text, (120, 35))

        if game_over:
            msg = self.large_font.render("¡Has perdido!", True, WHITE)
            restart = self.font.render("Pulsa R para reiniciar", True, WHITE)
            screen.blit(msg, msg.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 40)))
            screen.blit(restart, restart.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 10)))
