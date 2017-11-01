import pygame
from pygame import *


class AllObject(object):

    def __init__(self,image):
        self.image = pygame.image.load(image)
        self.width = image.get_width()
        self.height = image.get_height()