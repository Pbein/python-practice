# file: main.py

import pygame

# Initialize pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame")

# Colors
WHITE = (255,255,255)

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill(WHITE)
    pygame.display.flip()

pygame.quit()
