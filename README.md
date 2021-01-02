# pygame-projects


## Links

http://programarcadegames.com/index.php?chapter=example_code

## 1. Import & Initialization

```python
import pygame
pygame.init()
```

## 2. Display, Surfaces, Images, and Transformations

- for computers (x=0,y=0) is top left corner

## Create screen

```python
screen = pygame.display.set_mode((width, height)) 
```

Initializes and creates the window where your game will run, and returns a Surface, here assigned to the name “screen.” Note: you’re passing a tuple, hence the double parenthesis.

## Set title

```python
display.set_caption('Title of the window')
```

## Update - Draw Display: blitting is drawing

```python
pygame.display.update()
```

Redraws the main display surface if argument list is empty. Optionally, you can pass it a list of Rects, and it will just redraw the portions of the screen indicated in the list.

```python
pygame.display.get_surface()
```

Returns a reference to the Surface instantiated with the set_mode() function.
Use this if you forget to assign set_mode() to a name.

```python
screen.blit()
```

Note: “Surface” is the name of the class, so you’d use the name you assigned when you created the surface. For example, if your main display Surface was called “screen” (as it is above), you’d use screen.blit(), not Surface.blit()

```python
Copy pixels from one Surface to another

Surface.blit(sourceSurface, destinationRect, optionalSourceRect) 
```

Used to draw images to the screen. If you omit the third argument, the entire source Surface is copied to the area of the destination Surface specified by the Rect in the second argument

## Drawing objects - primitives

- rectangle

  pygame.draw.rect(surface, color, rectangle_tuple, width)

- polygon

- circle

  pygame.draw.circle(surface, color, center_point, radius, width)

- ellipse

  pygame.draw.ellipse(surface, color, bounding_rectangle, width)

- line

  pygame.draw.line(surface, color, start_point, end_point, width) 

  pygame.draw.lines(surface, color, closed, pointlist, width)

- pixel

- pixel array

```python
pygame.draw.line(Surface, color, (x1,y1), (x2,y2), width)
```

## Colour objects

```python
Creates a color object with RGBA as arguments.

pygame.Color(R, G, B)
black = (0,0,0)
white = (255,255,255)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
```

```python
Fills surface with a solid color.

Surface.fill(R,G,B)
```

# Rectangle

pygame.Rect(top-left-corner-x, top-lef-corner-y, width, height)

spamRect = pygame.Rect(10, 20, 200, 300)

### pygame.Rect: rectangle attributes

**myRect.left**					 integer
**myRect.right	 ** 			integer
**myRect.top** 					integer
**myRect.bottom** 			integer
**myRect.centerx			** integer
**myRect.centery**			 integer
**myRect.width** 				integer
**myRect.height**				integer
**myRect.size** 				   A tuple of two ints: (width, height)
**myRect.topleft** 			 A tuple of two ints: (left, top)
**myRect.topright** 		  A tuple of two ints: (right, top)
**myRect.bottomleft** 	 A tuple of two ints: (left, bottom)
**myRect.bottomright**   A tuple of two ints: (right, bottom)
**myRect.midleft** 			A tuple of two ints: (left, centery)
**myRect.midright** 		 A tuple of two ints: (right, centery)
**myRect.midtop** 			A tuple of two ints: (centerx, top)
**myRect.midbottom** 	A tuple of two ints: (centerx, bottom)

All of these attributes can be assigned to:

```
rect1.right = 10
rect2.center = (20,30)
```

## Convert

Before you use convert() on any surface, screen has to be initialized with set_mode()

```
import pygame
pygame.init()
image = pygame.image.load("file_to_load.jpg")
print(image.get_rect().size) # you can get size
screen = pygame.display.set_mode(image.get_rect().size, 0, 32)
image = image.convert() # now you can convert 
```

- Changes pixel format

```python
Surface.convert()
```

Changes pixel format of the Surface’s image to the format used by the main display. Makes things faster. Use it.

```python
Changes pixel format (transparency)

Surface.convert_alpha()
```

Same as above, but when the Surface’s image has alpha transparency values to deal with.

```python
Get dimensions and location of surface

Surface.get_rect()
```

Returns a Rect that will tell you the dimensions and location of the surface.

```python
Loads image from disk and gets image size

image = pygame.image.load('filename')
image_width = image.get_rect().size[0]
image_height = image.get_rect().size[1]

```

Note that in Python, directories are indicated by a forward slash, unlike Windows 

- Rotates Surface counterclockwise by degrees

```python
pygame.transform.rotate(Surface, angle)
```

