import sys, pygame

WIDTH, HEIGHT = 768, 1024
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (80, 200, 150)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham's Line Algorithm")

def draw_line_bresenham(x1, y1, x2, y2):
    x1,x2,y1,y2 = int(x1),int(x2),int(y1),int(y2)
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if x2 > x1:
        lx = 1
    else:
        lx = -1

    if y2 > y1:
        ly = 1
    else:
        ly = -1

    x,y = x1,y1

    if dx>dy:
        p = 2 * dy - dx
        for k in range(dx):
            screen.set_at((x,y), WHITE)
            if p < 0:
                x += lx
                p += 2*dy
            else:
                x += lx
                y += ly
                p += 2*dy - 2*dx
    else:
        p = 2*dx - dy
        for k in range(dy):
            screen.set_at((x,y), WHITE)
            if p < 0:
                y += ly
                p += 2*dx
            else:
                x += lx
                y += ly
                p += 2*dx - 2*dy

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(GREEN)

        # Draw football field lines
        # outer lines
        draw_line_bresenham(50, 50, WIDTH-50, 50)
        draw_line_bresenham(50, 50, 50, HEIGHT-50)
        draw_line_bresenham(WIDTH-50, 50, WIDTH-50, HEIGHT-50)
        draw_line_bresenham(50, HEIGHT-50, WIDTH-50, HEIGHT-50)

        #centre
        draw_line_bresenham(50, HEIGHT/2, WIDTH-50, HEIGHT/2)

        #inner lines
        #upper
        draw_line_bresenham(WIDTH/2-200, 50, WIDTH/2-200, HEIGHT/4)
        draw_line_bresenham(WIDTH/2+200, 50, WIDTH/2+200, HEIGHT/4)
        draw_line_bresenham(WIDTH/2-200, HEIGHT/4, WIDTH/2+200, HEIGHT/4)
        #upperinner
        draw_line_bresenham(WIDTH/2-150, 50, WIDTH/2-150, HEIGHT/4-75)
        draw_line_bresenham(WIDTH/2+150, 50, WIDTH/2+150, HEIGHT/4-75)
        draw_line_bresenham(WIDTH/2-150, HEIGHT/4-75, WIDTH/2+150, HEIGHT/4-75)

        #lower
        draw_line_bresenham(WIDTH/2-200, HEIGHT-HEIGHT/4, WIDTH/2-200, HEIGHT-50)
        draw_line_bresenham(WIDTH/2+200, HEIGHT-HEIGHT/4, WIDTH/2+200, HEIGHT-50)
        draw_line_bresenham(WIDTH/2-200, HEIGHT-HEIGHT/4, WIDTH/2+200, HEIGHT-HEIGHT/4)
        #lower inner
        draw_line_bresenham(WIDTH/2-150, HEIGHT-HEIGHT/4+75, WIDTH/2-150, HEIGHT-50)
        draw_line_bresenham(WIDTH/2+150, HEIGHT-HEIGHT/4+75, WIDTH/2+150, HEIGHT-50)
        draw_line_bresenham(WIDTH/2-150, HEIGHT-HEIGHT/4+75, WIDTH/2+150, HEIGHT-HEIGHT/4+75)

        pygame.draw.circle(screen, WHITE, (WIDTH/2, HEIGHT/2), 100, 1)
        pygame.display.update()



if __name__ == "__main__":
    main()
