import pygame
from pygame import *
from Tools.Vector2D import Vector2D


class TestWorld(object):
    #初始化空地图
    def __init__(self, world_image):
        #存放地图上的物体
        self.objects = []
        self.main_object = object
        self.world_image = pygame.image.load(world_image)
        self.width = self.world_image.get_width()
        self.height = self.world_image.get_height()
        self.speed = 1
        self.position = (0, 0)

    def add_object(self, object_add):
        self.objects.append(object_add)
        object_add.world = self

    def delete_object(self, object_del):
        self.objects.remove(object_del)

    def set_main_object(self, object_main):
        self.main_object = object_main
        self.speed = object_main.speed

    def move_to(self, destination):
        direction = Vector2D.from_to(self.position, destination).normalize()
        x = self.position[0] + direction.x * self.speed
        y = self.position[1] + direction.y * self.speed
        self.position = (x, y)

if __name__ == "__main__":
    world = TestWorld("../images/background.jpg")