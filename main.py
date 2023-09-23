# file: main.py

import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0) 

# Set up display and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Collect and Dodge')
clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.size = 30
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed = 5

    def draw(self):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.size)

    def move(self, key):
        if key[pygame.K_UP]:
            self.y -= self.speed
        if key[pygame.K_DOWN]:
            self.y += self.speed
        if key[pygame.K_LEFT]:
            self.x -= self.speed
        if key[pygame.K_RIGHT]:
            self.x += self.speed

class Collectible:
    def __init__(self):
        self.size = 15
        self.x = random.randint(self.size, WIDTH - self.size)
        self.y = random.randint(self.size, HEIGHT - self.size)

    def draw(self):
        pygame.draw.circle(screen, GREEN, (self.x, self.y), self.size)

class Obstacle:
    def __init__(self):
        self.width = 40
        self.height = 60
        self.x = random.randint(0, WIDTH - self.width)
        self.y = random.randint(0, HEIGHT - self.height)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

player = Player()
collectibles = [Collectible() for _ in range(5)]
obstacles = [Obstacle() for _ in range(3)]
score = 0

font = pygame.font.SysFont(None, 55)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    screen.fill(WHITE)

    player.draw()
    for c in collectibles:
        c.draw()

    for o in obstacles:
        o.draw()

    # Check for collisions with collectibles
    for c in collectibles:
        if player.x - player.size < c.x < player.x + player.size and player.y - player.size < c.y < player.y + player.size:
            score += 1
            collectibles.remove(c)
            collectibles.append(Collectible())

    #Check for collisions with obstacles
    for o in obstacles:
        if (player.x - player.size < o.x + o.width and player.x + player.size > o.x and player.y - player.size < o.y + o.height and player.y + player.size > o.y):
            running = False

    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10,10))

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
