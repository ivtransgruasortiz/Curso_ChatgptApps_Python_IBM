# main.py

import pygame
from constants import *
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pong vs IA (Ajustable)")
    clock = pygame.time.Clock()

    # Parámetros ajustables
    ball_speed = 5
    paddle_speed = 5
    difficulty = 7
    paused = False

    # Objetos del juego
    player = Paddle(20, (WINDOW_HEIGHT - PADDLE_HEIGHT) // 2, speed=paddle_speed)
    ai = Paddle(WINDOW_WIDTH - 30, (WINDOW_HEIGHT - PADDLE_HEIGHT) // 2, speed=6)
    ball = Ball(speed=ball_speed)
    scoreboard = Scoreboard()
    font = pygame.font.SysFont("Arial", 72)

    running = True
    while running:
        screen.fill(BLACK)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Pulsar P para pausar/reanudar
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused = not paused

        keys = pygame.key.get_pressed()

        # Ajustes de velocidad y dificultad (permitidos incluso en pausa)
        if keys[pygame.K_q]:
            ball_speed = max(MIN_SPEED, ball_speed - 1)
            ball.update_speed(ball_speed)
            pygame.time.wait(150)
        if keys[pygame.K_w]:
            ball_speed = min(MAX_SPEED, ball_speed + 1)
            ball.update_speed(ball_speed)
            pygame.time.wait(150)

        if keys[pygame.K_a]:
            paddle_speed = max(MIN_SPEED, paddle_speed - 1)
            player.speed = paddle_speed
            pygame.time.wait(150)
        if keys[pygame.K_s]:
            paddle_speed = min(MAX_SPEED, paddle_speed + 1)
            player.speed = paddle_speed
            pygame.time.wait(150)

        if keys[pygame.K_z]:
            difficulty = max(1, difficulty - 1)
            pygame.time.wait(150)
        if keys[pygame.K_x]:
            difficulty = min(10, difficulty + 1)
            pygame.time.wait(150)

        # Movimiento solo si el juego no está en pausa
        if not paused:
            # Movimiento jugador
            if keys[pygame.K_UP]:
                player.move(up=True)
            if keys[pygame.K_DOWN]:
                player.move(up=False)

            # Movimiento IA con dificultad
            ai.auto_move(ball.rect.centery, difficulty=difficulty)

            # Movimiento pelota
            ball.move()

            # Colisiones
            if ball.rect.colliderect(player.rect) or ball.rect.colliderect(ai.rect):
                ball.speed_x *= -1

            # Puntos
            if ball.rect.left <= 0:
                scoreboard.point_to_ai()
                ball.reset()
            elif ball.rect.right >= WINDOW_WIDTH:
                scoreboard.point_to_player()
                ball.reset()

        # Dibujar objetos
        player.draw(screen)
        ai.draw(screen)
        ball.draw(screen)
        scoreboard.draw(screen, ball_speed, paddle_speed, difficulty)

        # Mostrar mensaje de pausa si aplica
        if paused:
            pause_text = font.render("PAUSA", True, WHITE)
            pause_rect = pause_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            screen.blit(pause_text, pause_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
