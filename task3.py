import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

BALL_RADIUS = 25
BALL_X, BALL_Y = WIDTH // 2, HEIGHT // 2
STEP = 20

running = True
while running:
    pygame.time.delay(50)
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (BALL_X, BALL_Y), BALL_RADIUS)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and BALL_Y - BALL_RADIUS - STEP >= 0:
                BALL_Y -= STEP
            elif event.key == pygame.K_DOWN and BALL_Y + BALL_RADIUS + STEP <= HEIGHT:
                BALL_Y += STEP
            elif event.key == pygame.K_LEFT and BALL_X - BALL_RADIUS - STEP >= 0:
                BALL_X -= STEP
            elif event.key == pygame.K_RIGHT and BALL_X + BALL_RADIUS + STEP <= WIDTH:
                BALL_X += STEP

pygame.quit()
