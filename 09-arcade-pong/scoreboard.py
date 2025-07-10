# scoreboard.py

import pygame
from constants import *

class Scoreboard:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", FONT_SIZE)
        self.score_player = 0
        self.score_ai = 0

    def draw(self, screen, ball_speed, paddle_speed, difficulty):
        score_text = f"Jugador: {self.score_player}   IA: {self.score_ai}"
        config_text = f"Bola:{ball_speed}  Pala:{paddle_speed}  Dificultad:{difficulty}"

        score_surf = self.font.render(score_text, True, WHITE)
        config_surf = self.font.render(config_text, True, WHITE)

        score_rect = score_surf.get_rect(center=(WINDOW_WIDTH // 2, 30))
        config_rect = config_surf.get_rect(center=(WINDOW_WIDTH // 2, 70))

        screen.blit(score_surf, score_rect)
        screen.blit(config_surf, config_rect)

    def point_to_player(self):
        self.score_player += 1

    def point_to_ai(self):
        self.score_ai += 1
