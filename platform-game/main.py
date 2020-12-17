"""
Doodle Jump

Attributes:
    g (TYPE): Description
"""

import pygame as pg
import random
from settings import *
from sprites import *
import os
from os import path

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
		- load data: load graphics, sound, highscore file
		"""
		pg.init()
		pg.mixer.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		self.running = True
		self.playing = True
		#closeste match to our font name
		self.font_name = pg.font.match_font(FONT_NAME)
		self.highscore = 0
		self.load_data()

	def read_highscore_file(self, filename):
		#if file exists, read from it
		if os.path.exists(filename):
			with open(filename, 'r') as f:
				try:
					data = int(f.read())
					return data
				except:
					return 0
		# if file doesnt exists, create new
		else:
			with open(filename, 'w') as f:
				try:
					f.write("0")
					return 0
				except:
					return 0

	def load_data(self):
		""" method for loading date before starting the game
		- get folder directories, build paths for files
		- load graphics
		- load sounds
		- load files: highscore
		"""
		self.dir = path.dirname(__file__) #get application folder path

		# load spritesheet image
		self.img_dir = path.join(self.dir, 'img')
		spritesheet_file = path.join(self.img_dir, SPRITESHEET_FILE)
		self.spritesheet = Spritesheet(spritesheet_file)

		# load high score file
		highscore_file = path.join(self.dir, HIGHSCORE_FILE)
		self.highscore = self.read_highscore_file(highscore_file)

		# load sounds: .ogg files are best
		self.snd_dir = path.join(self.dir, 'snd')
		# load jump sound
		self.jump_snd_file = path.join(self.snd_dir, 'Jump33.wav')
		self.jump_sound = pg.mixer.Sound(self.jump_snd_file)
		self.jump_sound.set_volume(0.2)

	def new(self):
		"""Start a New Game
		"""
		self.score = 0
		#create sprites groups
		self.all_sprites = pg.sprite.Group()

		#create platform group
		self.platforms = pg.sprite.Group()

		#add player to sprites group
		"""create a new instance of Player and send it reference to game object
		so we can access platforms also in player class"""
		self.player = Player(self) #send reference
		self.all_sprites.add(self.player)

		#add platform list to platform group and to sprites group
		for plat in PLATFORM_LIST:
			#p = Platform(plat[0],plat[1],plat[2],plat[3]) same as bottom
			p = Platform(self, *plat) #explode plat list to components
			self.all_sprites.add(p)
			self.platforms.add(p)
		#load music before start of game
		pg.mixer.music.load(path.join(self.snd_dir, 'Happy Tune.ogg'))
	
	def run(self):
		"""Game Loop
		"""
		# start music: infinite loop
		pg.mixer.music.play(loops = -1)
		self.playing = True
		while self.playing:
			self.clock.tick(FPS) # keep looping at the right speed
			self.events()
			self.update()
			self.draw()
		# stop music with fadeout
		pg.mixer.music.fadeout(1000) # 1sec fade

	def update(self):
		"""Game Loop - Update
		- update all sprites
		- checking if player hits platform - only if falling
		-
		"""
		#debug number of platforms, check if deleted properly
		#print(len(self.platforms))
		# update all sprites
		self.all_sprites.update()

		# PLAYER-PLATFORM COLLISION DETECTION - this stops us from falling
		# checking if player hits platform - only if falling
		if self.player.vel.y > 0:
			# do a collision check with platform
			hits = pg.sprite.spritecollide(self.player, self.platforms, False)
			if hits: # hits is a list of multiple collisions
				# find which platform is lowes
				lowest = hits[0]
				for hit in hits:
					if hit.rect.bottom > lowest.rect.bottom:
						lowest = hit
				if self.player.pos.x < lowest.rect.right + 10 and \
					self.player.pos.x > lowest.rect.left - 10:
					#dont snap if the ears touch platform. only feet
					if self.player.pos.y < lowest.rect.bottom:
						self.player.pos.y = lowest.rect.top
						self.player.vel.y = 0
						# when we land on paltform, reset jumping ability
						self.player.jumping = False

		# SCROLING WINDOW
		# if player reaches top 1/4 of screen
		if self.player.rect.top <= HEIGHT/4:
			#litle math for nicer screnn scrolling. take player speed or number 2
			# even if player is not moving, the screen moves until in range
			self.player.pos.y += max(abs(self.player.vel.y),2)
			for plat in self.platforms:
				plat.rect.y += max(abs(self.player.vel.y),2)
				#remove platforms on the bottom
				if plat.rect.top >= HEIGHT:
					plat.kill() #remove bottom ones
					self.score += 1

		# spawn new platforms to keep some avarage number
		while len(self.platforms) < 6:
			#randomize creation of platforms
			width = random.randrange(50, 100)
			p = Platform(self,
				random.randrange(0, WIDTH-width),
				random.randrange(-75, -30))
			self.platforms.add(p)
			self.all_sprites.add(p)

		# GAME OVER
		# Die! and game over condition
		if self.player.rect.bottom > HEIGHT:
			#do a bling when dying- looks like scroling camera
			for sprite in self.all_sprites:
				sprite.rect.y -= max(self.player.vel.y, 10)
				if sprite.rect.bottom < 0:
					sprite.kill()

		if len(self.platforms) == 0:
			self.playing = False

	def events(self):
		"""Game Loop - events
		- close window + escape key event stops game
		"""
		for event in pg.event.get():
			# check for closing window
			if (event.type == pg.QUIT) or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
				if self.playing:
					self.playing = False
				self.running = False
				self.player.vel.y = 0

			# jumping section. jump higher if we hold space
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					self.player.jump()
			if event.type == pg.KEYUP:
				if event.key == pg.K_SPACE:
					self.player.jump_cut()

	def draw(self):
		"""Game Loop - draw
		- fill with background colour
		- draw all sprites
		- draw text score
		- flip everything to display
		"""
		self.screen.fill(BG_COLOR)
		self.all_sprites.draw(self.screen)
		# put player always in front of other stuff
		self.screen.blit(self.player.image, self.player.rect)
		self.draw_text(str(self.score), 22, WHITE, WIDTH_MID, 15)
		pg.display.flip()

	def show_start_screen(self):
		"""game splash/start screen
		"""
		# start playing music
		pg.mixer.music.load(path.join(self.snd_dir, 'Yippee.ogg'))
		pg.mixer.music.set_volume(0.2) # 0 < x < 1
		pg.mixer.music.play(loops = -1)

		self.screen.fill(BG_COLOR)
		self.draw_text(TITLE, 48, WHITE, WIDTH_MID, HEIGHT//4)
		self.draw_text("Arrows to move, Space to jump", 22, WHITE, WIDTH_MID, HEIGHT_MID)
		self.draw_text("Press a key to play", 22, WHITE, WIDTH_MID, HEIGHT*3/4)
		self.draw_text("High score : " + str(self.highscore), 22, WHITE, WIDTH_MID, 15)
		pg.display.flip()
		self.wait_for_key()

		# stop music
		pg.mixer.music.fadeout(1000) # s0.5sec fade

	def show_go_screen(self):
		"""game over/continue screen
		If player presses (X), than ignore game over screen
		Game over screen is called only if a player dies
		- handle highscore file
		"""
		if not self.running:
			return
		# start playing music
		pg.mixer.music.load(path.join(self.snd_dir, 'Yippee.ogg'))
		pg.mixer.music.set_volume(0.2) # 0 < x < 1
		pg.mixer.music.play(loops = -1)

		self.screen.fill(BG_COLOR)
		self.draw_text("GAME OVER", 48, WHITE, WIDTH_MID, HEIGHT//4)
		self.draw_text("Score : "+str(self.score), 22, WHITE, WIDTH_MID, HEIGHT_MID)
		self.draw_text("press a key to play again", 22, WHITE, WIDTH_MID, HEIGHT*3/4)
		# save highscore
		if self.score > self.highscore:
			self.highscore = self.score
			self.draw_text("NEW HIGH SCORE ! CONGRATS", 22, WHITE, WIDTH_MID, HEIGHT_MID + 40)
			with open(path.join(self.dir, HIGHSCORE_FILE), "w") as f:
				f.write(str(self.highscore))
		else:
			self.draw_text("High score : " + str(self.highscore), 22, WHITE, WIDTH_MID, 15)
		pg.display.flip()
		self.wait_for_key()
		# stop music
		pg.mixer.music.fadeout(1000) # s0.5sec fade

	def wait_for_key(self):
		waiting = True
		while waiting:
			self.clock.tick(FPS)
			for event in pg.event.get():
				#check for closing window
				if (event.type == pg.QUIT) or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
					""" this is original, but doesnt close screen at game over
					if self.playing:
						waiting = False
						self.running = False
						self.playing = False
					"""
					waiting = False
					self.running = False
					self.playing = False
				if event.type == pg.KEYUP:
					waiting = False

	def draw_text(self, text, size, color, x, y):
		font = pg.font.Font(self.font_name, size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x, y)
		self.screen.blit(text_surface, text_rect)

#----------------MAIN GAME------------------
g = Game() # instance of game object

g.show_start_screen()
while g.running:
	g.new()
	g.run()
	g.show_go_screen()
pg.quit()

