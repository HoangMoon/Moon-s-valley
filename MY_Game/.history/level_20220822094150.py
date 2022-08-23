import pygame
from settings import *
from basic_player import Player

class Level:
    def __init__(self):
        #get display surface
        self.display_surface = pygame.display.get_surface()

        #get sprite groups
        self.all_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.all_sprites = Player((640,360), self.all_sprites)

    def run(self,dt):
        self.display_surface.fill('red')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update()