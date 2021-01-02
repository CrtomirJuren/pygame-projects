"""
Basic Movement and Key Presses
video: https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5

1. create a rectangle
2. move it by key pressed
"""

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

pygame.init()

WIDTH, HEIGHT = 640, 480
#### Create a canvas on which to display everything ####
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
#set windows title
pygame.display.set_caption("8 way movement vector")

#### Create a surface with the same size as the window ####
background = pygame.Surface((WIDTH, HEIGHT))

#character variables
x = 50
y = 50
width = 40
height = 60
vel = 5

sprite = pygame.Surface((50, 50))
sprite.fill((255,255,255))
rect = sprite.get_rect()
rect.center = (WIDTH / 2, HEIGHT / 2)

clock = pygame.time.Clock()
sprite_pos = Vector2(100.0, 100.0)
sprite_speed = 300.

clock = pygame.time.Clock()
#main game loop
run = True
while run:
    # pygame.time.delay(100) #this will be a clock for the game
    for event in pygame.event.get(): #check for all events that are happening
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
    	
    key_direction = Vector2(0, 0)
    keystate = pygame.key.get_pressed()

    if keystate[pygame.K_UP]:
        key_direction.y = -1
    if keystate[pygame.K_DOWN]:
        key_direction.y = +1
    if keystate[pygame.K_LEFT]:
        key_direction.x = -1
    if keystate[pygame.K_RIGHT]:
        key_direction.x = +1		
    
    #if diagonal movement
    if key_direction.x != 0 and key_direction.y !=0:
        key_direction.x = 0.707*key_direction.x
        key_direction.y = 0.707*key_direction.y
    
    # make sure direction vector is a unit vector
    key_direction.normalize()
    
    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0
    
    sprite_pos += key_direction * sprite_speed * time_passed_seconds
    #### Blit the surface onto the canvas ####
    screen.blit(background,(0,0))
    
    #### Blit the surface onto the canvas ####
    screen.blit(sprite,(int(sprite_pos.x), int(sprite_pos.y))) 
    
    
    pygame.display.update()

# exit pygame
pygame.quit()
exit()
