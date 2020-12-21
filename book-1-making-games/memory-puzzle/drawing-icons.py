# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 15:27:13 2020

@author: crtom
"""
import pygame

WHITE   = (255, 255, 255)
BLACK   = (  0,   0,   0)
GREY    = (128, 128, 128)
SILVER  = (192, 192, 192)

RED     = (255,   0,   0)
YELLOW  = (255, 255,   0)
ORANGE  = (255, 128,   0)
MAGENTA = (255,   0, 255)
PURPLE  = (128,   0, 128)

LIME    = (  0, 255,   0)
BLUE    = (  0,   0, 255)
NAVYBLUE= ( 60,  60, 100)
CYAN    = (  0, 255, 255)
GRAY	= (128, 128, 128)
MAROON  = (128,   0,   0)
OLIVE   = (128, 128,   0)
GREEN   = (  0, 128,   0)
TEAL    = (  0, 128, 128)
NAVY    = (  0,   0, 128)


def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)

def draw_circle_alpha(surface, color, center, radius):
    target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.circle(shape_surf, color, (radius, radius), radius)
    surface.blit(shape_surf, target_rect)

def draw_polygon_alpha(surface, color, points):
    lx, ly = zip(*points)
    min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
    target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
    surface.blit(shape_surf, target_rect)

def draw_background():
    background = pygame.Surface(window.get_size())
    ts, w, h, c1, c2 = 50, *window.get_size(), (160, 160, 160), (192, 192, 192)
    tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]

    for rect, color in tiles:
        pygame.draw.rect(background, color, rect)

    window.blit(background, (0, 0))

pygame.init()
window = pygame.display.set_mode((250, 250))
clock = pygame.time.Clock()

#--------------------------------------------
#------------background----------------------
#--------------------------------------------
background = pygame.Surface((250, 250))
background.fill((128,128,128))
window.blit(background, (0, 0))
#print(window.get_size())

#--------------------------------------------
#-------------line icon-------------
#--------------------------------------------
# icon1 = pygame.Surface((50, 50))
# icon1.fill((255,255,255))
# #pygame.draw.line(surface, color, start_pos, end_pos, width) -> Rect
# # draw horizontal line in icon surface
# pygame.draw.line(icon1, BLUE, (5,25), (45,25), 5)
# # draw vertical line in icon surface
# pygame.draw.line(icon1, BLUE, (25,5), (25,45), 5)
# #blit icon on main surface
# window.blit(icon1, (0, 0))

#--------------------------------------------
#----------------triangle icon----------------
#--------------------------------------------
icon3 = pygame.Surface((50, 50))
icon3.fill((255,255,255))
#line(surface, color, start_pos, end_pos, width) -> Rect
# draw horizontal line in icon surface
#Rect(left, top, width, height) -> Rect, Rect((left, top), (width, height)) -> Rect
pygame.draw.polygon(icon3, GREEN, ((10,40),(40,40),(25, 10)),4)
#blit icon on main surface
window.blit(icon3, (0, 0))

#--------------------------------------------
#----------------rectangle empty icon----------------
#--------------------------------------------
#Demo 1: Rectangle
#pygame.draw.rect(surface, color, pygame.Rect(left, top, width, height))

icon2 = pygame.Surface((50, 50))
icon2.fill((255,255,255))
#line(surface, color, start_pos, end_pos, width) -> Rect
# draw horizontal line in icon surface
#Rect(left, top, width, height) -> Rect, Rect((left, top), (width, height)) -> Rect
pygame.draw.rect(icon2, RED, [10,10,30,30],5)
#blit icon on main surface
window.blit(icon2, (60, 0))

#--------------------------------------------
#----------------circle empty icon-----------------
#--------------------------------------------
icon3 = pygame.Surface((50, 50))
icon3.fill((255,255,255))
#line(surface, color, start_pos, end_pos, width) -> Rect
# draw horizontal line in icon surface
#Rect(left, top, width, height) -> Rect, Rect((left, top), (width, height)) -> Rect
pygame.draw.circle(icon3, GREEN, (25, 25 ), 15, 5)
#blit icon on main surface
window.blit(icon3, (120, 0))

#--------------------------------------------
#----------------triangle icon----------------
#--------------------------------------------
icon3 = pygame.Surface((50, 50))
icon3.fill((255,255,255))
#line(surface, color, start_pos, end_pos, width) -> Rect
# draw horizontal line in icon surface
#Rect(left, top, width, height) -> Rect, Rect((left, top), (width, height)) -> Rect
pygame.draw.polygon(icon3, GREEN, ((10,40),(40,40),(25, 10)))
#blit icon on main surface
window.blit(icon3, (0, 60))

# #--------------------------------------------
# #----------------diamond icon----------------
# #--------------------------------------------
# icon4 = pygame.Surface((50, 50))
# icon4.fill((255,255,255))
# #line(surface, color, start_pos, end_pos, width) -> Rect
# # draw horizontal line in icon surface
# #Rect(left, top, width, height) -> Rect, Rect((left, top), (width, height)) -> Rect
# pygame.draw.polygon(icon4, GREEN, ((5,25),(25,5),(45, 25),(25, 45)))
# #blit icon on main surface
# window.blit(icon4, (0, 60))

#--------------------------------------------
#----------------rectangle filled icon----------------
#--------------------------------------------
#Demo 1: Rectangle
#pygame.draw.rect(surface, color, pygame.Rect(left, top, width, height))

icon5 = pygame.Surface((50, 50))
icon5.fill((255,255,255))
#line(surface, color, start_pos, end_pos, width) -> Rect
# draw horizontal line in icon surface
#Rect(left, top, width, height) -> Rect, Rect((left, top), (width, height)) -> Rect
pygame.draw.rect(icon5, RED, [10,10,30,30])
#blit icon on main surface
window.blit(icon5, (60, 60))

#--------------------------------------------
#----------------circle filled icon-----------------
#--------------------------------------------
icon6 = pygame.Surface((50, 50))
icon6.fill((255,255,255))
#line(surface, color, start_pos, end_pos, width) -> Rect
# draw horizontal line in icon surface
#Rect(left, top, width, height) -> Rect, Rect((left, top), (width, height)) -> Rect
pygame.draw.circle(icon6, GREEN, (25, 25 ), 15)
#blit icon on main surface
window.blit(icon6, (120, 60))

#--------------------------------------------
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


#    draw_background()
#    draw_rect_alpha(window, (0, 0, 255, 127), (55, 90, 140, 140))
#    draw_circle_alpha(window, (255, 0, 0, 127), (150, 100), 80)
#    draw_polygon_alpha(window, (255, 255, 0, 127),
#        [(100, 10), (100 + 0.8660 * 90, 145), (100 - 0.8660 * 90, 145)])

    pygame.display.flip()

pygame.quit()
exit()