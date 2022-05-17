import pygame
import random 
from .config import *

class Feliz(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)


		self.image = pygame.image.load('images/image_feliz.png')

		self.rect = self.image.get_rect()

		self.rect.center = (100, HEIGHT//2)

		self.pos_y = self.rect.bottom