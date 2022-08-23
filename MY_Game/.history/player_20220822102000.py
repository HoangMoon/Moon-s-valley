import pygame
from settings import*

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.Surface((32, 64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)



    #movement attributes
        self.direction = pygame.math.Vector2()
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = -1
        elif keys[pygame.K_LEFT]:
            self.direction.x = 1

    def update(self, dt):
        self.input() 