import sys, pygame


WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Ellipse Algorithm")

def plot_points(x,y,xc,yc):
    screen.set_at((x+xc, y+yc), WHITE)
    screen.set_at((-x+xc, y+yc), WHITE)
    screen.set_at((x+xc, -y+yc), WHITE)
    screen.set_at((-x+xc, -y+yc), WHITE)


def draw_ellipse(rx, ry, xc, yc):

    x, y = 0, ry

    p1 = ry*ry + 0.25*rx*rx - rx*rx*ry

    while 2*ry*ry*x <= 2*rx*rx*y:
        plot_points(x, y, xc, yc)
        if p1 < 0:
            x+=1
            p1+= 2*ry*ry*x + ry*ry
        else:
            x+=1
            y-=1
            p1+= 2*ry*ry*x - 2*rx*rx*y + ry*ry

    p2 = ry*ry*(x+0.5)*(x+0.5) + rx*rx*(y-1)*(y-1) - rx*rx*ry*ry

    while y!=0:
        plot_points(x, y, xc, yc)
        if p2>0:
            y-=1
            p2+= rx*rx - 2*rx*rx*y
        else:
            x+=1
            y-=1
            p2+= 2*ry*ry*x - 2*rx*rx*y + rx*rx


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)


        draw_ellipse(200, 100, 300, 300)


        pygame.display.flip()


if __name__ == "__main__":
    main()