- Resizes Surface to new resolution

```python
pygame.transform.scale(Surface, (width, height)) 
```

## Circles

```python
pygame.draw.circle(gameDisplay, self.colour, (self.x, self.y), self.size, self.thickness)

## Rectangles
- Returns a Rect moved x pixels horizontally and y pixels vertically
Rect.move(x, y)
```

- Moves the Rect x pixels horizontally and y pixels vertically

```python
Rect.move_ip(x, y) 
```

Assignable attributes (in most cases, a tuple of x and y values):
top, left, bottom, right, topleft, bottomleft, topright, bottomright, midtop, midleft, midbottom, midright, center, centerx, centery, size, width, height

# Display examples

- Classical way of creating image on display

```python
    #1.) draw background, dont paint it over image
    gameDisplay.fill(white)
    #2.) draw image on position (x,y)
    x = display_width*0.45
    y = display_height*0.8
    #use blit to add image to surface
    gameDisplay.blit(carImg,(x,y))
    #3.) update display
    pygame.display.update()
```

## Time

- Create a Clock object 

```python
pygame.time.Clock() 
```

(assign this to a name), which you can then call the tick() method on to find out how much time has passed since the last time you called tick()

```python
Returns the clock framerate

pygame.time.Clock.get_fps()
```

```python
Pause game for time specified

pygame.time.delay(milliseconds)
```

```python
Returns the number of milliseconds passed since pygame.init() was called

pygame.time.get_ticks() 
```

```python
Returns the time used in previous tick

pygame.time.Clock.get_time()
```

## Joystick

    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()

## Events

```python
Key press events
        #if key pressed start moving
        if event.type == pygame.EVENTDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
                
        #if key released stop moving
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT::
                x_change = 0

```

this code changes position only if key is pressed down.
When key is released. change is zero.

```python
Event for closing main windows press on (x)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
    pygame.quit()
```

One of the most common ways of event handling, Its a loop which constantly checks for events, quits if the QUIT event is triggered and
prevents your game from freezing.

```python
Places a new event that you specify on the queue

pygame.event.post()
```

```python
Creates a new event object

pygame.event.Event()
```

```python
Gets the event from the queue

pygame.event.get()
```

```python
Remove all the events from the queue

pygame.event.clear()
```

Events are always in a queue. Order of events does matter.

```python
Get a list of events

pygame.event.get() 
```

Call once per frame to get a list of events that occurred since the last time pygame.event.get() was called.

- Event type values:
  - QUIT one
  - KEYDOWN unicode, key, mod (if you import pygame.locals, compare to e.g. K_a for “a”)
  - KEYUP key, mod
  - MOUSEMOTION pos, rel, buttons
  - MOUSEBUTTONUP pos, button
  - MOUSEBUTTONDOWN pos, button
  - JOYAXISMOTION joy, axis, value

### Mouse events

- lmb, mmb, rmb = pygame.mouse.get_pressed Returns the mouse buttons pressed as a tuple of three
  booleans, one for the left, middle, and right mouse buttons.
-  pygame.mouse.get_rel—Returns the relative mouse movement (or mickeys) as a tuple
  with the x and y relative movement.
- pygame.mouse.get_pos—Returns the mouse coordinates as a tuple of the x and y values.
- pygame.mouse.set_pos—Sets the mouse position. Takes the coordinate as a tuple or list
  for x and y.
- pygame.mouse.set_visible—Changes the visibility of the standard mouse cursor. If
  False, the cursor will be invisible
- pygame.mouse.get_focused—Returns True if the Pygame window is receiving mouse
  input. When Pygame runs in a window, it will only receive mouse input when the window
  is selected and at the front of the display.
- pygame.mouse.set_cursor—Sets the standard cursor image. This is rarely needed since
  better results can be achieved by blitting an image to the mouse coordinate.
- pyGame.mouse.get_cursor—Gets the standard cursor image. See the previous item.

### Joystic Events

• pygame.joystick.init—Initializes the joystick module. This is called automatically by
pygame.init, so you rarely need to call it yourself.
• pygame.joystick.quit—Uninitializes the joystick module. Like init, this function is
called automatically and so is not often needed.
• pygame.joystick.get_init—Returns True if the joystick module has been initialized. If it
returns False, the following joystick functions won’t work.
• pygame.joystick.get_count—Returns the number of joysticks currently plugged into
the computer.
• pygame.joystick.Joystick—Creates a new joystick object that is used to access all information
for that stick. The constructor takes the ID of the joystick—the first joystick is ID
0, then ID 1, and so on, up to the number of joysticks available on the system.

