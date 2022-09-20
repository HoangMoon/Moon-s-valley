import pygame
from settings import *

class Generic(pygame.sprite.Sprite):
	def __init__(self, pos, surf, groups, z = LAYER['main']):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(topleft = pos)
		self.z = z
class Water(Generic):
	def __int__(self, pos, frames, groups):

		#animation setup
		self.frames = frames
		self.frames_index = 0

		#sprite setup

		super().__init__(
			pos = pos,
			surf= self.frames[self.frames_index],
			groups= groups,
			z= LAYER['water'])
		