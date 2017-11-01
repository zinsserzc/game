from worlds.TestWorld import TestWorld
from objects.SimpleObject import SimpleObject
from pygame import *
from sys import exit

SCREEN_SIZE = (640, 480)
background_image_name = "images/background.jpg"
object_image = "images/fugu.png"

world = TestWorld(background_image_name)
role = SimpleObject(object_image, (1, 1))
world.add_object(role)
world.set_main_object(role)

current_world = world

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,RESIZABLE,32)
world_surface = world.world_image.convert()
role_surface = role.role_image.convert_alpha()

screen.blit(world_surface, (0, 0))
screen.blit(role_surface, role.position)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE,RESIZABLE,32)