## Fonts

```python
f = pygame.font.Font(None, 32) 
```

Creates a font object of size 32 using the default font. If you know where the .TTF file of the font you want to use is located, you can use the filename as the first argument

- create a message and display it on screen

```

```

## Rendering

```python
surf = f.render(“Hello”, 1, (255,0,255), (255,255,0))
```

Creates a surface of rendered text using the font of the font object. The first argument is the text itself, the second is whether the text is anti-aliased or not (0 for no), the third argument is a 3-item tuple that defines the RGB values of the color of the text, and the fourth (optional) argument is a 3-item tuple that defines the RGB values of the color of the background. If the fourth argument is not specified, the background will be transparent. This command creates a surface that has the word Hello in magenta on a yellow background, which can then be blitted to the screen like any surface. It’s quite ugly.

## Audio

### Initialize

```
pygame.mixer.init()
```

### Playing Sound Effects

```python
# 1. create a sound object
soundObj = pygame.mixer.Sound('beeps.wav') # must be an uncompressed WAV or OGG
# 2. start sound
soundObj.play()
# 3. wait and let the sound play for 1 second
time.sleep(1) 
# 4. stop sound
soundObj.stop()
```

### Playing Background

For background music, you do not create objects, since you can only have one music track running at any time. Music is streamed, never fully loaded at once. You can use MIDI files.

```python
pygame.mixer.music.load(filename)
pygame.mixer.music.play(loops=0, offset) #  -1 to repeat indefinitely, offset in sec
pygame.mixer.music.stop()
```

# Sprites,module with basic game object classes

| [pygame.sprite.Sprite](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite) | Simple base class for visible game objects.                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [pygame.sprite.DirtySprite](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.DirtySprite) | A subclass of Sprite with more attributes and features.      |
| [pygame.sprite.Group](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group) | A container class to hold and manage multiple Sprite objects. |
| [pygame.sprite.RenderPlain](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.RenderPlain) | Same as pygame.sprite.Group                                  |
| [pygame.sprite.RenderClear](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.RenderClear) | Same as pygame.sprite.Group                                  |
| [pygame.sprite.RenderUpdates](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.RenderUpdates) | Group sub-class that tracks dirty updates.                   |
| [pygame.sprite.OrderedUpdates](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.OrderedUpdates) | RenderUpdates sub-class that draws Sprites in order of addition. |
| [pygame.sprite.LayeredUpdates](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.LayeredUpdates) | LayeredUpdates is a sprite group that handles layers and draws like OrderedUpdates. |
| [pygame.sprite.LayeredDirty](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.LayeredDirty) | LayeredDirty group is for DirtySprite objects. Subclasses LayeredUpdates. |
| [pygame.sprite.GroupSingle](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.GroupSingle) | Group container that holds a single sprite.                  |
| [pygame.sprite.spritecollide](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.spritecollide) | Find sprites in a group that intersect another sprite.       |
| [pygame.sprite.collide_rect](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.collide_rect) | Collision detection between two sprites, using rects.        |
| [pygame.sprite.collide_rect_ratio](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.collide_rect_ratio) | Collision detection between two sprites, using rects scaled to a ratio. |
| [pygame.sprite.collide_circle](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.collide_circle) | Collision detection between two sprites, using circles.      |
| [pygame.sprite.collide_circle_ratio](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.collide_circle_ratio) | Collision detection between two sprites, using circles scaled to a ratio. |
| [pygame.sprite.collide_mask](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.collide_mask) | Collision detection between two sprites, using masks.        |
| [pygame.sprite.groupcollide](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.groupcollide) | Find all sprites that collide between two groups.            |
| [pygame.sprite.spritecollideany](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.spritecollideany) | Simple test if a sprite intersects anything in a group.      |

### Class pygame.sprite.Sprite

*Simple base class for visible game objects.*

| [pygame.sprite.Sprite.update](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite.update) | method to control sprite behavior       |
| ------------------------------------------------------------ | --------------------------------------- |
| [pygame.sprite.Sprite.add](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite.add) | add the sprite to groups                |
| [pygame.sprite.Sprite.remove](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite.remove) | remove the sprite from groups           |
| [pygame.sprite.Sprite.kill](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite.kill) | remove the Sprite from all Groups       |
| [pygame.sprite.Sprite.alive](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite.alive) | does the sprite belong to any groups    |
| [pygame.sprite.Sprite.groups](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite.groups) | list of Groups that contain this Sprite |

