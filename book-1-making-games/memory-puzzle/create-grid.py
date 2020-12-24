# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 19:16:26 2020

@author: crtom

 GRID = 600*600
 GRID 6x6 = 36 pieces
 100x100 per square
 one piece is 80x80 + margin = 100x100
"""

# create a list of touple positions
grid_touple_list = []
grid_pixel_pos_list = []
card_position_list = []

for y in range(0, 6):
    for x in range(0, 6):
        grid_touple_list.append((x,y))
        grid_pixel_pos_list.append((x*100, y*100))
        card_position_list.append(((x*100) + 10, (y*100) + 10))

# for x in range(0, 600, 100):
#     for y in range(0, 600, 100):
#         grid_pixel_pos_list.append((x, y))
#         card_position_list.append((x + 10, y + 10))

print(grid_touple_list)
print(grid_pixel_pos_list)
print(card_position_list)