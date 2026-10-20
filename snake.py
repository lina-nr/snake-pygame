import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

x = 300
y = 300
dx = 20
dy = 0
snake = [(300, 300)]
food_x = random.randint(0, 29) * 20
food_y = random.randint(0, 29) * 20
score = 0
game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_SPACE:
                x = 300
                y = 300
                dx = 20
                dy = 0
                snake = [(300, 300)]
                food_x = random.randint(0, 29) * 20
                food_y = random.randint(0, 29) * 20
                score = 0
                game_over = False

            if event.key == pygame.K_LEFT and dx != 20:
                dx = -20
                dy = 0
            if event.key == pygame.K_RIGHT and dx != -20:
                dx = 20
                dy = 0
            if event.key == pygame.K_UP and dy != 20:
                dx = 0
                dy = -20
            if event.key == pygame.K_DOWN and dy != -20:
                dx = 0
                dy = 20

    if not game_over:
        x = x + dx
        y = y + dy
        snake.append((x, y))

        if x == food_x and y == food_y:
            food_x = random.randint(0, 29) * 20
            food_y = random.randint(0, 29) * 20
            score = score + 1
        else:
            snake.pop(0)

        if x < 0 or x >= 600 or y < 0 or y >= 600:
            game_over = True
        if (x, y) in snake[:-1]:
            game_over = True

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, 20, 20))
    for (sx, sy) in snake:
        pygame.draw.rect(screen, (0, 255, 0), (sx, sy, 20, 20))

    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    if game_over:
        over = font.render("Game over - press SPACE", True, (255, 255, 255))
        screen.blit(over, (150, 285))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()