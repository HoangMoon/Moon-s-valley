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
        self.player = Player((640,360), self.all_sprites)
        Generic(
            pos=(0,0),
            surf= pygame.image.load('./graphics/world/ground.png').convert_alpha(),
            groups= self.all_sprites,
            z = LAYER['ground'])

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
        # dùng math.vector2 để tạo hiệu ứng di chuyển 
        self.offset =pygame.math.Vector2()


    def Custom_draw():
        # khi player di chuyển background di chuyển ngược lại của 2 chiều x;y
        self.offset.x = Player.rect.centerx - SCREEN_WIDTH/2
        self.offset.y = Player.rect.centery - SCREEN_HEIGHT/2 


        # use layer to blit the sprite in order
        for layer in LAYER.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect -= self.offset
                    self.display_surface.blit(sprite.image, sprite.rect)