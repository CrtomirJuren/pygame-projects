"""Summary

Attributes:
    BLACK (tuple): Description
    BLUE (tuple): Description
    CYAN (tuple): Description
    FPS (int): Description
    GRAY (tuple): Description
    GREEN (tuple): Description
    HEIGHT (int): Description
    LIME (tuple): Description
    MAGENTA (tuple): Description
    MAROON (tuple): Description
    NAVY (tuple): Description
    OLIVE (tuple): Description
    PURPLE (tuple): Description
    RED (tuple): Description
    SILVER (tuple): Description
    TEAL (tuple): Description
    TITLE (str): Description
    WHITE (tuple): Description
    WIDTH (int): Description
    YELLOW (tuple): Description
"""
# game options/settings
TITLE = "Doodle Jump!"
WIDTH = 480
HEIGHT = 600
WIDTH_MID = WIDTH // 2
HEIGHT_MID = HEIGHT // 2
FPS = 60
FONT_NAME = 'arial'
HIGHSCORE_FILE = "highscore.txt"
SPRITESHEET_FILE ="spritesheet_jumper.png"

#player properties
#if positive = move DOWN, negative = move UP
PLAYER_ACC = 0.7
PLAYER_FRICTION = -0.1
PLAYER_GRAVITY = 1
PLAYER_JUMP_VELOCITY = -40

# Starting platforms Platform(x, y, width, height)
PLATFORM_LIST = [
(0, HEIGHT - 60),
(WIDTH//2-50, HEIGHT*3/4),
(125, HEIGHT-350),
(350, 200),
(175, 100)
]

#RGB color constants
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
RED     = (255,0,0)
LIME    = (0,255,0)
BLUE    = (0,0,255)

YELLOW  = (255,255,0)
CYAN    = (0,255,255)
MAGENTA = (255,0,255)
SILVER  = (192,192,192)
GRAY	= (128,128,128)
MAROON  = (128,0,0)
OLIVE   = (128,128,0)
GREEN   = (0,128,0)
PURPLE  = (128,0,128)
TEAL    = (0,128,128)
NAVY    = (0,0,128)

BG_COLOR = TEAL
PLATFORM_COLOR = LIME