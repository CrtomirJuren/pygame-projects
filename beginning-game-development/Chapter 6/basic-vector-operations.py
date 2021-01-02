# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 21:10:25 2020

@author: crtom
"""

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

# draw antialiase line for vectors
from pygame import gfxdraw

from math import *

# defines  
WIDTH, HEIGHT = 640, 480

WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
RED     = (255,0,0)
LIME    = (0,255,0)
BLUE    = (0,0,255)
YELLOW  = (255,255,0)
CYAN    = (0,255,255)
MAGENTA = (255,0,255)
SILVER  = (192,192,192)
GREY	= (128,128,128)
MAROON  = (128,0,0)
OLIVE   = (128,128,0)
GREEN   = (0,128,0)
PURPLE  = (128,0,128)
TEAL    = (0,128,128)
NAVY    = (0,0,128)

pygame.init()
#### Create a canvas on which to display everything ####
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
#set windows title
pygame.display.set_caption("vector arrow")

#### Create a surface with the same size as the window ####
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(WHITE)

clock = pygame.time.Clock()

def draw_point(screen, color, p, radius): #, color, position, radius
    
    point = (int(p[0]), int(p[1]))
    
    pygame.draw.circle(screen, color, point, radius)
    

def draw_line(screen, color, startpoint, vector, width):
    """
    Draws line representing vector.
    """

    v1 = Vector2(vector.x, vector.y)
    
    endpoint = (v1.x + startpoint[0], v1.y + startpoint[1])
    
    startpoint = (int(startpoint[0]), int(startpoint[1]))
    endpoint = (int(endpoint[0]), int(endpoint[1]))
    
    pygame.draw.line(screen, color, startpoint, endpoint, width)

# ----------drawing
p_A = (WIDTH // 2, HEIGHT // 2)
p_B = (WIDTH // 2, 50)
vector_AB = Vector2.from_points(p_A, p_B)

# print(p_A)
# print(p_B)
# #as_tuple


#------------------------
screen.blit(background, (0,0))

draw_point(screen, RED, p_A, 5)
pygame.display.update()

draw_point(screen, BLUE, p_B, 5)
pygame.display.update()

# draw_line(screen, color, startpoint, vector, width):
# ORIGINAL VECTOR
draw_line(screen, BLACK, p_A, vector_AB, 3)
pygame.display.update()

# ROTATED VECTOR
angle = 45
x_rot = cos(angle)*vector_AB.x - sin(angle)*vector_AB.y
y_rot = sin(angle)*vector_AB.x + cos(angle)*vector_AB.y
vector_AB_rot = Vector2(x_rot, y_rot)
draw_line(screen, GREY, p_A, vector_AB_rot, 3)

# perpendicualar vector
vector_AB_perp = Vector2(-vector_AB_rot.y, vector_AB_rot.x)
draw_line(screen, GREY, p_A, vector_AB_perp, 3)
pygame.display.update()

# arrow head to original vector
# first find point on original vector that is a little bellow vector endpoint
vector_norm = Vector2(vector_AB.x, vector_AB.y)
vector_norm.normalise()
vector_norm *= 10
vector_norm = vector_AB - vector_norm
draw_line(screen, GREY, p_A, vector_norm, 3)
pygame.display.update()

# find perpendicular vector to original
vector_perp = Vector2(-vector_AB.y, vector_AB.x)
vector_perp.normalise()
vector_perp *= 5

point = (int(vector_norm.x) +  p_A[0], int(vector_norm.y) +  p_A[1])
point = (point[0], point[1])

draw_point(screen, BLACK, point, 5)

draw_line(screen, GREY, point, vector_perp, 3)
draw_line(screen, GREY, point, -vector_perp, 3)

# pointL = original_vector_startpoint+
point_R = (point[0] + vector_perp.x, point[1] + vector_perp.y)
point_L = (point[0] - vector_perp.x, point[1] - vector_perp.y)
draw_point(screen, BLACK, point_R, 5)
draw_point(screen, BLACK, point_L, 5)

endpoint = vector_AB.x+ p_A[0], vector_AB.y + p_A[1]

# draw rectangle
pygame.draw.polygon(screen, GREEN, (point_L, point_R, endpoint))

pygame.display.update()

print(vector_AB)
print(vector_norm)
print(point)
print(vector_perp)
# draw_line(screen, RED, p_A, vector_a, 3)
# pygame.display.update()





#----------------------
#main game loop
clock = pygame.time.Clock()
run = True
angle = 0.
while run:
    # pygame.time.delay(100) #this will be a clock for the game
    for event in pygame.event.get(): #check for all events that are happening
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
    
    # calculate times
    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

# exit pygame
pygame.quit()
exit()

"""
    #draw_arrow(screen, 0, 10, GREEN)
    #------------------DRAWINGS------------------------
    #### Blit the surface onto the canvas ####
    screen.blit(background,(0,0))
    #### Blit the points onto canvas
    
    angle += 0.01
    
    
    #draw_arrow(screen, colour, startpoint, vector, width):
    draw_point(screen, BLUE, p_A, 5)
    #draw_point(screen, GREEN, p_B, 5)
    draw_arrow(screen, BLUE, p_A, vector_AB_rot, 2)
    #screen.blit(arrow, arrow_pos)
    #### display canvas ####
    pygame.display.update()
    x_rot = cos(angle)*vector_AB.x - sin(angle)*vector_AB.y
    y_rot = sin(angle)*vector_AB.x + cos(angle)*vector_AB.y
    
    vector_AB_rot = Vector2(x_rot, y_rot)
"""