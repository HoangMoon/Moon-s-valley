import imp
from tokenize import group


import pygame
from setting import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups): 
        super().__init__(group)


        self.image = pygame.Surface((64,32))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)