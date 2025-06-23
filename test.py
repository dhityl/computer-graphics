import sys, pygame
import numpy as np
import math

WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Midpoint Ellipse Algorithm")

angle = 0  # Global angle for ellipse movement

def plot_points(x, y, xc, yc):
    screen.set_at((x + xc, y + yc), WHITE)
    screen.set_at((-x + xc, y + yc), WHITE)
    screen.set_at((x + xc, -y + yc), WHITE)
    screen.set_at((-x + xc, -y + yc), WHITE)

def draw_ellipse(rx, ry, xc, yc):
    x, y = 0, ry
    p1 = ry * ry + 0.25 * rx * rx - rx * rx * ry

    while 2 * ry * ry * x <= 2 * rx * rx * y:
        plot_points(x, y, xc, yc)
        if p1 < 0:
            x += 1
            p1 += 2 * ry * ry * x + ry * ry
        else:
            x += 1
            y -= 1
            p1 += 2 * ry * ry * x - 2 * rx * rx * y + ry * ry

    p2 = ry * ry * (x + 0.5) * (x + 0.5) + rx * rx * (y - 1) * (y - 1) - rx * rx * ry * ry

    while y != 0:
        plot_points(x, y, xc, yc)
        if p2 > 0:
            y -= 1
            p2 += rx * rx - 2 * rx * rx * y
        else:
            x += 1
            y -= 1
            p2 += 2 * ry * ry * x - 2 * rx * rx * y + rx * rx

def draw_circle(xc, yc, r, color=WHITE):
    xc, yc = int(xc), int(yc)
    x = 0
    y = r
    p = 1 - r

    while x <= y:
        screen.set_at((x + xc, y + yc), color)
        screen.set_at((y + xc, x + yc), color)
        screen.set_at((x + xc, -y + yc), color)
        screen.set_at((y + xc, -x + yc), color)
        screen.set_at((-x + xc, y + yc), color)
        screen.set_at((-y + xc, x + yc), color)
        screen.set_at((-x + xc, -y + yc), color)
        screen.set_at((-y + xc, -x + yc), color)

        if p < 0:
            x += 1
            p += 2 * x + 1
        else:
            x += 1
            y -= 1
            p += 2 * x - 2 * y + 1

def draw_circle_fill(xc, yc, r, color=WHITE):
    for radius in range(r + 1):
        draw_circle(xc, yc, radius, color)

def main():
    global angle
    rx, ry = 200, 100
    xc, yc = 300, 300
    orbit_radius = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # Draw static ellipse
        draw_ellipse(rx, ry, xc, yc)

        # Calculate rotating circle position using ellipse parametric equations
        ellipse_x = xc + int(rx * math.cos(angle))
        ellipse_y = yc + int(ry * math.sin(angle))

        # Draw filled circle moving along the ellipse
        draw_circle_fill(ellipse_x, ellipse_y, orbit_radius)

        # Update angle for rotation
        angle += 0.05
        if angle >= 2 * math.pi:
            angle = 0

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
