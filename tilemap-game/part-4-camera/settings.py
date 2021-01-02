# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:08:54 2020

@author: crtom
"""

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (140, 140, 140)

# game settings
WIDTH = 1024 # divisible by 16*64 32*32
HEIGHT = 768 # 16*48 32*24 66*12

FPS = 60

TITLE = 'Tilemap demo'
BGCOLOR = DARKGREY

TILESIZE = 32

GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# player settings
PLAYER_SPEED = 600 # 100 px/seconds
