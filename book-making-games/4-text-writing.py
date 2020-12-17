# -*- coding: utf-8 -*-
"""
There are six steps to making text appear on the screen:

1. Create a pygame.font.Font object.

2. Create a Surface object with the text drawn on it by calling the Font object’s render() method.

3. Create a Rect object from the Surface object by calling the Surface object’s get_rect() method.
 This Rect object will have the width and height correctly set for the text that was rendered,
 but the top and left attributes will be 0.

4. Set the position of the Rect object by changing one of its attributes.
 On line 15, we set the center of the Rect object to be at 200, 150.

5. Blit the Surface object with the text onto
 the Surface object returned by pygame.display.set_mode().

6. Call pygame.display.update() to make the display Surface appear on the screen.
"""

import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True: # main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    # must be called after display.update
    fpsClock.tick(FPS)