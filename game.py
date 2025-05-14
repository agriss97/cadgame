import pygame

pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_img = pygame.image.load("bird.png")
pipe_img = pygame.image.load("pipe.png")
bg_img = pygame.image.load("background.png")

# Bird attributes
bird_x, bird_y = 50, HEIGHT // 2
gravity = 0.5
bird_velocity = 0

# Pipe attributes
pipe_width = 70
pipe_gap = 150
pipe_speed = 3
pipes = [{"x": 300, "y": 400}]

def move_bird():
    global bird_y, bird_velocity
    bird_velocity += gravity
    bird_y += bird_velocity

def handle_input():
    global bird_velocity
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_velocity = -7  # Bird jumps
    return True

import random

def move_pipes():
    for pipe in pipes:
        pipe["x"] -= pipe_speed  # Move pipes left
    if pipes[0]["x"] < -pipe_width:
        pipes.pop(0)
        pipes.append({"x": WIDTH, "y": random.randint(200, 400)})

def check_collision():
    if bird_y >= HEIGHT or bird_y <= 0:
        return True
    for pipe in pipes:
        if bird_x < pipe["x"] + pipe_width and bird_x + 34 > pipe["x"]:  # 34 is bird width
            if bird_y < pipe["y"] or bird_y > pipe["y"] + pipe_gap:
                return True
    return False

def draw_game():
    screen.blit(bg_img, (0, 0))
    for pipe in pipes:
        screen.blit(pipe_img, (pipe["x"], pipe["y"] - 300))  # Top pipe
        screen.blit(pipe_img, (pipe["x"], pipe["y"] + pipe_gap))  # Bottom pipe
    screen.blit(bird_img, (bird_x, bird_y))
    pygame.display.update()

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(30)  # FPS
    running = handle_input()
    move_bird()
    move_pipes()
    if check_collision():
        break  # Game over
    draw_game()

pygame.quit()