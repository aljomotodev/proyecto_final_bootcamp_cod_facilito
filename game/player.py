import pygame
from .config import *
from .game import *
from game import pinchos

class Player(pygame.sprite.Sprite):
	# def __init__(self, left, bottom):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('images/codi_fuego.png')
		
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH // 2, HEIGHT // 2)
		# self.rect.left = left
		# self.rect.bottom = bottom
		# self.rect_x = 500
		# self.rect_y = 700 
	
	def collide_with(self, sprites):
		objects = pygame.sprite.spritecollide(self, sprites, False)
		if objects:
			return objects[0]



