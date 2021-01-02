# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 16:29:01 2020

@author: crtom

https://www.youtube.com/watch?v=Qdeb1iinNtk&list=PLX5fBCkxJmm1fPSqgn9gyR3qih8yYLvMj&index=2

Pygame Tutorial - Making a Platformer ep. 2: Images, Input, and Collisions
"""

import sys
import pygame
from pygame.locals import*
import random
#from settings import *
import time
import math

from gameobjects.vector2 import Vector2
from RGB import *

WIDTH, HEIGHT = 400, 400

# initialize pygame and create a window
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")


#all_sprites = pygame.sprite.Group()

# create background
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(WHITE)
screen.blit(background, (0,0))

# create player image
player_image = pygame.Surface((50, 50))
player_image.fill(BLACK)

player_pos = Vector2(200, 150)
player_speed = 300

screen.blit(player_image, (player_pos.x, player_pos.y))

# game loop
clock = pygame.time.Clock()
running = True
while running:

    # process input (events)
    for event in pygame.event.get(): #check for all events that are happening
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    
    pressed_keys = pygame.key.get_pressed()
    key_direction = Vector2(0, 0)
    
    if pressed_keys[K_LEFT]:
        key_direction.x = -1
    elif pressed_keys[K_RIGHT]:
         key_direction.x = +1
    if pressed_keys[K_UP]:
        key_direction.y = -1
    elif pressed_keys[K_DOWN]:
        key_direction.y = +1
    
    
    key_direction.normalize()
    
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    #----------
    player_pos += key_direction * player_speed * time_passed_seconds
        
    # draw/render
    screen.blit(background, (0,0))
    #all_sprites.draw(screen)
    # screen.blit(player_image, (50, 50))

    screen.blit(player_image, (player_pos.x, player_pos.y))
    # after drawing everything, flip the display
    pygame.display.update()

pygame.quit()
