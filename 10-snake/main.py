# main.py

import pygame
from constants import *
from snake import Snake
from food import Food
from wall import Wall
from scoreboard import Scoreboard

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    def reset_game():
        return Snake(), Food(), Wall(), Scoreboard(), False, DEFAULT_SPEED

    DEFAULT_SPEED = 5
    snake, food, wall, scoreboard, game_over, speed = reset_game()

    running = True
    while running:
        screen.fill(BLACK)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Cambiar velocidad
        if keys[pygame.K_z]:
            speed = max(1, speed - 1)
            pygame.time.wait(100)
        if keys[pygame.K_x]:
            speed = min(10, speed + 1)
            pygame.time.wait(100)

        if not game_over:
            # Movimiento
            if keys[pygame.K_UP]:
                snake.change_direction((0, -1))
            elif keys[pygame.K_DOWN]:
                snake.change_direction((0, 1))
            elif keys[pygame.K_LEFT]:
                snake.change_direction((-1, 0))
            elif keys[pygame.K_RIGHT]:
                snake.change_direction((1, 0))

            snake.move()

            # Colisiones
            if snake.check_collision() or wall.is_collision(snake.get_head()):
                game_over = True

            if snake.get_head() == food.position:
                snake.grow()
                food = Food()
                scoreboard.increase()

        else:
            # Reiniciar con tecla R
            if keys[pygame.K_r]:
                snake, food, wall, scoreboard, game_over, speed = reset_game()
                pygame.time.wait(150)

        # Dibujar todo
        wall.draw(screen)
        snake.draw(screen)
        food.draw(screen)
        scoreboard.draw(screen, speed, game_over)

        pygame.display.flip()
        clock.tick(speed + 5)

    pygame.quit()

if __name__ == "__main__":
    main()
