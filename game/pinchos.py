import pygame
from .config import *

class Pincho(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('images/pinchos_multiples.png')

		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0

	def collide_with(self, sprites):
		objects = pygame.sprite.spritecollide(self, sprites, False)
		if objects:
			return objects[0]
