import pygame
import time
import random

pygame.init()
#---------game constants variables-------------
display_width = 800
display_height = 600
#RGB color constants 
black = (0,0,0)
white = (255,255,255)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
#------------------------------------------------------
#create main display window
gameDisplay = pygame.display.set_mode((display_width,display_height))
#set main display window title
pygame.display.set_caption('Race Game')

clock = pygame.time.Clock()
#-------------------load images-----------------------------------
# load image
carImg = pygame.image.load('race_car_transp_v2.png')
#get image size in pixels. for colision detection
carImg_width = carImg.get_rect().size[0]
carImg_height = carImg.get_rect().size[1]

#-------------------FUNCTIONS------------------------------------
#creating things that move towards car
def things(thingx,thingy,thingw,thingh,color):
	pygame.draw.rect((gameDisplay),color,[thingx,thingy,thingw,thingh])

#function to display a car
def car(x,y):
	gameDisplay.blit(carImg,(x,y)) #we blit car image to a surface

def text_objects(text,font):
	textSurface = font.render(text, True, black)
	return	textSurface, textSurface.get_rect()

def message_display(text):
	#define look of the writing
	largeText = pygame.font.Font('freesansbold.ttf',100)
	#create a custom function for message box display
	TextSurf, TextRect = text_objects(text, largeText)
	#center the message box display on of the middle screen
	TextRect.center =((display_width/2),(display_height/2))
	#draw image with blit
	gameDisplay.blit(TextSurf,TextRect)
	#update display
	pygame.display.update()
	time.sleep(2)
	game_loop()

def crash():
	message_display('You Chrashed')

def game_loop():
	x = display_width*0.45
	y = display_height*0.8
	#for computers (x=0,y=0) is top left corner

#--------------------main game loop--------------------
	x_change = 0
	
	#objects apear randomly on x axis
	thing_startx = random.randrange(0,display_width)
	#start object off the screen-above 
	thing_starty = -600
	thing_speed = 7
	thing_width = 100 #pixles
	thing_height = 100

	gameExit = False

	while not gameExit:

		#------------key press game logic-------------
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				#gameExit = True
				pygame.quit()
				quit()	

				#if key pressed start moving
			if event.type == pygame.KEYDOWN:
			    if event.key == pygame.K_LEFT:
			    	x_change = -5
			    elif event.key == pygame.K_RIGHT:
			    	x_change = 5

				#if key released stop moving
			if event.type == pygame.KEYUP:
			    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
			    	x_change = 0

		x += x_change

		#------------graphics and logic----------------------
		#draw background
		gameDisplay.fill(white)	
		#draw things
		things(thing_startx, thing_starty,thing_width,thing_height,black)
		#move things
		thing_starty += thing_speed
		#draw car
		car(x,y)				
		#----------check boundaries for chrash----------
		if x > display_width - carImg_width or x < 0:
			crash()
			gameExit = True
		#----------is thing thing that moves off the screen----------
		if thing_starty > display_height:
			thing_starty = 0 - thing_height 
			thing_startx = random.randrange(0,display_width)
		#start is 600 off the screen
		#start is 600 off the screen

		pygame.display.update() #update all changes to display
		clock.tick(60)	
#------------------------------------
game_loop()		#game is running here, until pygame.QUIT
#pygame.quit()	
#quit()