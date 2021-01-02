# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 18:28:20 2020

@author: crtom
"""
import pygame as pg
from settings import * 

# collision function of two sprites
def collide_hit_rect(one, two):
    # normal collision does this
    #return one.rect.colliderect(two.rect)
    return one.hit_rect.colliderect(two.rect)
    
class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip()) # remove new line char at end
                # print(line)
    
        # how big map is
        self.tilewidth = len(self.data[0]) # N of columns
        self.tileheight = len(self.data) # N of rows
        
        # pixel width of the map
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

# camera object is independant from other objects. it needs only tilemap
class Camera:
    # 1. must shift the drawing rectangle to what we want to draw
    # 2. camera must update to where the player offset is
    
    """ theory
    - Returns a Rect moved x pixels horizontally and y pixels vertically
    Rect.move(x, y)
    """
    def __init__(self, width, height):
        # use rectangle to track camera
        #self.camera = pg. Rect(SHIFT_X, SHIFT_Y, width, height)
        self.camera = pg. Rect(0, 0, width, height)
        self.width = width
        self.height = height
        
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
    
    # update and follow targeted sprite
    def update(self, target):
        # if player moves to right, map moves to the left
        x = -target.rect.centerx + int(WIDTH / 2)
        y = -target.rect.centery + int(HEIGHT / 2)
        
        # now limit scrolling, so we dont see over the map
        x = min(0, x) # left side
        y = min(0, y) # top side
        
        x = max(-(self.width - WIDTH), x) # right side
        y = max(-(self.height - HEIGHT), y) # bottom side
                
        
        # ADJUST WHERE our camera rectangle is
        self.camera = pg.Rect(x, y, self.width, self.height)
    