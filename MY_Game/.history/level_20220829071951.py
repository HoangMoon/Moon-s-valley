import imp
import pygame
from settings import *
from player import Player
from overlay import Overlay
from sprites import Generic


class Level:
    def __init__(self):
        #get display surface
        self.display_surface = pygame.display.get_surface()

        #get sprite groups
        self.all_sprites = CameraGroup()

        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self):
        Generic(pos=(0,0),
        surf= pygame.image.load('./graphics/world/ground.png').convert_alpha(),
        groups= self.all_sprites,
        z = LAYER['ground'])
        self.player = Player((640,360), self.all_sprites)

    def run(self,dt):
        self.display_surface.fill('black')
        self.all_sprites.Custom_draw()
        self.all_sprites.update(dt)
        self.overlay.display()
 # self.all_sprites.draw(self.display_surface)


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
    
    def Custom_draw(self):
        # use layer to blit the sprite in order
        for layer in LAYER.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    self.display_surface.blit(sprite.image, sprite.rect)