"""Snake Game Python Tutorial
youtube video: https://www.youtube.com/watch?v=CD4qAhfFuLo
current time: 33:00
"""
import sys
import math
import random
import pygame
from pygame.locals import *
import tkinter as tk
from tkinter import messagebox

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class cube(object):
    """
    """
    w = 500 #set pixel screen width
    rows = 20 #set number of rows

    def __init__(self,start,dirnx=1,dirny=0,color=RED):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self,dirnx,dirny):
        """
        move cube, by adding new direction to previous position
        """
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0]+self.dirnx, self.pos[1]+self.dirny)

    def draw(self,surface,eyes=False):
        """
        drawing: convert x,y grid position to pixel position
        """
        dis = self.w // self.rows #distance between x and y values
        #variables for easy coding
        i = self.pos[0] # row
        j = self.pos[1] # column
        #draw just a little bit less, so we draw inside of the square. and we dont cover grid.
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1,dis-2,dis-2 ))

        #draw eyes
        if eyes:
                centre = dis//2
                radius = 3
                circleMiddle = (i*dis+centre-radius, j*dis+8 ) #eye 1
                circleMiddle2 = (i*dis+dis-radius*2, j*dis+8 ) #eye 2
                pygame.draw.circle(surface, BLACK, circleMiddle, radius)
                pygame.draw.circle(surface, BLACK, circleMiddle2, radius)

def drawGrid(w,rows,surface):
    """
    This function draws a square grid on main display
    """
    #distance between grid lines
    sizeBtwn = w // rows
    x = 0
    y = 0

    #create grid by drawing lines
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        #vertical lines
        pygame.draw.line(surface, WHITE, (x,0), (x,w))
        #horizontal lines
        pygame.draw.line(surface, WHITE, (0,y), (w,y))

def redrawWindow(surface):
    global rows, width, s
    #background
    surface.fill(BLACK)
    #draw grid
    drawGrid(width, rows, surface)
    #update display
    pygame.display.update()


def main():
    global width, rows, s
    #create game display
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width)) #square display

    clock = pygame.time.Clock()

    flag = True
    FPScount = 0
    print(FPScount)
    while flag:
        #pygame.time.delay(50)
        clock.tick(10)  #game max speed 10 FPS
        s.move()
        redrawWindow(win)

        FPScount += 1
        print(f'FPScount:{FPScount}')

#rows = 0
#w = 0
#h = 0

#cube.rows = rows
#cube.w = w
main()
pygame.quit()
sys.exit()