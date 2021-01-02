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

# draw_point(screen, RED, p_A, 5)
# pygame.display.update()

# draw_point(screen, BLUE, p_B, 5)
# pygame.display.update()

# draw_line(screen, color, startpoint, vector, width):
# ORIGINAL VECTOR
# draw_line(screen, BLACK, p_A, vector_AB, 3)
# pygame.display.update()

# ROTATED VECTOR
angle = 45
x_rot = cos(angle)*vector_AB.x - sin(angle)*vector_AB.y
y_rot = sin(angle)*vector_AB.x + cos(angle)*vector_AB.y
vector_AB_rot = Vector2(x_rot, y_rot)
# draw_line(screen, GREY, p_A, vector_AB_rot, 3)

# perpendicualar vector
vector_AB_perp = Vector2(-vector_AB_rot.y, vector_AB_rot.x)
# draw_line(screen, GREY, p_A, vector_AB_perp, 3)
# pygame.display.update()

# arrow head to original vector
# first find point on original vector that is a little bellow vector endpoint
vector_norm = Vector2(vector_AB.x, vector_AB.y)
# vector_norm.normalise()
vector_norm *= 10
vector_norm = vector_AB - vector_norm
# draw_line(screen, GREY, p_A, vector_norm, 3)
# pygame.display.update()

# find perpendicular vector to original
vector_perp = Vector2(-vector_AB.y, vector_AB.x)
vector_perp.normalize()
vector_perp *= 5

point = (int(vector_norm.x) +  p_A[0], int(vector_norm.y) +  p_A[1])
point = (point[0], point[1])

# draw_point(screen, BLACK, point, 5)

draw_line(screen, GREY, point, vector_perp, 3)
draw_line(screen, GREY, point, -vector_perp, 3)

# pointL = original_vector_startpoint+
point_R = (point[0] + vector_perp.x, point[1] + vector_perp.y)
point_L = (point[0] - vector_perp.x, point[1] - vector_perp.y)
# draw_point(screen, BLACK, point_R, 5)
# draw_point(screen, BLACK, point_L, 5)

endpoint = vector_AB.x+ p_A[0], vector_AB.y + p_A[1]

# draw rectangle
# pygame.draw.polygon(screen, GREEN, (point_L, point_R, endpoint))

# pygame.display.update()

# print(vector_AB)
# print(vector_norm)
# print(point)
# print(vector_perp)
# draw_line(screen, RED, p_A, vector_a, 3)
# pygame.display.update()

def draw_vector(screen, startpoint, vector, color, width, DEBUG = False):
    """
             E
            ***
           *****
          L**M**R
             *
             *
             *
             *
         ----S-----
             *
             *
             O
    
    E - vector endpoint  
    M - arrow midpoint  
    L - arrow left point  
    R - arrow right point  
    """
    #------------CALCULATIONS---------------
    #DEBUG = False
    # create points
    E = (0, 0) 
    L = (0, 0)
    M = (0, 0)
    R = (0, 0)

    # copy vector to new
    v = Vector2(int(vector.x), int(vector.y))
    
    # 1) set S - starrpoint
    S = (startpoint[0], startpoint[1])
    
    # 2) set E - endpoint
    E = (v.x + S[0], v.y + S[1])
    
    # 3) Find vector SM
    v_SM = Vector2(v.x, v.y)
    v_SM.normalize()
    v_SM *= 2*width # v_SM *= 10
    v_SM = v - v_SM
    
    M = (S[0]+v_SM.x, S[1]+v_SM.y) 
    
    # 3) Find perpendicular vector
    v_perp = Vector2(-v.y, v.x)
    v_perp.normalize()
    v_perp *= width # v_perp *= 5
    
    # 4) Find arrow head points
    L = (M[0] - v_perp.x, M[1] - v_perp.y)
    R = (M[0] + v_perp.x, M[1] + v_perp.y)
    
    #------------DRAWINGS---------------
    # pixels must be integers
    E = (int(E[0]),int(E[1]))
    M = (int(M[0]),int(M[1]))
    L = (int(L[0]),int(L[1]))
    R = (int(R[0]),int(R[1]))
    
    # draw main vector line
    pygame.draw.line(screen, color, S, M, width)
    
    # draw points for debugging purpose
    # points = S, E, L, M, R
    if DEBUG:
        print('S = ', S)
        print('E = ', E)
        print('M = ', M)
        print('M = ', L)
        print('M = ', R)
        pygame.draw.circle(screen, BLUE, S, 5)
        pygame.draw.circle(screen, BLUE, E, 5)
        
        pygame.draw.circle(screen, GREEN, M, 5)
        pygame.draw.circle(screen, RED, L, 5)
        pygame.draw.circle(screen, GREY, R, 5)
    
    # draw arrow head poligone
    # if very short, dont draw arrow
    #length = sqrt(v.x
    pygame.draw.polygon(screen, color, (L, R, E))
    
draw_vector(screen, p_A, vector_AB, BLACK, 5)

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

    angle += 0.01

    x_rot = cos(angle)*vector_AB.x - sin(angle)*vector_AB.y
    y_rot = sin(angle)*vector_AB.x + cos(angle)*vector_AB.y
    vector_AB_rot = Vector2(x_rot, y_rot)

    # get X component
    magnitude = sqrt(vector_AB.x**2 + vector_AB.y**2)
    
    direction = Vector2(vector_AB_rot.x, vector_AB_rot.y)
    direction.normalize()
    # print(direction)
    
    #x_component = magnitude * sin(angle)
    x_component = direction.x * magnitude
    y_component = direction.y * magnitude
    #y_component = magnitude * cos(angle)
    
    # print('angle:', angle, 'x_component:', x_component,'y_component:', y_component)
    
    v_x = Vector2(x_component, 0)
    v_y = Vector2(0, y_component)
    
    #---------------UPDATE DISPALY-----------
    screen.blit(background, (0,0))
    # draw circle
    
    pygame.draw.circle(screen, GREY, p_A, int(magnitude),2)
    pygame.draw.line(screen, GREY, (0, HEIGHT//2), (WIDTH, HEIGHT//2), 2)
    pygame.draw.line(screen, GREY, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 2)
    
    draw_vector(screen, p_A, vector_AB_rot, BLACK, 5)
    draw_vector(screen, p_A, v_x, RED, 5)
    draw_vector(screen, p_A, v_y, BLUE, 5)

    # update all drawing objects
    pygame.display.update()
    
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