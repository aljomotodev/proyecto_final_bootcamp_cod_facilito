import sys
import pygame
from .config import *
from .pinchos import *
from .player import *
from .ballons import *
from .file_admin import *

class Game:
	def __init__(self):
		pygame.init()

		self.surface = pygame.display.set_mode( (WIDTH, HEIGHT)) 
		pygame.display.set_caption(TITTLE)

		self.running = True

		#objeto para leer y escribir del archivo score.txt
		self.file = fileAdmin()
		self.score_actual = 0

		self.font = pygame.font.match_font(FONT)

	def start(self):
		self.new()
	
	def new(self):
		self.generate_elements()
		self.run()

		#variable para las vidas
		self.vida = 0

	def generate_elements(self):
		self.pincho = Pincho()
		self.codi = Player()
		# self.ballon = Ballon()

		self.sprites = pygame.sprite.Group()
		self.ballons = pygame.sprite.Group()

		self.sprites.add(self.pincho)
		self.sprites.add(self.codi)
		# self.sprites.add(self.ballon)

		self.generate_ballons()

	def generate_ballons(self):

		if len(self.ballons) < MAX_BALLONS: #si no existen ballons

			# for b in range(0,MAX_BALLONS):
			ballon = Ballon()
			self.sprites.add(ballon)
			self.ballons.add(ballon)



	def run(self):
		while self.running:
			self.events() 
			self.draw()
			self.update()

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
				self.stop()
				pygame.quit()
				sys.exit()
			
		
		pressed = pygame.key.get_pressed()

		if pressed[pygame.K_w]:
			self.codi.rect.y -=5

		if pressed[pygame.K_d]:
			self.codi.rect.x +=5

		if pressed[pygame.K_s]:
			self.codi.rect.y +=5

		if pressed[pygame.K_a]:
			self.codi.rect.x -=5

	def draw(self):
		self.surface.fill(BLUE)

		self.draw_text()

		self.sprites.draw(self.surface)

	def update(self):
		pygame.display.flip()

		self.sprites.update()

		ballon = self.codi.collide_with(self.ballons)
		if ballon:
			ballon.kill()
			self.generate_ballons()
			self.score_actual += 1

		ballon_pincho = self.pincho.collide_with(self.ballons)
		if ballon_pincho:
			ballon_pincho.kill()
			self.generate_ballons()
			self.score_actual = 0


	def stop(self):
		
		last_score = int(self.file.readFile())
		if self.score_actual > last_score:
			self.file.writeFile(str(self.score_actual))

		

	def display_text(self, text, size, color, pos_x, pos_y):
		font = pygame.font.Font(self.font, size)

		text = font.render(text, True, color)
		rect = text.get_rect()
		rect.midtop = (pos_x, pos_y)

		self.surface.blit(text, rect)

	def draw_text(self):
		self.display_text('Last Score: ' + self.file.readFile(), 36, WHITE, 100, 80)
		self.display_text('Actual Score: ' + str(self.score_actual), 36, WHITE, 100, 120)

		



	