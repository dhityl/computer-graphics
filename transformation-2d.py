import sys, pygame
import numpy as np


WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 200, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Dimensional Transformation")


def translate(x,y,tx,ty):
    initial = np.array([x,y,1])
    transformation = np.array([[1,0,tx], [0,1,ty], [0,0,1]])
    result = np.matmul(transformation, initial)

    return np.array([result[0], result[1]])


def scale(x,y,sx,sy):
    initial = np.array([x,y,1])
    transformation = np.array([[sx,0,0], [0,sy,0], [0,0,1]])
    result = np.matmul(transformation, initial)

    return np.array([result[0], result[1]])


def rotate(x,y,theta):
    initial = np.array([x,y,1])
    transformation = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0,0,1]])
    result = np.matmul(transformation, initial)

    return np.array([result[0], result[1]])


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)

        x1, y1 = 100, 100
        x2, y2 = 300, 300
        tx, ty = 150,0
        sx, sy = 1.5, 1.5
        theta = np.radians(40)

        #original line
        pygame.draw.line(screen, WHITE, (x1, y1), (x2, y2))

        #translation
        startpos = translate(x1,y1,tx,ty)
        endpos = translate(x2,y2,tx,ty)
        pygame.draw.line(screen, BLUE, startpos, endpos)

        #scaling + translation
        startpos = scale(x1, y1, sx, sy)
        endpos = scale(x2, y2, sx, sy)

        startpos = translate(startpos[0], startpos[1], -75, 50)
        endpos = translate(endpos[0], endpos[1], -75, 50)
        pygame.draw.line(screen, GREEN, startpos, endpos)

        #rotation
        startpos = rotate(x1, y1, theta)
        endpos = rotate(x2, y2, theta)
        pygame.draw.line(screen, RED, startpos, endpos)


        pygame.display.flip()


if __name__ == "__main__":
    main()

