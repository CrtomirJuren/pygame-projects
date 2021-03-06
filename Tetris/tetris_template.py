import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""
"""
Python and Pygame Tutorial - Build Tetris! Full GameDev Course
https://www.youtube.com/watch?v=zfvxp7PgQ6c&t=1188s

CURRENT VIDEO POSITION 15:55/1:40:05
"""
pygame.font.init()

# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# SHAPE FORMATS

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape

#main data structure, hold information for pieces
class Piece(object):
  def  __init__(self, x, y, shape):
    self.x = x
    self.y = y
    self.shape = shape
    self.colour = shape_colors[shapes.index(shape)]
    rotation = 0
  pass

def create_grid(locked_positions={}):
  #create a blank grid
  grid = [[(0,0,0) for x in range(10)] for x in range(20)] #10x20 grid of (0,0,0) coulours
  
  for i in range(len(grid): #rows represented by i
    for j in range(len(grid[i]))  #columns by j
    if (j,i) in locked_positions:
      c = locked_positions[(j,i)]
      grid[i][j] = c

  return grid

def convert_shape_format(shape):
  pass

def valid_space(shape, grid):
  pass

def check_lost(positions):
  pass

#randomly picks one of the shapes from the list
#it picks when we need a new shape to fall down
def get_shape():
  return random.choice(shapes)

def draw_text_middle(text, size, color, surface):
  pass

def draw_grid(surface, row, col):
  #we draw a black surface
  surface.fill(0,0,0)
  #set up font for drawing to the screen
  pygame.font.init()
  font = pygame.font.SysFont('comicsans'.60)
  #write the game title
  label = font.render('Tetris',1,(255,255,255))
  #draw label on the middle of the screen
  surface.blit(label, top_left_x + play_width/2 - (label.get_width()/2),30)

  for i in  range(grid):
    for j in range(len(grid[i])):
      pygame.draw.rect(surface,grid[i][j],)

def clear_rows(grid, locked):
  pass

def draw_next_shape(shape, surface):
  pass

def draw_window(surface):
  pass

def main():
  pass

def main_menu():
  pass

main_menu()  # start game