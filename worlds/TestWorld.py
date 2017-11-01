import pygame
from pygame import *


class TestWorld(object):
    #初始化空地图
    def __init__(self, world_image):
        #存放地图上的物体
        self.objects = []
        self.main_object = object
        self.world_image = pygame.image.load(world_image)
        self.width = self.world_image.get_width()
        self.height = self.world_image.get_height()

    def add_object(self, object_add):
        self.objects += object_add

    def delete_object(self, object_del):
        self.objects.remove(object_del)

    def set_main_object(self, object_main):
        self.main_object = object_main

if __name__ == "__main__":
    world = TestWorld("../images/background.jpg")