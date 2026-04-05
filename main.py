
import pygame
import random

emoji ="❤️" #input("What emoji you want to use?\n-> ")

pygame.init()
screen = pygame.display.set_mode((500, 800))
clock = pygame.time.Clock()

PAD_WIDTH = 100
PAD_HEIGHT = 20
running = True
dt = 0
yellow=(253, 253, 150)


BALL_SPEED = 400
bat_pos = pygame.Vector2(screen.get_width() / 2, 750)

ball_pos = pygame.Vector2(250, 600)
font2 = pygame.font.SysFont("Segoe UI Emoji", 20)
ball = font2.render(emoji, True, "black")

ball_random_vector = pygame.Vector2(random.choice([-1, 1]), random.uniform(-1, -0.25))
BALL_VEC = ball_random_vector.normalize() * BALL_SPEED

font=pygame.font.Font("freesansbold.ttf", 20)


score = 0

def keys():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        bat_pos.x -= 1000 * dt
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        bat_pos.x += 1000 * dt


def draw():
    position = font.render(f"Score: {score}", True, "black")
    bposition = font.render(f"X: {int(ball_pos.x)} | Y: {int(ball_pos.y)}\nX: {bat_pos.x}", True, "black")
    screen.fill(yellow)
    screen.blit(position, (20, 20))
    screen.blit(bposition, (screen.get_width() / 2, 20))
    screen.blit(ball, ball_pos)
    pygame.draw.rect(screen, "black", (bat_pos.x, bat_pos.y,  PAD_WIDTH, PAD_HEIGHT))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw()
    keys()
    
    ball_pos += BALL_VEC * dt

    if int(ball_pos.y) == 775:
        score += 1
        # print(score)

    #restrict movement
    bat_pos.x = max(0, min(bat_pos.x, 400))
    ball_pos.x = max(0, min(ball_pos.x, 480))
    ball_pos.y = max(0, min(ball_pos.y, 775))
    pygame.display.flip()

    dt = clock.tick(120) / 1000 #120 fps

pygame.quit()
