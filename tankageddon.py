from multiprocessing.connection import wait
import pygame as pygame
import math
pygame.init()

size = width, height = 1280, 720

screen = pygame.display.set_mode(size)

tank1_sprite = pygame.image.load("tank1.png")
tank_width = 40
tank_height = 60
x1 = 100
y1 = 100
rot1 = 0
vel = 5
rot_vel = 5

run = True


def redraw():

    tank1 = pygame.transform.scale(tank1_sprite, (50, 50))
    tank1 = pygame.transform.rotate(tank1, rot1-90)
    print(rot1)

    screen.fill((0, 0, 0))
    screen.blit(tank1, (x1,y1))
    pygame.display.update()


while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rot1 -= rot_vel
    if keys[pygame.K_RIGHT]:
        rot1 += rot_vel
    if keys[pygame.K_UP]:
        y1 += math.sin(math.radians(rot1))*vel
        x1 += math.cos(math.radians(rot1))*vel
    if keys[pygame.K_DOWN]:
        y1 -= math.sin(math.radians(rot1))*vel
        x1 -= math.cos(math.radians(rot1))*vel

    if rot1 < 0:
        rot1 += 360
    if rot1 > 360:
        rot1 -= 360
    
    redraw()

    

pygame.quit()