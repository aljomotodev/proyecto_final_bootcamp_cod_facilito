import pygame
import random 
from .config import *

class Ballon(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('images/globo_azul.png')

		self.rect = self.image.get_rect()
		self.rect.x = random.randint(100, 900)
		self.rect.y = 550

		self.pos_y = self.rect.bottom
	
	def update_pos(self):
		self.pos_y += -3
	
	def update(self):
		self.update_pos()
		
		self.rect.bottom = self.pos_y

	 
