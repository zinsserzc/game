import pygame
from pygame import *
import constants

SCREEN_SIZE = (640,480)

class Testworld(object):
    def __init__(self,screen,image,x,y):
        self.image = image
        self.screen = screen
        self.background = pygame.image.load(image).convert()
        screen.blit(self.background,(x,y))
        pygame.display.update()

    def on_event(self,event):
        if event.type == VIDEORESIZE:
            SCREEN_SIZE = event.size
            screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        self.screen.blit(self.background,(0,0))

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE,RESIZABLE,32)
    image_name = '../images/background.jpg'
    game = Testworld(screen,image_name,0,0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        game.on_event(event)
        pygame.display.update()