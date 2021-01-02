"""
Game Template
"""
import sys
import pygame as pg
from pygame.locals import*
import random
from settings import *
import time
import math

WIDTH, HEIGHT = 200, 200

# initialize pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()

# game loop
running = True
while running:

	# keep looping at the right speed
	clock.tick(FPS)
	# process input (events)
	for event in pg.event.get(): #check for all events that are happening
		if event.type == pg.QUIT:
			running = False
		if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
			running = False

	# Update
	all_sprites.update()

	# draw/render
	screen.fill(BLACK)
	all_sprites.draw(screen)
	# after drawing everything, flip the display
	pg.display.update()

pg.quit()