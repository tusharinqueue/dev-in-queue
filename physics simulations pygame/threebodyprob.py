import pygame
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

G = 20  # STRONG gravity

bodies = [
    {"x": 350, "y": 300, "vx": 0, "vy": 0, "mass": 20, "color": (255, 0, 0)},
    {"x": 450, "y": 300, "vx": 0, "vy": 0, "mass": 20, "color": (0, 255, 0)},
    {"x": 400, "y": 450, "vx": 0, "vy": 0, "mass": 20, "color": (0, 0, 255)}
]

running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # PHYSICS
    for i in range(len(bodies)):
        fx, fy = 0, 0

        for j in range(len(bodies)):
            if i == j:
                continue

            dx = bodies[j]["x"] - bodies[i]["x"]
            dy = bodies[j]["y"] - bodies[i]["y"]
            dist = math.hypot(dx, dy) + 0.1

            force = G * bodies[i]["mass"] * bodies[j]["mass"] / (dist ** 2)
            angle = math.atan2(dy, dx)

            fx += math.cos(angle) * force
            fy += math.sin(angle) * force

        bodies[i]["vx"] += fx / bodies[i]["mass"]
        bodies[i]["vy"] += fy / bodies[i]["mass"]

    # UPDATE POSITIONS
    for b in bodies:
        b["x"] += b["vx"]
        b["y"] += b["vy"]
        pygame.draw.circle(screen, b["color"], (int(b["x"]), int(b["y"])), 6)

    pygame.display.flip()

pygame.quit()
