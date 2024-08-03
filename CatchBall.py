import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1380
SCREEN_HEIGHT = 705
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BALL_SIZE = 20
BALL_FALL_SPEED = 5
PADDLE_SPEED = 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Ball")

music = pygame.mixer.music.load("mario.mp3")
pygame.mixer.music.play(-1)

# Set up the clock for timing
clock = pygame.time.Clock()

# Paddle
paddle = pygame.Rect((SCREEN_WIDTH - PADDLE_WIDTH) // 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
ball = pygame.Rect(random.randint(0, SCREEN_WIDTH - BALL_SIZE), 0, BALL_SIZE, BALL_SIZE)

# Score
score = 0

# Font
font = pygame.font.SysFont(None, 36)

def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
        paddle.x += PADDLE_SPEED

    # Update ball position
    ball.y += BALL_FALL_SPEED

    # Check if ball is caught
    if paddle.colliderect(ball):
        score += 1
        ball.x = random.randint(0, SCREEN_WIDTH - BALL_SIZE)
        ball.y = 0

    # Check if ball is missed
    if ball.y > SCREEN_HEIGHT:
        print(f'Game Over! Your final score is {score}')
        running = False

    # Draw everything
    draw_objects()
    clock.tick(30)

pygame.quit()
