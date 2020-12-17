"""Sprite classes for platform game

Attributes:
	vec (TYPE): Description
"""
import pygame as pg
import random
from settings import *
vec = pg.math.Vector2

class Spritesheet:

	"""Utility class for loading and parsing spritesheets
	"""
	def __init__(self, filename):
		self.spritesheet = pg.image.load(filename).convert()

	def get_image(self, x, y, width, height):
		image = pg.Surface((width,height))
		# from spritesheet we cut out an image (x, y, width, height)
		image.blit(self.spritesheet, (0,0), (x, y, width, height))
		#resize image
		image = pg.transform.scale(image, (width//2, height//2))
		return image

class  Player(pg.sprite.Sprite):

	"""Summary

	Attributes:
		acc (TYPE): Description
		game (TYPE): Description
		image (TYPE): Description
		pos (TYPE): Description
		rect (TYPE): Description
		vel (TYPE): Description
	"""

	def __init__(self, game):
		"""Summary

		Args:
		    game (TYPE): Description
		"""
		pg.sprite.Sprite.__init__(self)

		self.game = game #this is a copy of game for reference
		self.jumping = False
		self.walking = False
		self.current_frame = False
		self.last_update = False # frame animation
		self.load_images()
		self.image = pg.Surface((30,40))
		#self.image.fill(YELLOW) # YELLOW RECTANGLE PLAYER
		#get image from spritesheet
		#self.image = self.game.spritesheet.get_image(614,1063,120,191)
		# fix color image background problem
		#self.image.set_colorkey(BLACK)

		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH_MID, HEIGHT_MID)
		self.pos = vec(50, HEIGHT_MID) # player spawn location

		self.vel = vec(0,0)
		self.acc = vec(0,0)

	def load_images(self):
		"""Load player images for animation
		- standing
		- walk right
		- walk left
		- jumping
		"""
		# Standing frames
		self.standing_frames = [
		self.game.spritesheet.get_image(614,1063, 120, 191),
		self.game.spritesheet.get_image(690, 406, 120, 201)]
		# fix color image background problem
		for frame in self.standing_frames:
			frame.set_colorkey(BLACK)
		# Walking right frames
		self.walk_frames_r = [
		self.game.spritesheet.get_image(678, 860, 120, 201),
		self.game.spritesheet.get_image(692, 1458, 120, 207)]
		for frame in self.walk_frames_r:
			frame.set_colorkey(BLACK)
		# Walking left frames
		self.walk_frames_l = []
		for frame in self.walk_frames_r:
			#flip(​Surface, flip vertically, flip horizonally)
			self.walk_frames_l.append(pg.transform.flip(frame, True, False))
		# Jumping frames
		self.jump_frame = self.game.spritesheet.get_image(382, 763, 150, 181)
		self.jump_frame.set_colorkey(BLACK)

	def jump_cut(self):
		""" Jump cut
		- when we are jumping we are traveling at 16 speed
		- jump cut, decreases jump velocity
		"""
		if self.jumping:
			if self.vel.y < -3:
				self.vel.y = -3

	def jump(self):
		"""Jump
		Jump only if standing on platform
		Check 2 pixel below if platform is there, than jump allowed
		1. temporary lower player for 2 pixel
		2. check for collision with platform
		3. move player 2 pixel up to original position
		4. if collided, than a player can jump
		"""
		self.rect.x += 2
		hits = pg.sprite.spritecollide(self, self.game.platforms, False)
		self.rect.x -= 2

		if hits and not self.jumping:
			self.jumping = True
			self.vel.y = PLAYER_JUMP_VELOCITY
			self.game.jump_sound.play()

	def update(self):
		""" Update player
		- key press events
		- movement mehanics equations
		- (friction, gravity, acc, vel, pos)
		"""
		self.animate()

		self.acc = vec(0,PLAYER_GRAVITY) # 0.5 is gravity
		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT]:
			self.acc.x = -PLAYER_ACC
		elif keys[pg.K_RIGHT]:
			self.acc.x = PLAYER_ACC

		# boundaries constraints
		# if on RIGTH and if we are deccelerating toward wall
		if self.pos.x - (self.rect.width//2) <= 0:
			if self.vel.x < 0 or self.acc.x < 0:
				self.acc.x = 0
				self.vel.x = 0
		# if on LEFT and if we are accelerating toward wall
		if self.pos.x + (self.rect.width//2) >= WIDTH:
			if self.vel.x > 0 or self.acc.x > 0:
				self.acc.x = 0
				self.vel.x = 0

		self.vel += self.vel*PLAYER_FRICTION
		self.vel += self.acc

		# if because of friction, we stop. its because velocity
		# is rounded to 0. But its not 0. so we use treshold
		if abs(self.vel.x) < 0.1: # if velocity blow 0.1 pixel treshold
			self.vel.x = 0 # force velocity to 0, if too small

		#oon equation deltaX = 0.5*(v0 + v)
		self.pos += self.vel + 0.5*self.acc
		#self.rect.center = self.pos
		self.rect.midbottom = self.pos #player standing on platform

		#position = myFont.render("Position:", 1, WHITE)
		#screen.blit(position, (0, 0))

	def animate(self):
		"""animation is based on time
		- get current time
		"""
		now = pg.time.get_ticks()
		# animation for moving
		# if x velocity is not 0, than we are walking
		if self.vel.x != 0:
			self.walking = True
		else:
			self.walking = False
		# show walk animation
		if self.walking:
			if now - self.last_update > 150:
				self.last_update = now
				self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
				#keep track where our bottom of rectangle is
				#so our character stands on platform
				bottom = self.rect.bottom

				# check direction, right/left
				if self.vel.x > 0: # right walk
					self.image = self.walk_frames_r[self.current_frame]
				else: # left walk
					self.image = self.walk_frames_l[self.current_frame]

				self.rect = self.image.get_rect()
				self.rect.bottom = bottom
		# animation for standing
		if not self.jumping and not self.walking:
			if now - self.last_update > 350:
				self.last_update = now
				self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
				#keep track where our bottom of rectangle is
				#so our character stands on platform
				bottom = self.rect.bottom
				self.image = self.standing_frames[self.current_frame]
				self.rect = self.image.get_rect()
				self.rect.bottom = bottom

class Platform(pg.sprite.Sprite):

	"""Summary

	Attributes:
		image (TYPE): Description
		rect (TYPE): Description
	"""

	def __init__(self, game, x, y):
		"""class to create platform and boundaries
		where we can walk on

		Args:
			x (TYPE): Description
			y (TYPE): Description
			w (TYPE): Description
			h (TYPE): Description
		"""
		pg.sprite.Sprite.__init__(self)
		self.game = game
		# platform frames
		images = [
		self.game.spritesheet.get_image(0, 288, 380 ,94),
		self.game.spritesheet.get_image(213, 1662, 201, 100)]

		#select random image
		self.image = random.choice(images)
		#self.image = pg.Surface((w, h))
		#self.image.fill(PLATFORM_COLOR)
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y