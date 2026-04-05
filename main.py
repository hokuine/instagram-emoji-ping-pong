
import pygame
import random

emoji = input("What emoji you want to use?\n-> ")

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

PAD_WIDTH = 100
PAD_HEIGHT = 20
SCREEN_WIDTH_HALF = screen.get_width() / 2
SCREEN_HEIGHT_HALF = screen.get_height() / 2

DT = 0
FPS=360

yellow=(253, 253, 150)

running = True
BALL_SPEED = 700
bat_pos = pygame.Vector2(screen.get_width() / 2, 750)

ball_pos = pygame.Vector2(250, 600)
font2 = pygame.font.SysFont("Segoe UI Emoji", 20)
ball = font2.render(emoji, True, "black")

ball_random_vector = pygame.Vector2(random.choice([-1, 1]), random.uniform(-1, -0.25))
BALL_VEL = ball_random_vector.normalize() * BALL_SPEED

font=pygame.font.Font("freesansbold.ttf", 20)


score = 0

def handle_input():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bat_pos.x -= 1000 * DT
    if keys[pygame.K_a]: 
        bat_pos.x -= 1000 * DT

    if keys[pygame.K_RIGHT]:
        bat_pos.x += 1000 * DT
    if keys[pygame.K_d]: 
        bat_pos.x += 1000 * DT

def physics():
    #restrict movement
    bat_pos.x = max(0, min(bat_pos.x, SCREEN_WIDTH - PAD_WIDTH))
    ball_pos.y = max(0, min(ball_pos.y, 775))


    #bounces off wall with this it reverses the y or x vector component
    if ball_pos.x <= 0 or ball_pos.x >= 480:
        BALL_VEL.x *= -1

    if ball_pos.y <= 0 or ball_pos.y >= 775:
        BALL_VEL.y *= -1

def draw():
    position = font.render(f"Score: {score}", True, "black")
    bposition = font.render(f"X: {int(ball_pos.x)} | Y: {int(ball_pos.y)}", True, "black")
    screen.fill(yellow)
    screen.blit(position, (20, 20))
    screen.blit(bposition, (SCREEN_WIDTH_HALF, 20))
    screen.blit(ball, ball_pos)
    pygame.draw.rect(screen, "black", (bat_pos.x, bat_pos.y,  PAD_WIDTH, PAD_HEIGHT))

def game_over():
    over_screen=font.render(f"Game Over | Your score was: {score}\nPress R to retry", True, "black")
    rect = over_screen.get_rect(center=(SCREEN_WIDTH_HALF, SCREEN_HEIGHT_HALF))
    screen.blit(over_screen, rect)
    
game_running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and not game_running:
                game_running = True
                score = 0
                ball_pos.update(250, 600)


    physics()
    draw()
    handle_input()
    if game_running:
        ball_pos += BALL_VEL * DT



    paddle_rect = pygame.Rect(bat_pos.x, bat_pos.y, PAD_WIDTH, PAD_HEIGHT)
    ball_rect = ball.get_rect(topleft=ball_pos)
    # if ball_rect.colliderect(paddle_rect) and BALL_VEL.y > 0:
    #     BALL_VEL.y *= -1
    #     score += 1

    # if ball_rect.colliderect(paddle_rect) and BALL_VEL.y > 0:
    #     if ball_rect.bottom <= paddle_rect.top + 25:
    #         ball_pos.y = bat_pos.y - 20
            
    #         offset = (ball_rect.centerx - paddle_rect.centerx) / (PAD_WIDTH / 2)

    #         BALL_VEL.x = offset * BALL_SPEED
    #         BALL_VEL.y *= -1

    #         BALL_VEL += BALL_VEL.normalize() * 10
    #         score += 1
    if ball_rect.colliderect(paddle_rect) and BALL_VEL.y > 0:

        ball_pos.y = bat_pos.y - ball_rect.height

        offset = (ball_rect.centerx - paddle_rect.centerx) / (PAD_WIDTH / 2)

        direction = pygame.Vector2(offset, -1)
        BALL_VEL = direction.normalize() * BALL_SPEED

        score += 1

    if ball_pos.y >= 775:
        game_over()
        game_running = False

    pygame.display.flip()

    DT = clock.tick(FPS) / 1000 #120 DT

pygame.quit()
