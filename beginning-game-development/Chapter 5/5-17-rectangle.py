# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 11:08:39 2020

@author: crtom
"""


import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

pygame.init()
HEIGHT, WIDTH = (400,400)

#### Create a canvas on which to display everything ####
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

#### Create a surface with the same size as the window ####
background = pygame.Surface((WIDTH, HEIGHT))

#background = pygame.image.load(background_image_filename).convert()
#sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()
position = Vector2(100.0, 100.0)
speed = 250.
heading = Vector2()

sprite = pygame.Surface((50, 50))
sprite.fill((255,255,255))
rect = sprite.get_rect()
rect.center = (WIDTH / 2, HEIGHT / 2)

# at start destination is the same as object position
destination = (WIDTH / 2, HEIGHT / 2)

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == MOUSEBUTTONDOWN:
            destination_x = event.pos[0] - sprite.get_width()/2.0 
            destination_y = event.pos[1] - sprite.get_height()/2.0 
            destination = (destination_x, destination_y)
            print(destination)
    
            heading = Vector2.from_points(position, destination) 
            heading.normalize()
            
    #### Blit the surface onto the canvas ####
    screen.blit(background,(0,0))

    #### Blit the surface onto the canvas ####
    screen.blit(sprite,(int(position.x), int(position.y)))   
    
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    
    distance_moved = time_passed_seconds * speed
    position += heading * distance_moved

        
    pygame.display.update()