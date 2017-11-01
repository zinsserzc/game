from worlds.TestWorld import TestWorld
from objects.SimpleObject import SimpleObject
from pygame import *
from sys import exit
import pygame

SCREEN_SIZE = (640, 480)
background_image_name = "images/background.jpg"
object_image = "images/fugu.png"

world = TestWorld(background_image_name)
role = SimpleObject(object_image, (1, 1))
world.add_object(role)
world.set_main_object(role)

current_world = world

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,RESIZABLE,32)
world_surface = world.world_image.convert()
role_surface = role.role_image.convert_alpha()

screen.blit(world_surface, world.position)
screen.blit(role_surface, role.position)

while True:

    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE,RESIZABLE,32)

    pressed_mouse = pygame.mouse.get_pressed()
    #print(pressed_mouse)  get_pressed() 返回的是一个三维 tuple (0,0,0)
    if pressed_mouse[0] == 1:
        role.move_to(pygame.mouse.get_pos())
        world.move_to((-pygame.mouse.get_pos()[0], -pygame.mouse.get_pos()[1]))

    screen.fill((255, 255, 255))
    screen.blit(world_surface, world.position)
    screen.blit(role_surface, (SCREEN_SIZE[0]/2 - role.width/2, SCREEN_SIZE[1]/2 - role.height/2))

    pygame.display.update()