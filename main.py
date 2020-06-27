import pygame
import os
import math
import random
import colorsys

os.environ["SDL_VIDEO_CENTERED"]='1'

width, height = 1920, 1080
white, black = (230, 230, 230), (15, 15, 15)
size = (width, height)

pygame.display.set_caption("Cardioid")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
total = 10
fps = 60

total = 200
pos = (width//2, height//2)
radius = 500
colors = []
factor = 0
hue = 0
def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def translate(value, min1, max1, min2, max2):
    return min2 + (max2 - min2)* ((value-min1)/(max1-min1))

def get_position(n):
    angle = angle = translate(n%total, 0, total, 0, 2*math.pi)
    x = int(radius * math.cos(angle+math.pi))
    y = int(radius * math.sin(angle+math.pi))
    return (int(x), int(y))

def add_tuple(a, b):
    return (a[0] + b[0], a[1]+ b[1])

run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.circle(screen, white, (pos[0], pos[1]), radius, 1)
    mouse = pygame.mouse.get_pos()

    # mouse control
    total = int(translate(mouse[0], 0, width, 0, 200))

    if total <= 0:
        total = 1

    theta = 2 * math.pi/total

    if hue > 1:
            hue = 0
    for i in range(total):
        position = get_position(i)
        colors.append((random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
        pygame.draw.circle(screen, white, add_tuple(pos, position), 10)

    for i in range(total):
        a, b = get_position(i), get_position(i* factor)
        pygame.draw.line(screen, (hsv2rgb(hue, 1, 1)), add_tuple(a, pos), add_tuple(b, pos), 1)
    pygame.display.update()
    factor += 0.002
    hue += 0.001

pygame.quit()
