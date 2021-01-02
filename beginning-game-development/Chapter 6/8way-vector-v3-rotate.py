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

from math import *

# defines  
WIDTH, HEIGHT = 640, 480

BLACK = (0 , 0 , 0)  
GREEN = (0 , 255 , 0)  


pygame.init()
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

# sprite = pygame.Surface((50, 50))
# sprite.fill((255,255,255))
# rect = sprite.get_rect()
# rect.center = (WIDTH / 2, HEIGHT / 2)

sprite_pos = Vector2(100.0, 100.0)
sprite_speed = 300.
sprite_rotation = 0.
sprite_rotation_speed = 180. # deg/second

#-----------------create sprite - rectangle---------
# define a surface (RECTANGLE)  
sprite_orig = pygame.Surface((50 , 50))  
# for making transparent background while rotating an image  
sprite_orig.set_colorkey(BLACK)  
# fill the rectangle / surface with green color  
sprite_orig.fill(GREEN)  
# creating a copy of orignal image for smooth rotation  
sprite = sprite_orig.copy()  
sprite.set_colorkey(BLACK)  
# define rect for placing the rectangle at the desired position  
rect = sprite.get_rect()  
rect.center = (WIDTH // 2 , HEIGHT // 2)  
# keep rotating the rectangle until running is set to False 
screen.blit(sprite, rect)
#-------------------------------------------------
clock = pygame.time.Clock()

key_direction = Vector2(0, 0)

#main game loop
clock = pygame.time.Clock()
run = True
while run:
    # pygame.time.delay(100) #this will be a clock for the game
    for event in pygame.event.get(): #check for all events that are happening
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
    	
    # key_direction.x, key_direction.y = (0, 0)
    rotation_direction = 0.
    movement_direction = 0.
    
    keystate = pygame.key.get_pressed()

    if keystate[pygame.K_UP]:
        # key_direction = vector_up
        movement_direction = +1
    
    if keystate[pygame.K_DOWN]:
        movement_direction = -1
    
    if keystate[pygame.K_LEFT]:
        rotation_direction = +1
    
    if keystate[pygame.K_RIGHT]:
         rotation_direction = -1
    
    # direction vector is a unit vector, normalize it
    # diagonals are 0.707
    # key_direction.normalize()
    # print(key_direction)
    # sprite calculation
    
    #rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
    #w, h = rotated_sprite.get_size()
    #sprite_draw_pos = Vector2(sprite_pos.x - w/2, sprite_pos.y - h/2)
    #screen.blit(rotated_sprite, sprite_draw_pos)
    #screen.blit(rotated_sprite, (int(sprite_pos.x), int(sprite_pos.y))) 
    
    # calculate times
    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    # calculate sprite rotation and heading
    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds
    
    heading_x = sin(sprite_rotation*pi/180.)
    heading_y = cos(sprite_rotation*pi/180.)
    heading = Vector2(heading_x, heading_y)
    heading *= movement_direction
    
    # calculate sprite positoin    
    sprite_pos += heading * sprite_speed * time_passed_seconds
    #------------------ROTATIONS------------------------
    
    # making a copy of the old center of the rectangle  
    #old_center = rect.center
    
    # now do the drawings 
    rotated_sprite = pygame.transform.rotate(sprite_orig, sprite_rotation)
    rect = rotated_sprite.get_rect()  
    
    # set the rotated rectangle to the old center  
    #rect.center = old_center  
    
    w, h = rotated_sprite.get_size()
    sprite_draw_pos = Vector2(sprite_pos.x-w/2, sprite_pos.y-h/2)    
    
    #------------------DRAWINGS------------------------
    #### Blit the surface onto the canvas ####
    screen.blit(background,(0,0))
    #### Blit the sprite onto canvas
    screen.blit(rotated_sprite, (sprite_draw_pos.x,sprite_draw_pos.y))
    #### display canvas ####
    pygame.display.update()

    #print(*sprite_draw_pos)
    print(rect)
    #print(sprite_rotation)
# exit pygame
pygame.quit()
exit()
