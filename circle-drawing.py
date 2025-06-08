import sys, pygame

WIDTH, HEIGHT = 1000, 1000
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (250, 150, 0)
GRAY = (100, 100, 100)
REDORANGE = (200, 100, 50)
LIGHTBLUE = (60, 140, 200)
RED = (200, 0, 0)
BROWN = (150, 80, 30)
PALEYELLOW = (180, 180, 80)
PALEBLUE = (80, 100, 120)
DEEPBLUE  = (50, 50, 150)



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Circle Algorithm")



def draw_circle(xc, yc, r, color = WHITE):
    xc,yc = int(xc), int(yc)
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
        screen.set_at((-y + xc, -x+ yc), color)

        if p < 0:
            x += 1
            p += 2*x + 1
        else:
            x += 1
            y -= 1
            p += 2*x - 2*y + 1


def draw_circle_fill(xc, yc, r, color = WHITE):
    for x in range(r):
        draw_circle(xc, yc, x, color)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        #sun
        draw_circle_fill(WIDTH/2, HEIGHT/2, 50, ORANGE)

        #draw solar system

        #orbits
        draw_circle(WIDTH/2, HEIGHT/2, 100)
        draw_circle(WIDTH/2, HEIGHT/2, 150)
        draw_circle(WIDTH/2, HEIGHT/2, 200)
        draw_circle(WIDTH/2, HEIGHT/2, 250)
        draw_circle(WIDTH/2, HEIGHT/2, 300)
        draw_circle(WIDTH/2, HEIGHT/2, 350)
        draw_circle(WIDTH/2, HEIGHT/2, 400)
        draw_circle(WIDTH/2, HEIGHT/2, 450)

        #planets
        draw_circle_fill(WIDTH/2 + 100, HEIGHT/2, 10, GRAY) #Mercury
        draw_circle_fill(WIDTH/2, HEIGHT/2 - 150, 15, REDORANGE) #Venus
        draw_circle_fill(WIDTH/2 -200, HEIGHT/2, 15, LIGHTBLUE) #Earth
        draw_circle_fill(WIDTH/2, HEIGHT/2 + 250, 12, RED) #Mars
        draw_circle_fill(WIDTH/2 - 250, HEIGHT/2 - 175, 22, BROWN) #Jupiter
        draw_circle_fill(WIDTH/2 + 220, HEIGHT/2 - 275, 20, PALEYELLOW) #Saturn
        draw_circle_fill(WIDTH/2 + 315, HEIGHT/2 + 250, 16, PALEBLUE) #Uranus
        draw_circle_fill(WIDTH/2 - 315, HEIGHT/2 + 320, 16, DEEPBLUE) #Neptune
        
        pygame.display.update()


if __name__ == "__main__":
    main()
