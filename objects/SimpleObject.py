from Tools.Vector2D import Vector2D
import pygame


class SimpleObject(object):
    def __init__(self, role_image, position):
        self.position = position
        self.speed = 1
        self.role_image = pygame.image.load(role_image)
        self.width = self.role_image.get_width()
        self.height = self.role_image.get_height()

    def move_to(self, destination):
        direction = Vector2D.from_to(self.position, destination).normalize()
        x = self.position[0]
        if 0 < x < self.world.width:
            x = self.position[0] + direction.x * self.speed
        y = self.position[1]
        if 0 < y < self.world.height:
            y = self.position[1] + direction.y * self.speed
        self.position = (x, y)