### Class pygame.sprite.Group

*A container class to hold and manage multiple Sprite objects.*

| [pygame.sprite.Group.sprites](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.sprites) | list of the Sprites this Group contains     |
| ------------------------------------------------------------ | ------------------------------------------- |
| [pygame.sprite.Group.copy](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.copy) | duplicate the Group                         |
| [pygame.sprite.Group.add](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.add) | add Sprites to this Group                   |
| [pygame.sprite.Group.remove](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.remove) | remove Sprites from the Group               |
| [pygame.sprite.Group.has](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.has) | test if a Group contains Sprites            |
| [pygame.sprite.Group.update](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.update) | call the update method on contained Sprites |
| [pygame.sprite.Group.draw](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.draw) | blit the Sprite images                      |
| [pygame.sprite.Group.clear](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.clear) | draw a background over the Sprites          |
| [pygame.sprite.Group.empty](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.empty) | remove all Sprites                          |

## Default subclassing Sprite Object

```python
class Block(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
```

# Groups, and Collision Detection

Check if a sprite collides with a group. If collision, returns True

```python
# check if sprite and a group walls collides
if pg.sprite.spritecollideany(self, self.game.walls)
```
Check for collision

```
hits = pg.sprite.spritecollide(self, self.game.walls, False) 
```



```python
class Monster(pygame.sprite.Sprite):
def __init__(self):
pygame.sprite.Sprite.__init__(self)
self.image = pygame.image.load(“monster.png”)
self.rect = self.image.get_rect()
...
monsters = pygame.sprite.RenderPlain((monster1, monster2, monster3))
monsters.update()
monsters.draw()
Rect.contains(Rect): return True or False
Rect.collidepoint(x, y): return True or False
Rect.colliderect(Rect): return True or False
Rect.collidelist(list): return index
pygame.sprite.spritecollide(sprite, group, dokill):
return Sprite_list
pygame.sprite.groupcollide(group1, group2, dokill1,
dokill2): return Sprite_dict
```

### Updating sprites icons

This two codes are the same

```python
    self.all_sprites.draw(self.screen)
```
```python
for sprite in self.all_sprites:
    self.screen.blit(sprite.image, sprite.rect)
```
## OOP Examples

- drawing a circle

```
class Particle:
  def __init__(self, (x, y), size):
    self.x = x
    self.y = y
    self.size = size
    self.colour = (0, 0, 255)
    self.thickness = 1

    def display(self):
      pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

particle = Particle((150, 50), 15)
particle.display()
```

## Resources

- [PyGame with Python 3 WEBSITE](https://pythonprogramming.net/pygame-python-3-part-1-intro/)
- [PyGame with Python 3 YOUTUBE](https://www.youtube.com/watch?list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&v=ujOTNg17LjI&feature=emb_title)
- [pygame cheat sheet](pygame-cheatsheet.pdf)
- [create an image with GIMP](https://www.youtube.com/watch?v=5myI73oFvAA)
- SW to create image with transparent background
  [GIMP open source image editor](https://www.gimp.org/)


# Examples

## Simplest pygame code

```python
import pygame

pygame.init()

#### Create a canvas on which to display everything ####
window = (400,400)
screen = pygame.display.set_mode(window)
#### Create a canvas on which to display everything ####

#### Create a surface with the same size as the window ####
background = pygame.Surface(window)
#### Create a surface with the same size as the window ####

#### Populate the surface with objects to be displayed ####
pygame.draw.rect(background,(0,255,255),(20,20,40,40))
pygame.draw.rect(background,(255,0,255),(120,120,50,50))
#### Populate the surface with objects to be displayed ####

#### Blit the surface onto the canvas ####
screen.blit(background,(0,0))
#### Blit the surface onto the canvas ####

#### Update the the display and wait ####
pygame.display.flip()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
#### Update the the display and wait ####

pygame.quit()
```

## 1_Intro

[readme](1_intro/readme.md)

## Tetris

[Python and Pygame Tutorial - Build Tetris! Full GameDev Course](https://www.youtube.com/watch?v=zfvxp7PgQ6c&t=1188s)

## Tile map editor

www.mapeditor.org

Loading .tmx files made from tile-editors. 

INSTAL pip install pytmx



## **GAME PHYSICS - MECHANICS**

### Tweening- easing functions

- linear
- quadratic
- cubic
- quartic
- quintic
- sinusoidal
- exponential
- crcular
- elastic
- back

```python
conda install -c conda-forge pytweening
```

