#!/usr/bin/env python
import pygame
from sys import exit
from pygame.locals import *
from random import randint

background_image_filename = 'images/background.jpg'
mouse_image_filename = 'images/fugu.png'

SCREEN_SIZE = (640,480)


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE,RESIZABLE,32)

#标题
pygame.display.set_caption("hello world")

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

#文字
text_content = "willlllllqweqweqwe"
my_font = pygame.font.SysFont("arial",64)
name_surface = my_font.render(text_content,True,(0,0,255),255)
screen.blit(name_surface, (0, 0))

w = background.get_width()
h = background.get_height()
print(w,h)
x = 0
y = 0
fullscreen = False
while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE,RESIZABLE,32)

    if event.type == KEYDOWN:
        print(event)

        if event.key == K_LEFT and x > -w+SCREEN_SIZE[0]:
            x -= 1
        elif event.key == K_RIGHT and x < 0:
            x += 1
        elif event.key == K_UP and  y > -h+SCREEN_SIZE[1]:
            y -= 1
        elif event.key == K_DOWN and y < 0:
            y += 1
        elif event.key == K_f:
            fullscreen = not fullscreen
            if fullscreen:
                screen = pygame.display.set_mode((640,480),pygame.FULLSCREEN,32)
            else:
                screen = pygame.display.set_mode((640,480),0,32)

        print(x,y)

    #rand_col = (randint(0,255),randint(0,255),randint(0,255))
    #screen.lock()
    #for _ in range(100):
        #rand_pos = (randint(0,639),randint(0,479))
        #screen.set_at(rand_pos,rand_col)

    #screen.unlock()
    screen.fill((0,0,0))

    #screen.blit(mouse_cursor,(x,y))

    screen.blit(background, (x,y))



    pygame.display.update()