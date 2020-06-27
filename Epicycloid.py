import pygame
import os
import math

os.environ["SDL_VIDEO_CENTERED"]='1'

width, height = 1920, 1080
white, black = (230, 230, 230), (15, 15, 15)
orange, red = (255, 123, 0), (255, 23, 46)
blue = (0, 166, 255)
size = (width, height)

pygame.display.set_caption("Cardioid")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

fps = 60
radius1 = 150
radius2 = 75
previous = 1
center_circle = (width//2, height//2)
cardioid = []
angle = 0
def translate(value, min1, max1, min2, max2):
    return min2 + (max2 - min2)* ((value-min1)/(max1-min1))
run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.circle(screen, white, center_circle, radius1, 3)



    mouse = pygame.mouse.get_pos()
    pos = int(translate(mouse[0], 0, width, 0, 6))

    if pos <= 0:
        pos = 1
    if previous != pos:
        screen.fill(black)
        cardioid.clear()

    radius2 = int(radius1/int(pos))
    x1 = int((radius1+radius2) * math.cos(angle)) + center_circle[0]
    y1 = int((radius1+radius2) * math.sin(angle)) + center_circle[1]

    x2 = int(-radius2 * math.cos((radius1+radius2) * angle/radius2 )) + x1
    y2 = int(-radius2 * math.sin((radius1+radius2) * angle/radius2 )) + y1

    x = int((radius1+radius2) * math.cos(angle) - radius2 * math.cos(((radius1+radius2)/radius2 ) * angle) )+ width//2
    y = int((radius1+radius2) * math.sin(angle) - radius2 * math.sin(((radius1+radius2)/radius2 ) * angle) )+ height//2

    cardioid.append((x, y))
    # pygame.draw.circle(screen, green, (int(x)+radius2, int(y)+radius2), radius2, 3)

    if len(cardioid) > 2:
        pygame.draw.lines(screen, orange, False, cardioid, 3)
    pygame.draw.circle(screen, blue, (int(x1), int(y1)), radius2, 2)
    pygame.draw.circle(screen, red, (x2, y2), 10)



    angle += 0.01
    previous = pos
    pygame.display.update()

pygame.quit()
