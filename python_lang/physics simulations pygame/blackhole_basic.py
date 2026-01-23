import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Black hole
bh_x= WIDTH // 2
bh_y =HEIGHT // 2
BH_MASS = 5000

# Particle
particles = []

for _ in range(200):
    particles.append({
        "x": random.randint(0, WIDTH),
        "y": random.randint(0, HEIGHT),
        "vx": random.uniform(-1, 1),
        "vy": random.uniform(-1, 1)
    })

running = True
while running:
    screen.fill((90,79,207))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw black hole
    pygame.draw.circle(screen, (0, 0, 0), (bh_x, bh_y), 15)

    for p in particles:
        dx = bh_x - p["x"]
        dy = bh_y - p["y"]
        dist = math.hypot(dx, dy)

        if dist < 1:
            continue

        force = BH_MASS / (dist ** 2)
        angle = math.atan2(dy, dx)

        p["vx"] += math.cos(angle) * force
        p["vy"] += math.sin(angle) * force

        p["x"] += p["vx"]
        p["y"] += p["vy"]

        pygame.draw.circle(screen, (255, 255, 255), (int(p["x"]), int(p["y"])), 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
