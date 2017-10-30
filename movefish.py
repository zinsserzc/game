import pygame
from pygame import *
from sys import exit

background_image_name = "images/background.jpg"
fish_image_name = "images/fugu.png"

SCREEN_SIZE = (640,480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)

#设置帧率
clock = pygame.time.Clock()
time_passed = clock.tick()

x = 0
background_surface = pygame.image.load(background_image_name).convert()
fish_surface = pygame.image.load(fish_image_name)

while True:

    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background_surface,(0,0))
    screen.blit(fish_surface,(x,100))
    x += 10
    if x > 640:
        x = -fish_surface.get_width()/2
    pygame.display.update()