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

    for i in range(int(step)):
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


        #make a house with dda lines
        #roof
        draw_line_dda(50, HEIGHT/3,  WIDTH/2, 50)
        draw_line_dda(WIDTH/2, 50, WIDTH-50 , HEIGHT/3)

        #frame
        draw_line_dda(50, HEIGHT/3, WIDTH-50, HEIGHT/3)
        draw_line_dda(50, HEIGHT/3, 50, HEIGHT-50)
        draw_line_dda(50, HEIGHT-50, WIDTH-50, HEIGHT-50)
        draw_line_dda(WIDTH-50, HEIGHT/3, WIDTH-50, HEIGHT-50)

        #door
        draw_line_dda(WIDTH/2-100, HEIGHT-50-400, WIDTH/2-100, HEIGHT-50)
        draw_line_dda(WIDTH/2-100, HEIGHT-50-400, WIDTH/2+100, HEIGHT-50-400)
        draw_line_dda(WIDTH/2+100, HEIGHT-50-400, WIDTH/2+100, HEIGHT-50)
                      
        pygame.display.flip()

if __name__ == "__main__":
    main()
