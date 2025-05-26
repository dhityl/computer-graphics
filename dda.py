import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1280, 1024
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("DDA Line Algorithm")

def draw_line_dda(x1,y1,x2,y2):

    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        step = abs(dx)
    else:
        step = abs(dy)
        
    xinc = dx/step
    yinc = dy/step

    x, y  = x1, y1
    screen.set_at((round(x), round(y)), WHITE)

    while x!=x2 or y!=y2:
        x += xinc
        y += yinc
        screen.set_at((round(x), round(y)), WHITE)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        draw_line_dda(200, 800, 1000 , 400) # Call with coordinates for the line to draw
        pygame.display.flip()

if __name__ == "__main__":
    main()
