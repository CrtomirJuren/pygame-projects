"""
Game Template

Attributes:
    g (TYPE): Description
"""

import pygame as pg # rename for fast typing
import random
from settings import *

class Game:

	"""Summary
	
	Attributes:
	    all_sprites (TYPE): Description
	    clock (TYPE): Description
	    playing (bool): Description
	    running (bool): Description
	    screen (TYPE): Description
	"""

	def __init__(self):
		"""initialize game window, etc
		"""
		pg.init()
		pg.mixer.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		pg.display.set_caption("My Game")
		self.clock = pg.time.Clock()
		self.running = True

	def new(self):
		"""Start a New Game
		"""
		self.all_sprites = pg.sprite.Group()

	def run(self):
		"""Game Loop
		"""
		self.playing = True
		while  self.playing:
			self.clock.tick(FPS) # keep looping at the right speed
			self.events()
			self.update()
			self.draw()

	def update(self):
		"""Game Loop - Update
		"""
		self.all_sprites.update()


	def events(self):
		"""Game Loop - events
		"""
		for event in pg.event.get():
			#check for closing window
			if (event.type == pg.QUIT) or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
				if self.playing:
					self.playing = False
				self.running = False

	def draw(self):
		"""Game Loop - draw
		"""
		self.screen.fill(BLACK)
		self.all_sprites.draw(self.screen)
		pg.display.flip() # after drawing everything, flip the display

	def show_start_screen(self):
		"""game splash/start screen
		"""
		print("game start")
		pass

	def show_go_screen(self):
		"""game over/continue screen
		"""
		print("game end")
		pass

g = Game() # instance of game object
g.show_start_screen()
while g.running:
	g.new()
	g.run()
	g.show_go_screen()

pg.quit()

